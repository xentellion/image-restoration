# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from protos import modules_pb2 as protos_dot_modules__pb2


class ModuleStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SimSwapImage = channel.unary_unary(
                '/module.Module/SimSwapImage',
                request_serializer=protos_dot_modules__pb2.ModuleRequest.SerializeToString,
                response_deserializer=protos_dot_modules__pb2.ModuleReply.FromString,
                )
        self.SimSwapVideo = channel.unary_unary(
                '/module.Module/SimSwapVideo',
                request_serializer=protos_dot_modules__pb2.ModuleRequest.SerializeToString,
                response_deserializer=protos_dot_modules__pb2.ModuleReply.FromString,
                )
        self.GhostImage = channel.unary_unary(
                '/module.Module/GhostImage',
                request_serializer=protos_dot_modules__pb2.ModuleRequest.SerializeToString,
                response_deserializer=protos_dot_modules__pb2.ModuleReply.FromString,
                )
        self.GhostVideo = channel.unary_unary(
                '/module.Module/GhostVideo',
                request_serializer=protos_dot_modules__pb2.ModuleRequest.SerializeToString,
                response_deserializer=protos_dot_modules__pb2.ModuleReply.FromString,
                )


class ModuleServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SimSwapImage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SimSwapVideo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GhostImage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GhostVideo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ModuleServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SimSwapImage': grpc.unary_unary_rpc_method_handler(
                    servicer.SimSwapImage,
                    request_deserializer=protos_dot_modules__pb2.ModuleRequest.FromString,
                    response_serializer=protos_dot_modules__pb2.ModuleReply.SerializeToString,
            ),
            'SimSwapVideo': grpc.unary_unary_rpc_method_handler(
                    servicer.SimSwapVideo,
                    request_deserializer=protos_dot_modules__pb2.ModuleRequest.FromString,
                    response_serializer=protos_dot_modules__pb2.ModuleReply.SerializeToString,
            ),
            'GhostImage': grpc.unary_unary_rpc_method_handler(
                    servicer.GhostImage,
                    request_deserializer=protos_dot_modules__pb2.ModuleRequest.FromString,
                    response_serializer=protos_dot_modules__pb2.ModuleReply.SerializeToString,
            ),
            'GhostVideo': grpc.unary_unary_rpc_method_handler(
                    servicer.GhostVideo,
                    request_deserializer=protos_dot_modules__pb2.ModuleRequest.FromString,
                    response_serializer=protos_dot_modules__pb2.ModuleReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'module.Module', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Module(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SimSwapImage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/module.Module/SimSwapImage',
            protos_dot_modules__pb2.ModuleRequest.SerializeToString,
            protos_dot_modules__pb2.ModuleReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SimSwapVideo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/module.Module/SimSwapVideo',
            protos_dot_modules__pb2.ModuleRequest.SerializeToString,
            protos_dot_modules__pb2.ModuleReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GhostImage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/module.Module/GhostImage',
            protos_dot_modules__pb2.ModuleRequest.SerializeToString,
            protos_dot_modules__pb2.ModuleReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GhostVideo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/module.Module/GhostVideo',
            protos_dot_modules__pb2.ModuleRequest.SerializeToString,
            protos_dot_modules__pb2.ModuleReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
