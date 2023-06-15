from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ModuleReply(_message.Message):
    __slots__ = ["message"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class ModuleRequest(_message.Message):
    __slots__ = ["isMultiple", "text"]
    ISMULTIPLE_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    isMultiple: bool
    text: str
    def __init__(self, isMultiple: bool = ..., text: _Optional[str] = ...) -> None: ...
