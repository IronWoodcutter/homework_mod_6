
'''
# вывод перечня файлов в дереве каталогов с помощью рекурсии
import os
import re

def create_dict():

    CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
    TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
                   "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")
    
    TRANS = {}
    
    for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
        TRANS[ord(c)] = l
        TRANS[ord(c.upper())] = l.upper()
    return TRANS
    
TRANS = create_dict()
    
def normalize(name):
    name = name.translate(TRANS)
    name = re.sub(r'[\W]','_', name)


    return name

def mylister(path):
    
    print('[' + path + ']')
    # здесь получение списка файлов
    for file in os.listdir(path):
        # добавить путь к каталогу
        path = os.path.join(path, file)
        
        if not os.path.isdir(path):
            print(file)
            if file == r'.+\..+': 
                file_name = file.rsplit('.', 1)[0]
                file_extension = file.rsplit('.', 1)[1]
                print(file_name)
                new_file_name = f'{normalize(file_name)}.{file_extension}'
                print(new_file_name)
                os.rename(path, new_file_name)
                
                print(file_name)
                print(file_extension)
                print(path)

        else:
            normalize(file)
            print('Подкаталог: ', file)
            mylister(path)  # рекурсия в подкаталоги

if __name__ == '__main__':
    # имя каталога в командной строке
    mylister(r'E:\shop')
'''
'''
import os

main_path = r'd:\down'

# key names will be folder names!
extensions = {

    'images': ['jpeg', 'png', 'jpg','svg'],
    'video': ['mp4', 'mov', 'avi', 'mkv'],
    'documents': ['doc', 'docx', 'txt', 'pdf', 'xlsx', 'pptx'],
    'audio': ['mp3', 'ogg', 'wav', 'amr'],
    'archives': ['zip', 'gz', 'tar']

}


# also creates folders from dictionary keys
def create_folders_from_list(folder_path, folder_names):
    for folder in folder_names:
        if not os.path.exists(f'{folder_path}\\{folder}'):
            os.mkdir(f'{folder_path}\\{folder}')


def get_subfolder_paths(folder_path) -> list:
    subfolder_paths = [f.path for f in os.scandir(folder_path) if f.is_dir()]

    return subfolder_paths


def get_file_paths(folder_path) -> list:
    file_paths = [f.path for f in os.scandir(folder_path) if not f.is_dir()]

    return file_paths


def sort_files(folder_path):
    file_paths = get_file_paths(folder_path)
    ext_list = list(extensions.items())

    for file_path in file_paths:
        extension = file_path.split('.')[-1]
        file_name = file_path.split('\\')[-1]

        for dict_key_int in range(len(ext_list)):
            if extension in ext_list[dict_key_int][1]:
                print(f'Moving {file_name} in {ext_list[dict_key_int][0]} folder\n')
                os.rename(file_path, f'{main_path}\\{ext_list[dict_key_int][0]}\\{file_name}')


def remove_empty_folders(folder_path):
    subfolder_paths = get_subfolder_paths(folder_path)

    for p in subfolder_paths:
        if not os.listdir(p):
            print('Deleting empty folder:', p.split('\\')[-1], '\n')
            os.rmdir(p)


if __name__ == "__main__":
    create_folders_from_list(main_path, extensions)
    sort_files(main_path)
    remove_empty_folders(main_path)
'''
'''
import os
import re

list_folders_path = []
list_files_path = []


def create_dict():

    CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
    TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
                   "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

    TRANS = {}

    for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
        TRANS[ord(c)] = l
        TRANS[ord(c.upper())] = l.upper()
    return TRANS


TRANS = create_dict()


def normalize(name):
    name = name.translate(TRANS)
    name = re.sub(r'[\W]', '_', name)

    return name


def mylister(main_path):
    print('текущая директория: ', '[' + main_path + ']')
    # здесь получение списка файлов
    for file in os.listdir(main_path):
        # добавить путь к каталогу
        path = os.path.join(main_path, file)

        if not os.path.isdir(path):
            print(file)
            if re.search(r'.+\..+', file):
                file_name = file.rsplit('.', 1)[0]
                file_extension = file.rsplit('.', 1)[1]
                normalize_file_name = normalize(file_name)
                if file_name != normalize_file_name:
                    os.rename(path, f'{main_path}\\{normalize_file_name}.{file_extension}')

                print('имя файла: ', file_name)
                print('расширение файла: ', file_extension)
            else:

                print(
                    'Файл не соответствует структуре *.*: ', file)

        else:
            normalize_file = normalize(file)
            if file != normalize_file:
                os.rename(path, f'{main_path}\\{normalize_file}')
                
            mylister(path)  # рекурсия в подкаталоги


if __name__ == '__main__':
    mylister(r"E:\shop")
    print('Список папок: ', list_folders_path)
    print("Список файлов: ", list_files_path)
'''

import os
import re



def create_dict():

    CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
    TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
                   "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

    TRANS = {}

    for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
        TRANS[ord(c)] = l
        TRANS[ord(c.upper())] = l.upper()
    return TRANS


TRANS = create_dict()


def normalize(name):
    name = name.translate(TRANS)
    name = re.sub(r'[\W]', '_', name)

    return name

list_path = {}
def mylister(main_path):
    list_files_path = []
    print('текущая директория: ', '[' + main_path + ']')
    # здесь получение списка файлов
    for file in os.listdir(main_path):
        # добавить путь к каталогу
        path = os.path.join(main_path, file)
        list_files_path.append()
        if not os.path.isdir(path):
            list_files_path.append()
        else:    
            mylister(path)  # рекурсия в подкаталоги
    list_path.update(main_path = list_files_path)    

def normalize_files(list_files_path):
    for file_path in list_files_path:
        full_file_name = file_path.split('\\')[-1]
        file_name = full_file_name.rsplit('.', 1)[0]
        file_extension = full_file_name.rsplit('.', 1)[1]
        normalize_file_name = normalize(file_name)
        if file_name != normalize_file_name:
            os.rename(file_path, f'')

if __name__ == '__main__':
    mylister(r"E:\shop")
    print('Список папок: ', list_folders_path)
    print("Список файлов: ", list_files_path)
    print('Словарь значений: ', list_path)
