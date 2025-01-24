import os
import time

def main() -> None:
    counter: int = 0
    for root, dirs, files in os.walk('./'):
        for file in files:
            filepath: str = os.path.join(root, file)
            parent_dir = os.path.dirname(filepath)
            filetime: float = os.path.getmtime(filepath)
            formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
            filesize = os.path.getsize(filepath)
            counter += 1
            print(f'{counter}\tОбнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
            

if __name__ == "__main__":
    main()
