from pydantic import BaseModel
from typing import Any


class ServiceResponse(BaseModel):
    """
    Standard service response wrapper.

    Attributes:
        success (bool): Indicates if the response is successful.
        status (int): HTTP-like status code of the response.
        data (Any): Payload of the response, e.g., dict, list, etc.
        message (str | None): Optional message providing additional info.
    """
    
    success: bool
    status: int = 200
    data: Any = None
    message: str | None = None

    @classmethod
    def ok(
        cls,
        data: Any = None,
        message: str | None = None,
        status: int = 200
    ) -> "ServiceResponse":
        """
        Create a successful service response.

        Args:
            data (Any): Response payload, e.g., dict, list, etc.
            message (str | None): Optional message.
            status (int): Status code of the response. Defaults to 200.

        Returns:
            ServiceResponse: Instance representing a successful response.
        """
        return cls(success=True, status=status, data=data, message=message)

    @classmethod
    def error(
        cls,
        message: str,
        data: Any = None,
        status: int = 400
    ) -> "ServiceResponse":
        """
        Create an error service response.

        Args:
            message (str): Error message.
            data (Any): Optional payload providing additional info.
            status (int): Status code of the response. Defaults to 400.

        Returns:
            ServiceResponse: Instance representing an error response.
        """
        return cls(success=False, status=status, message=message, data=data)

    def response(self) -> dict[str, Any]:
        """
        Convert the ServiceResponse instance to a dict suitable for API responses.

        Returns:
            dict[str, Any]: Dictionary containing 'content' and 'status_code'.
        """
        return {
            "content": {
                "data": self.data,
                "message": self.message,
                "success": self.success
            },
            "status_code": self.status,
        }


class BaseService:
    
    def ok(
        self,
        data: Any = None,
        message: str | None = None,
        status: int = 200
    ) -> ServiceResponse:
        return ServiceResponse.ok(data=data, message=message, status=status)

    def error(
        self,
        message: str,
        data: Any = None,
        status: int = 400
    ) -> ServiceResponse:
        return ServiceResponse.error(message=message, data=data, status=status)
