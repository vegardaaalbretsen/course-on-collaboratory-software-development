# Docker Cheat Sheet

## Useful Docker Commands

### Basic Docker Commands

- `docker --version` - Check Docker version
- `docker run <image>` - Run a Docker container from an image, you can add many options to this command, like `-d` to run in detached mode, `-p` to map ports, `--name` to give the container a name, and many more.
- `docker ps` - List running Docker containers
- `docker ps -a` - List all Docker containers (running and stopped)
- `docker stop <container>` - Stop a running container
- `docker rm <container>` - Remove a stopped container
- `docker inspect <container>` - Get detailed information about a container
- `docker logs <container>` - View logs of a container
- `docker exec -it <container> <command>` - Execute a command inside a running container, `-it` allows for interactive terminal access
- `docker exec -it <container> /bin/bash` - Access the bash shell of a running container if it has bash installed
- `docker network create <network>` - Create a new Docker network
- `docker network attach <network> <container>` - Attach a container to a network
- `docker volume create <volume>` - Create a new Docker volume

### Docker Compose Commands

- `docker-compose up` - Start services defined in a docker-compose.yml file
- `docker-compose down` - Stop and remove containers defined in a docker-compose.yml file
- `docker-compose ps` - List containers managed by Docker Compose
- `docker-compose logs` - View logs from services defined in a docker-compose.yml file

### Building Docker Images

- `docker build -t <image-name> <path>` - Build a Docker image from a Dockerfile
- `docker build -t <image-name>:<tag> <path>` - Build a Docker image with a specific tag
- `docker compose up --build` - Build images before starting containers in the case using self built images in docker-compose.yml
- `docker tag <image> <new-image-name>` - Tag an image with a new name
- `docker push <image>` - Push an image to a Docker registry (like Docker Hub)