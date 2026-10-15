# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a small REST API with FastAPI by defining endpoints, validating request data, and returning appropriate HTTP responses.

## 📝 Tasks

### 🛠️ Create the Books API

#### Description

Complete the starter application so it provides REST endpoints for an in-memory collection of books.

#### Requirements

Completed program should:

- Start a FastAPI application that can be run with Uvicorn.
- Define a `GET /books` endpoint that returns all books.
- Define a `GET /books/{book_id}` endpoint that returns one book by its ID.
- Return a `404` response when a requested book does not exist.

### 🛠️ Add Create and Update Operations

#### Description

Add endpoints that allow clients to create new books and update existing books.

#### Requirements

Completed program should:

- Define a `POST /books` endpoint that accepts a validated `BookCreate` request body.
- Assign a unique ID to each new book and return the created book.
- Define a `PUT /books/{book_id}` endpoint that updates an existing book.
- Return a `404` response when an update targets a book that does not exist.

### 🛠️ Document and Test the API

#### Description

Use FastAPI's built-in documentation and send requests to verify each endpoint behaves correctly.

#### Requirements

Completed program should:

- Use Pydantic models to validate required fields such as `title` and `author`.
- Return clear response data for successful and unsuccessful requests.
- Verify the endpoints using the interactive documentation at `/docs`.
- Include at least one example request and response in the student's submission notes.
