What is Docker ?
- Docker is a open platform for developing, shipping and running applications.
- A way to package applications with all the necessary dependencies and configurations.
- Portable artifacts, easily share and move this package to any environment.
- Makes the development and deployment more easy and efficient.

## Docker Image
1. Package or Artifact
2. Move or share this Artifact to any environment

## Docker Container
1. Docker Image - Run
2. Start the application
3. Create a Container -> Environment


## Docker Vs Virtual Machine
* Operating System : Docker uses the host operating system, VM uses its own operating system.

* Docker
- Docker Image size is usually smaller (MB).
- Dockers containers start and run must faster.

* VM
- VM Image size is usually larger (GB).
- VMs containers start and run must slower.

## Compatibility
- {Install VM on any OS}
- {Docker Images -> Compatibility Issues}

## Commands - Creating a Docker Image
`docker build -t welcome-app .` - to build the image.

`docker images` - to check the images.

`docker run -p 5000:5000 welcome-app` - to run the container.

`docker ps` - to check how many containers are running.

`docker ps -a` - to check all the containers.

`docker stop <container-id>` - to stop the container.

## Push Docker Image to Docker Hub
`docker login` - to login to docker hub.
[JourneyToDocker423]

`docker image rm -f welcome-app` - to remove the image.

## Now, Again Build the Image
`docker build -t anandacdr/docker-app .` - to build the image.

`docker tag anandacdr/docker-app anandacdr/welcome-app1` - to tag (change) the image name.

`docker push anandacdr/docker-app:latest` - to push the image to docker hub.

`docker image rm -f anandacdr/docker-app` - to remove the image.

`docker run -d -p 5000:5000 anandacdr/docker-app` - to run the container.

`docker ps` - to check how many containers are running.

