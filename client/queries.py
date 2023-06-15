from __future__ import print_function

import os
import grpc

from config_parser import DFParser
from protos import modules_pb2, modules_pb2_grpc

class QuerieManager:
    def __init__(self, data:DFParser) -> None:
        """Класс, ответственный за создание очереди и поочередное выполнение запросов 

        Args:
            data (DFParser): Полученные из парсера конфигурационного файла данные
        """
        self.data = data

    def run(self):
        """Поочередно выполняет запросы из конфигурационного файла"""
        print("Initializing...\n")
        for request in self.data.general_data.request:
            print(f"Performing {request}\n Inititaliazing...")
            print(f'{str(request).upper()}')
            print(os.getenv(f'{str(request).upper()}'))
            with grpc.insecure_channel(f"{request}:{os.getenv(f'{str(request).upper()}')}") as channel:
                stub = modules_pb2_grpc.ModuleStub(channel)
                method = getattr(self, request)
                method(stub)

    def faceswap(self, stub):
        """Выполняет запрос к микросервису

        Args:
            stub (_type_): объект из  автогенерированного gRPC кода
        """
        if self.data.general_data.type == "image":
            response = stub.SimSwapImage(modules_pb2.ModuleRequest(
                    isMultiple = self.data.general_data.multiple,
                    text = self.data.faceswap.create_command_string())
                )
        else:   # здесь else а не elif т.к. эта проверка происходит в парсере
            response = stub.SimSwapVideo(modules_pb2.ModuleRequest(
                    isMultiple = self.data.general_data.multiple,
                    text = self.data.faceswap.create_command_string())
                )

        print("Received: " + str(response.message))

    def ghost(self, stub):
        """Выполняет запрос к микросервису

        Args:
            stub (_type_): объект из  автогенерированного gRPC кода
        """
        if self.data.general_data.type == "image":
            response = stub.GhostImage(modules_pb2.ModuleRequest(
                    isMultiple = self.data.general_data.multiple,
                    text = self.data.ghost.create_command_string())
                )
        else:
            response = stub.GhostVideo(modules_pb2.ModuleRequest(
                    isMultiple = self.data.general_data.multiple,
                    text = self.data.ghost.create_command_string())
                )
        print("Received: " + str(response.message))