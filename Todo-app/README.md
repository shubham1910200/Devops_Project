
# 🚀 Todo App

A simple **Todo web application** built using **Flask** and Docker.

## 📚 Table of Contents
1. [Prerequisites](#prerequisites)
2. [Installation](#installation)
3. [Running the Application](#running-the-application)
4. [Running Tests](#running-tests)
5. [Docker Setup (Optional)](#docker-setup-optional)
6. [Contributing](#contributing)
7. [License](#license)

---

## Prerequisites

Before you begin, make sure you have the following installed:
- **Python 3.10** (or higher)
- **pip** (Python package installer)
- **Docker** (optional, for containerized environment)
- **Git** (for cloning the repository)

---

## Installation

### Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/shubham1910200/Devops_Project.git
cd Devops_Project/Todo-app
```

### Install Dependencies

Once inside the `Todo-app` directory, install the required dependencies using `pip`:

```bash
pip install -r requirements.txt
```

This will install all necessary Python packages, including **Flask**.

---

## Running the Application

### Run with Python

Once the dependencies are installed, you can start the application locally using Python:

```bash
python app.py
```

The app will be accessible at [http://localhost:5000](http://localhost:5000).

### Run with Docker

If you prefer to run the application inside a Docker container:

1. Build the Docker image:

```bash
docker build -t soma1999/todo-app .
```

2. Run the Docker container:

```bash
docker run -p 5000:5000 soma1999/todo-app
```

The app will be accessible at [http://localhost:5000](http://localhost:5000).

---

## Running Tests

To ensure everything is working, you can run the unit tests for the application.

### Run Tests Locally

If you want to run the tests locally:

```bash
python -m unittest discover -s tests
```

### Run Tests in Docker

Alternatively, you can run the tests inside the Docker container:

```bash
docker run --rm -v $(pwd):/app soma1999/todo-app:latest python3 -m unittest discover -s tests
```

---

## Docker Setup (Optional)

If you haven't installed Docker yet, follow the instructions for your operating system:

- Install Docker: [Docker Installation Guide](https://docs.docker.com/get-docker/)

Once Docker is installed, you can build and run the app using the commands provided above.

---

## Contributing

We welcome contributions! To contribute to this project, follow these steps:

1. Fork the repository.
2. Create a new branch:

```bash
git checkout -b feature-branch
```

3. Make your changes.
4. Commit your changes:

```bash
git commit -am 'Add new feature'
```

5. Push your branch:

```bash
git push origin feature-branch
```

6. Open a pull request with a description of your changes.

---

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more details.
```

