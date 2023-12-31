"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
This is a commons file containing special proto messages for the
server and client to communicate with each other.
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _Status:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _StatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_Status.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    READY: _Status.ValueType  # 0
    RUNNING: _Status.ValueType  # 1
    FINISHED: _Status.ValueType  # 2

class Status(_Status, metaclass=_StatusEnumTypeWrapper): ...

READY: Status.ValueType  # 0
RUNNING: Status.ValueType  # 1
FINISHED: Status.ValueType  # 2
global___Status = Status

@typing_extensions.final
class Tensor(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BUFFER_FIELD_NUMBER: builtins.int
    SIZE_FIELD_NUMBER: builtins.int
    DTYPE_FIELD_NUMBER: builtins.int
    CHUNKS_FIELD_NUMBER: builtins.int
    buffer: builtins.bytes
    @property
    def size(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    dtype: builtins.str
    chunks: builtins.int
    def __init__(
        self,
        *,
        buffer: builtins.bytes = ...,
        size: collections.abc.Iterable[builtins.int] | None = ...,
        dtype: builtins.str = ...,
        chunks: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["buffer", b"buffer", "chunks", b"chunks", "dtype", b"dtype", "size", b"size"]) -> None: ...

global___Tensor = Tensor
