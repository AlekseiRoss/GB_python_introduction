import os
import logging
from collections import namedtuple

# Настройка логирования
logging.basicConfig(filename='directory_info.log',
                    level=logging.INFO,
                    format='%(asctime)s - %(message)s')

# Создание объекта namedtuple для хранения информации о файлах и каталогах
FileInfo = namedtuple(
    'FileInfo',
    ['name', 'extension', 'is_directory', 'parent_directory'])


def process_directory(path):
    try:
        # Получение списка файлов и каталогов в указанной директории
        items = os.listdir(path)

        # Обход элементов в директории
        for item in items:
            item_path = os.path.join(path, item)

            # Определение имени, расширения и флага каталога для текущего
            # элемента
            name, extension = os.path.splitext(item)
            is_directory = os.path.isdir(item_path)

            # Создание объекта FileInfo
            file_info = FileInfo(name, extension, is_directory,
                                 os.path.basename(path))

            # Логирование информации
            logging.info(f'Name: {file_info.name}, '
                         f'Extension: {file_info.extension}, '
                         f'Directory: {file_info.is_directory}, '
                         f'Parent Directory: {file_info.parent_directory}')

            # Если текущий элемент - каталог, рекурсивно обрабатываем его
            if is_directory:
                process_directory(item_path)

    except Exception as e:
        logging.error(f'Error processing directory {path}: {str(e)}')


if __name__ == '__main__':
    import sys

    # Проверка, что передан аргумент командной строки (путь к директории)
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory_path>")
        sys.exit(1)

    directory_path = sys.argv[1]

    # Проверка, что указанный путь существует и является директорией
    if not os.path.exists(directory_path) or not os.path.isdir(directory_path):
        print(f"Invalid directory path: {directory_path}")
        sys.exit(1)

    # Запуск обработки директории
    process_directory(directory_path)
