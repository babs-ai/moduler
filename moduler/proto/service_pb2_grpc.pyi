"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import collections.abc
import grpc
import grpc.aio
import service_pb2
import typing

_T = typing.TypeVar('_T')

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta):
    ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore
    ...

class ModuleStub:
    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    execute: grpc.UnaryUnaryMultiCallable[
        service_pb2.Request,
        service_pb2.Response,
    ]

class ModuleAsyncStub:
    execute: grpc.aio.UnaryUnaryMultiCallable[
        service_pb2.Request,
        service_pb2.Response,
    ]

class ModuleServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def execute(
        self,
        request: service_pb2.Request,
        context: _ServicerContext,
    ) -> typing.Union[service_pb2.Response, collections.abc.Awaitable[service_pb2.Response]]: ...

def add_ModuleServicer_to_server(servicer: ModuleServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
