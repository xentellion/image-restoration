class DFGhost:
    def __init__(self, json_file: dict) -> None:
        """Класс-родитель, хрянящий данные для Ghost

        Args:
            json_file (dict): часть конфигурационного файла, полученная в виде словаря
        """
        self.source_image = json_file['source_image']
        self.target_file = json_file['target_file']
        self.output_path = json_file['output_file']

    def create_command_string(self) -> str:
        """Генерирует аргументы типа `--name Name ...` для использования в скриптах ghost
        в формате строки
        """
        raise NotImplementedError()
    

class DFGhostImage(DFGhost):
    def __init__(self, json_file: dict) -> None:
        """Создает объект, хранящий параметры для Ghost для фотографий

        Args:
            json_file (dict): часть конфигурационного файла, полученная в виде словаря
        """
        super(DFGhostImage, self).__init__(json_file)

    def create_command_string(self) -> str:
        return f'--source_paths {self.source_image} --target_image {self.target_file} \
            --out_image_name {self.output_path} --image_to_image True'


class DFGhostVideo(DFGhost):
    def __init__(self, json_file: dict) -> None:
        """Создает объект, хранящий параметры для Ghost для видео

        Args:
            json_file (dict): часть конфигурационного файла, полученная в виде словаря
        """
        super(DFGhostVideo, self).__init__(json_file)

    def create_command_string(self) -> str:
        return f'--source_paths {self.source_image} --target_video {self.target_file} \
            --out_video_name {self.output_path}'