from pydantic import BaseModel, Field
from typing_extensions import Literal, TypedDict, Annotated


class RequestData(BaseModel):
    """Type specification for incoming request data and validation logic."""

    ## I have included some examples and illustrative comments to help you
    ## understand what to do.
    # 1. List the fields you expect in the incoming request data.
    # 2. For each field, specify the type of the field, similarly to how
    # feature1 is specified as a float below. Keep in mind that the request
    # comes in as a json and is converted to a dictionary.
    # 3. You should also specify a description and example value for each field.
    #
    feature1: Annotated[float, Field(
        alias="Feature1",
        ge=0.0,
        le=10.0,
        description="This is an example feature. \
                The field name `feature1` means that the incoming \
                request data should have a key-value pair \
                with the key `feature1`. Notice also that the type \
                is given to be float. This means that the value \
                corresponding to the key `feature1` should be something \
                that can be converted to a float. '2' can be. 'two' cannot. \
                Also note the ge and le arguments. These are used to specify \
                constraints on the field. For a full list of constraints, \
            see the Pydantic documentation (https://docs.pydantic.dev/latest/api/fields/).",
        example=2.0,
    )

    year_feature: int = Field(
        alias="YearFeature",
        ge=1900,
        le=2025,
        description="This is another example feature. \
                The field name `year_feature` means that the incoming \
                request data should have a key-value pair with `year_feature` \
                as the key. The type is given to be int. \
                Also note the ge, le, gt, lt, and multiple_of arguments. \
                These are used to specify constraints on the field. \
                Since the field is a year, it should be greater than or equal to say 1900, \
                but less than or equal to the current year.",
        example=2021,
    )
