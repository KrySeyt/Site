from typing import Any

from pydantic import BaseModel, Field


class ValidationErrorSchema(BaseModel):
    detail: list[dict[str, Any]] = Field(description="Default detail of validation error", example=[
        {
            "loc": [
                "body",
                "phone_number"
            ],
            "msg": "field required",
            "type": "value_error.missing",
        }
    ])
