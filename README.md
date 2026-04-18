<div align="center">
<h1>FastAPI CRUD + Redis Cache</h1>
<p align="center">A clean, fast, and production-ready example of a CRUD API built with FastAPI, PostgreSQL, and Redis caching.</p>

[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff)](#)
[![FastAPI](https://img.shields.io/badge/FastAPI-009485.svg?logo=fastapi&logoColor=white)](#)
[![Postgres](https://img.shields.io/badge/Postgres-%23316192.svg?logo=postgresql&logoColor=white)](#)
[![Redis](https://img.shields.io/badge/Redis-%23DD0031.svg?logo=redis&logoColor=white)](#)
[![Pydantic](https://img.shields.io/badge/Pydantic-E92063?logo=Pydantic&logoColor=white)](#)
[![uv](https://img.shields.io/badge/uv-261230.svg?logo=uv&logoColor=#de5fe9)](#)
[![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=fff)](#)

</div>

## Features

- Full async CRUD operations
- Smart Redis caching for GET endpoints (with automatic cache invalidation on create/update/delete)
- PostgreSQL via Tortoise ORM + asyncpg
- Pydantic v2 models & strict validation
- Dependency injection & clean project structure
- Managed with **uv** – the blazingly fast Python package manager

## API Endpoints

| Method   | Endpoint             | Description                     |
| -------- | -------------------- | ------------------------------- |
| `GET`    | `/api/v1/users`      | List all users                  |
| `POST`   | `/api/v1/users`      | Create a new user               |
| `GET`    | `/api/v1/users/{id}` | Get user by ID (cached)         |
| `PUT`    | `/api/v1/users/{id}` | Update user (invalidates cache) |
| `DELETE` | `/api/v1/users/{id}` | Delete user (invalidates cache) |

## Quick Start
> [!TIP]
> `http://localhost:8000/docs` - Swagger \
> `http://localhost:5000` - PgAdmin

- Clone repo

```bash
git clone https://github.com/Fsoky/fastapi-crud.git
cd fastapi-crud
```

- Docker compose up

```bash
docker compose up
```
