from dataclasses import dataclass
from typing import Any


@dataclass
class ServiceResponse:
    data: dict[str, Any] | list[dict[str, Any]]
    status: int = 200