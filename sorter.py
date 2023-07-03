import os
import re
main_path = r'D:\English\Prince and Pauper'
# створюємо список файлів
def file_paths(main_path):
    file_paths = [os.path.join(main_path, file) for file in os.listdir(main_path) if not file.isdir()]
    return file_paths

# створюємо список папок
def folder_paths(main_path):
    folder_path = [folder_paths(os.path.join(main_path, folder) for folder in os.listdir(main_path) if  folder.isdir())]


print(file_paths(main_path))

'''
import os
import re
my_folder_path = r'D:\English\Prince and Pauper'
list_folders = []
list_files = []

# словник по якому будемо сортувати файли (ключі-папки, значення - розширення файлів)
extensions = {

    'images': ['jpeg', 'png', 'jpg','svg'],
    'video': ['mp4', 'mov', 'avi', 'mkv'],
    'documents': ['doc', 'docx', 'txt', 'pdf', 'xlsx', 'pptx'],
    'audio': ['mp3', 'ogg', 'wav', 'amr'],
    'archives': ['zip', 'gz', 'tar']
}

# створюємо словник для транслітерації строкових даних
def create_dict() -> dict:

    CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
    TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
                   "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")
    
    TRANS = {}
    
    for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
        TRANS[ord(c)] = l
        TRANS[ord(c.upper())] = l.upper()
    return TRANS
    
TRANS = create_dict()

# функція нормалізацшї імен файлів та папок   
def normalize(name):

    name = name.translate(TRANS)
    name = re.sub(r'[^_0-9A-Za-z]','_', name)

    return name

# отримаємо список файлів та папок
def my_list(my_folder_path):
    
    for item in os.listdir(my_folder_path):
        path = os.path.join(my_folder_path, item)
        
        if not os.path.isdir(path):
            list_files.append(path)
        else:
            list_folders.append(path)
            my_list(path)  # рекурсія в подкаталоги
    return list_folders, list_files


def normalize_item(list_files, list_folders):
    for file in list_files:
        full_file_name = os.path.basename(file)
        file_name = full_file_name.rsplit('.', 1)[0]
        file_extension = full_file_name.rsplit('.', 1)[1]
        normalize_file_name = normalize(file_name)
        if file_name != normalize_file_name:
            os.rename(file, f'{os.path.dirname(file)}\\{normalize_file_name}.{file_extension}')
    for folder in list_folders:
        folder_name = os.path.basename(folder)
        normalize_folder_name = normalize(folder_name)
        if folder_name != normalize_folder_name:
            os.rename(folder, f'{os.path.dirname(folder)}\\{normalize_folder_name}')
# функція створенн необхідних папок
def create_folder(my_folder_path, folder_names):
    for folder in folder_names:
        if not os.path.exists(f'{my_folder_path}\\{folder}'):
            os.mkdir(f'{my_folder_path}\\{folder}')

# функція сортування файлів

def sort_files(my_folder_path):
    extensions_list = list(extensions.items())
    for file_path in list_files:
        extension = file_path.split('.')[-1]
        file_name = os.path.basename(file_path)
        for folder in range(len(extensions_list)):
            if extension in extensions_list[folder][1]:
                os.rename(file_path, f'{my_folder_path}\\{extensions_list[folder][0]}\\{file_name}')



if __name__ == '__main__':
    # имя каталога в командной строке
    my_list(my_folder_path)
    normalize_item(list_files, list_folders)
    my_list(my_folder_path) # оновлюємо списки після нормалізациї
    create_folder(my_folder_path, extensions)
    print(list(extensions.items()))
'''