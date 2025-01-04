from pydantic import BaseModel, Field
from typing_extensions import Literal, TypedDict, Annotated


def NonNegativeFloat(
    desc: str = "This is a non-negative float.",
) -> Annotated[float, Field]:
    return Annotated[
        float,
        Field(
            ge=0.0,
            description=desc,
        ),
    ]
