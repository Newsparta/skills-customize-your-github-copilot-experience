# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a simple REST API using FastAPI by creating endpoints for reading and managing data, validating input, and returning structured JSON responses.

## 📝 Tasks

### 🛠️ Set Up a FastAPI App

#### Description
Create a FastAPI application that starts successfully and exposes a basic health check endpoint for testing.

#### Requirements
Completed program should:

- Import and initialize a `FastAPI` app
- Add a `GET` endpoint at `/health` that returns a JSON status message
- Run the app locally using Uvicorn or FastAPI's development server
- Confirm the endpoint responds successfully in a browser or with a client request

### 🛠️ Create a Resource and Add CRUD Endpoints

#### Description
Build a small API for managing a list of tasks or items using in-memory storage.

#### Requirements
Completed program should:

- Define a model for the resource using `pydantic` with required fields
- Add endpoints to create, read, update, and delete items
- Use appropriate HTTP methods such as `GET`, `POST`, `PUT`, and `DELETE`
- Store data temporarily in memory for the current running app
- Return JSON responses that match the model structure

### 🛠️ Validate Input and Improve Responses

#### Description
Add validation and cleaner API behavior so client requests are checked before they are processed.

#### Requirements
Completed program should:

- Validate required fields and data types using request models
- Return clear error responses for invalid input
- Use response models or structured JSON for consistent output
- Include at least one example request and response in the project documentation
