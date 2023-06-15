"""Модуль, отвественный за хранение аргументов и генерацию набора команд для Simswap
"""

class DFSimSwapBase:

    def __init__(self, json_file: dict) -> None:
        """Класс-родитель, хрянящий общие данные для всех типов 
        запросов

        Args:
            json_file (dict): часть конфигурационного файла, полученная в виде словаря
        """
        self.name = json_file['name']
        self.source_image = json_file['source_image']
        self.target_file = json_file['target_file']
        self.output_path = json_file['output_file']
        self.arc_path = json_file['arc_path']
    
    def create_command_string(self):
        """Генерирует аргументы типа `--name Name ...` для использования в скриптах simswap
        в формате строки
        """
        raise NotImplementedError()


class DFSimSwapPhoto(DFSimSwapBase):

    def __init__(self, json_file: dict) -> None:
        """Создает объект, хранящий параметры для SimSwap для фотографий

        Args:
            json_file (dict): часть конфигурационного файла, полученная в виде словаря
        """
        super(DFSimSwapPhoto, self).__init__(json_file)

    def create_command_string(self) -> str:
        return  f'--name {self.name} --Arc_path {self.arc_path} '\
                f'--pic_a_path {self.source_image} --pic_b_path {self.target_file} '\
                f'--output_path {self.output_path}'


class DFSimSwapVideo(DFSimSwapBase):

    def __init__(self, json_file: dict) -> None:
        """Создает объект, хранящий параметры для SimSwap для видео

        Args:
            json_file (dict): часть конфигурационного файла, полученная в виде словаря
        """
        super(DFSimSwapVideo, self).__init__(json_file)
        self.temp_path = json_file['temp_path']
        self.crop_size = json_file['crop_size']
        self.use_mask = json_file['use_mask']

    def create_command_string(self) -> str:
        return  f'--name {self.name} --Arc_path {self.arc_path} '\
                f'--pic_a_path {self.source_image} --video_path {self.target_file} '\
                f'--temp_path {self.temp_path} --output_path {self.output_path} '\
                f'--crop_size {self.crop_size} {"--use_mask" if self.use_mask else ""}'