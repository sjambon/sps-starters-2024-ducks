# Dockerfile
FROM node:16 AS builder

WORKDIR /app

# Copy package.json to the builder image
COPY package.json ./

# Generate package-lock.json without installing dependencies
RUN npm install --package-lock-only

# This stage is for generating package-lock.json
FROM node:16 AS final

# Set the working directory in the final image
WORKDIR /app

# Copy the generated package-lock.json from the builder stage
COPY --from=builder /app/package-lock.json ./
COPY package.json ./
RUN npm install react-router-dom

# Copy the rest of the application code
COPY . .

# Build the React app
RUN npm run build

# Install serve to serve the static files
RUN npm install -g serve

# Command to run the app
CMD ["serve", "-s", "build"]
