from pydantic import BaseModel


class Request(BaseModel):
    """Model for incoming request data."""

    model_path: str
    input_data: dict
