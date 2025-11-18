# FastAPI CRUD + Redis Cache
**A clean, fast, and production-ready example of a CRUD API built with FastAPI, PostgreSQL, and Redis caching.**

<div align="center">
<h3>Technology Stack</h3>

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![PostgreSQL](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Redis](https://img.shields.io/badge/redis-%23DD0031.svg?style=for-the-badge&logo=redis&logoColor=white)
![Pydantic](https://img.shields.io/badge/pydantic-%23E92063.svg?style=for-the-badge&logo=pydantic&logoColor=white)
![uv](https://img.shields.io/badge/uv-%23DE5FE9.svg?style=for-the-badge&logo=uv&logoColor=white)

</div>

## Features
- Full async CRUD operations
- Smart Redis caching for GET endpoints (with automatic cache invalidation on create/update/delete)
- PostgreSQL via Tortoise ORM + asyncpg
- Pydantic v2 models & strict validation
- Dependency injection & clean project structure
- Managed with **uv** – the blazingly fast Python package manager

## API Endpoints

| Method   | Endpoint                  | Description                     |
|----------|---------------------------|---------------------------------|
| `GET`    | `/api/v1/users`           | List all users                  |
| `POST`   | `/api/v1/users`           | Create a new user               |
| `GET`    | `/api/v1/users/{id}`      | Get user by ID (cached)         |
| `PUT`    | `/api/v1/users/{id}`      | Update user (invalidates cache) |
| `DELETE` | `/api/v1/users/{id}`      | Delete user (invalidates cache) |

## Quick Start

```bash
git clone https://github.com/Fsoky/fastapi-crud.git
cd fastapi-crud

# Using uv (recommended)
uv sync

# Run
uv run -m src.__main__
```

## TODO
- [ ] Tests (pytest)
- [ ] Docker
