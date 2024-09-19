#!/bin/sh

echo "Starting entrypoint.sh"

# Function to check if PostgreSQL is ready
postgres_ready() {
    python << END
import sys
import psycopg2
from urllib.parse import urlparse
url = urlparse("${DATABASE_URL}")
try:
    conn = psycopg2.connect(
        dbname=url.path[1:],
        user=url.username,
        password=url.password,
        host=url.hostname,
        port=url.port
    )
except psycopg2.OperationalError:
    sys.exit(-1)
sys.exit(0)
END
}

# Wait for PostgreSQL to be ready
until postgres_ready; do
    >&2 echo "PostgreSQL is unavailable - sleeping"
    sleep 1
done

>&2 echo "PostgreSQL is up - executing command"

# Initialize migrations if migrations folder is missing
if [ ! -d "migrations/env.py" ]; then
  flask db init   # Initialize migrations
  flask db migrate -m "Initial migration"
fi

# Run migrations to apply any new changes
flask db upgrade

# Execute the CMD
exec "$@"
