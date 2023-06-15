import json
from ConfigSetters import GeneralConfig, SimswapConfig, GhostConfig

class DFParser:
    def __init__(self, path: str) -> None:
        """Выделяет  и хранит основные 
        аргументы запроса (тип, выполняемые типы обработки) и специфики для каждого 
        модуля (например, параметры для faceswap) из предоставленного json файла
        """
        self.general_data = None
        self.faceswap = None
        self.__parse_json(path)
    
    def __parse_json(self, path: str):
        """Выделяет из json файла основные и модульные аргументы

        Args:
            path (str): Путь к конфигурационному файлу

        Raises:
            CannotDefineDeepfakeType: Ошибка неверно указанного типа обрабатываемого контента
        """
        with open(path, 'r') as config_file:
            config = json.load(config_file)
        # выделяем из config ключевые аргуемнты (тип, запрос и множественные ли снимки)
        self.general_data = GeneralConfig.GeneralConfig(config)
        # Основываясь на типе дипфейка выделяем из файла детали запроса
        if self.general_data.type == 'image':
            self.__parse_for_image(config)
        elif self.general_data.type == 'video':
            self.__parse_for_video(config)
        else:
            raise CannotDefineDeepfakeType(self.general_data.type)

    def __parse_for_video(self, config: dict):
        """Сохраняет настройки для обработки видео

        Args:
            config (dict): Словарь, полученный из json файла
        """
        self.faceswap = SimswapConfig.DFSimSwapVideo(config['faceswap'])
        self.ghost = GhostConfig.DFGhostVideo(config['ghost'])

    def __parse_for_image(self, config: dict):
        """Сохраняет настройки для обработки изображения

        Args:
            config (dict): Словарь, полученный из json файла
        """
        self.faceswap = SimswapConfig.DFSimSwapPhoto(config['faceswap'])
        self.ghost = GhostConfig.DFGhostImage(config['ghost'])


class CannotDefineDeepfakeType(Exception):
    def __init__(self, dftype: str) -> None:
        """Ошибка неверно указанного типа обрабатываемого контента
        Args:
            dftype (str): Полученный неверный тип контента
        """
        self.message = f"'type' в config.json должен быть 'image' или 'video', получено '{dftype}'"
        super().__init__(self.message) 