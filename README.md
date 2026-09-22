# SWE40006 Deployment Task 4

## Software Deployment and Evolution

This repository contains the implementation for SWE40006 Task 4: Container Application Deployment using Docker.

## Task 4.2 - Credit

The Credit-level implementation contains a Python Flask web application containerized using Docker.

Key features:
- Python Flask web application
- Dockerfile configuration
- Dependency management using requirements.txt
- Local Docker image build and container deployment
- Host-to-container port mapping
- Docker Hub image publishing
- Multi-platform Docker image support
- Deployment to a secondary Docker host using AWS EC2

## Task 4.3 - Distinction

The Distinction-level implementation contains a new FastAPI web application with additional Docker deployment features.

Key features:
- FastAPI web application
- Optimized Dockerfile
- Python slim base image
- Docker layer caching
- Non-root container user
- Docker environment variables
- Custom Docker network
- Health endpoint
- Multi-platform Docker image
- AWS EC2 deployment
- Public HTTP accessibility

## Docker Hub Images

Credit:
`yuchenzhang111/swe40006-task4-credit:1.0`

Distinction:
`yuchenzhang111/swe40006-task4-distinction:1.0`

## Project Structure

- `credit-app/` contains the Task 4.2 implementation.
- `distinction-app/` contains the Task 4.3 implementation.

## Security

Secrets, environment files, virtual environments, and AWS PEM private keys are excluded from version control.
