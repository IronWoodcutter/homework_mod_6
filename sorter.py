
'''
import os

path = r'D:\Python'



def get_folder_tree(path):
    print(os.listdir(path))
    for item in os.listdir(path):
        if os.path.isdir(path + '\\' + item):
            get_folder_tree(path + '\\' + item)
            print(item, type(item), path + '\\' + item)



get_folder_tree(path)

'''


# вывод перечня файлов в дереве каталогов с помощью рекурсии
import sys, os
def mylister(currdir):
    print('[' + currdir + ']')
    for file in os.listdir(currdir): # здесь получение списка файлов
        path = os.path.join(currdir, file) # добавить путь к каталогу
        if not os.path.isdir(path):
            print(path)
        else:
            mylister(path) # рекурсия в подкаталоги

if __name__ == '__main__':
    mylister(r"D:\Python") # имя каталога в командной строке


'''
TRANS = {}


def creating_dictionary():
    CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
    TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
                   "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

    global TRANS
    TRANS = {}

    for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
        TRANS[ord(c)] = l
        TRANS[ord(c.upper())] = l.upper()
    return TRANS


creating_dictionary()


def translate(name):
    return name.translate(TRANS)


creating_dictionary()
print(translate("фв_ ЧпкейЖ4З5ж"))


def normalize(path):
    pass
'''
def get_folder_tree():
    pass

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
