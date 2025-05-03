# Learn Dockerfile with a python Project

This repository contains a python project that can be easily run using Docker. Follow the steps below to set up and run the project.

## Getting Started

**Note:** Ensure that the `Dockerfile` exists in the `python-app` directory before proceeding.

### 1. Clone the Repository
```sh
git clone https://github.com/DevOps-Lebondeveloppeur/python-app
cd python-app
```

### 2. Build the Docker Image
```sh
docker build -t python-app-image .
```

### 3. Run the Docker Container
```sh
docker run -d --name python-app-container -p 5005:5001 python-app-image
```

## Access the Application
Open your browser and navigate to:
```
http://localhost:5005
```
# ci-cd-workshop
# ci-cd-workshop
