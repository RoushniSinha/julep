# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .agent_default_settings import AgentDefaultSettings
from .instruction import Instruction

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Agent(pydantic.BaseModel):
    name: str = pydantic.Field(description="Name of the agent")
    about: str = pydantic.Field(description="About the agent")
    instructions: typing.Optional[typing.List[Instruction]] = pydantic.Field(
        description="List of instructions for the agent"
    )
    created_at: typing.Optional[dt.datetime] = pydantic.Field(
        description="Agent created at (RFC-3339 format)"
    )
    updated_at: typing.Optional[dt.datetime] = pydantic.Field(
        description="Agent updated at (RFC-3339 format)"
    )
    id: str = pydantic.Field(description="Agent id (UUID)")
    default_settings: typing.Optional[AgentDefaultSettings] = pydantic.Field(
        description="Default settings for all sessions created by this agent"
    )
    model: str = pydantic.Field(description="The model to use with this agent")

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {
            "by_alias": True,
            "exclude_unset": True,
            **kwargs,
        }
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {
            "by_alias": True,
            "exclude_unset": True,
            **kwargs,
        }
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        json_encoders = {dt.datetime: serialize_datetime}
