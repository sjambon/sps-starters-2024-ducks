# DUCKS - Document Upload, Collaboration, and Knowledge Storage

## Overview

DUCKS, Document Upload, Collaboration, and Knowledge Storage, is a modern application that organizes data using a duck-themed framework.

### Components

- **Frontend**: React application for user interaction.
- **Backend**: Flask API for managing data.
- **Database**: PostgreSQL for storage.
- **S3 Storage**: For file uploads.

### Getting Started

For local development execute the following commands in root folder

Setting up Podman
```
podman machine init
podman machine start
```

And to build the application.

```
podman-compose build
podman-compose up -d --force-recreate
```
