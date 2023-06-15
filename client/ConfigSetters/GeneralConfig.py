class GeneralConfig:
    
    def __init__(self, json_file: dict) -> None:
        """Хранит основные аргументы запроса:

        - `type:str` - тип изображения (image\video)
        - `multiple:bool` - обработка одного или нескольких изображений
        - `request:str[]` - порядок выполнения запросов

        Args:
            json_file (dict): загруженный в виде словаря json файл
        """
        self.type = json_file['type']
        self.multiple = json_file['multiple']
        self.request = json_file['request']