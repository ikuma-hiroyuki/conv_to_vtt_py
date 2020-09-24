import os
import pathlib
from termcolor import cprint
import colorama
colorama.init()


def create_vtt_file(file_path: str):
    """
    Create vtt file (Subtitle file).
    """
    file_path = file_path.strip('"')

    def replace_file():
        """
        Original file read & String replacement.
        """

        new_string = 'WEBVTT\n\n'
        with open(file_path, 'r', encoding="utf_8_sig") as f:
            for line in f.readlines():
                new_string += line.replace(',',
                                           '.') if ('-->' in line) else line
        return new_string

    if os.path.exists(file_path):
        current_extension = pathlib.PurePath(file_path).suffix
        vtt_file_path = file_path.replace(current_extension, '.vtt')

        with open(vtt_file_path, 'w', encoding="utf_8_sig") as f:
            f.write(replace_file())
            cprint('[✔] The vtt file was created successfully.\n', 'green')
    else:
        cprint('[x] File does not exist.\n', 'red')


msg = ('Please enter the path of the target file.\n'
       '(Type "exit" to exit)\n'
       )

path = input(msg)
while True:
    if path.lower().strip('"') != 'exit':
        create_vtt_file(path)
        path = input(msg)
    else:
        break
