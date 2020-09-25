import colorama
import pathlib
from termcolor import cprint


def create_vtt_file(file_path: str):
    """
    Create vtt file (Subtitle file).
    """
    file_path = file_path.strip('"')
    current_extension = pathlib.PurePath(file_path).suffix

    if current_extension == '.srt':
        path_after_converting = file_path.replace(current_extension, '.vtt')
        with open(path_after_converting, 'w', encoding="utf_8_sig") as f:
            f.write(replace_to_vtt(file_path))
            cprint('[✔] The vtt file was created successfully.\n', 'green')
    else:
        cprint('[x] Not an Srt file.\n', 'red')


def replace_to_vtt(file_path: str):
    """
    Original file read & String replacement.
    """

    new_string = 'WEBVTT\n\n'
    with open(file_path, 'r', encoding="utf_8_sig") as f:
        for line in f.readlines():
            new_string += line.replace(',', '.') if ('-->' in line) else line
    return new_string


def main():
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


if __name__ == '__main__':
    colorama.init()
    main()
