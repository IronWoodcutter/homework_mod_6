
import os
import re
import shutil
import pathlib
my_folder_path = r'D:\English\Prince and Pauper'

# словник згідно якому будемо сортувати файли (ключі-папки, значення - розширення файлів)
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
    

# функція нормалізацшї імен файлів та папок   
def normalize(name):

    name = name.translate(create_dict())
    name = re.sub(r'[^_0-9A-Za-z]','_', name)

    return name

# отримаємо список файлів
def file_paths(my_folder_path, file_paths_=[]):
    
    for item in os.listdir(my_folder_path):
        path = os.path.join(my_folder_path, item)      
        if not os.path.isdir(path):
            file_paths_.append(path)
        else:   
            file_paths(path)  # рекурсія в подкаталоги
    return file_paths_
# отримаємо список папок
def folder_paths(my_folder_path, folder_paths_=[]):
    
    for item in os.listdir(my_folder_path):
        path = os.path.join(my_folder_path, item)      
        if  os.path.isdir(path):
            os.rename(path, f'{os.path.dirname(path)}\\{normalize(os.path.basename(path))}') 
            folder_paths_.append(path)
            folder_paths(path)
        else:   
           continue
    return folder_paths_
'''
def normalize_item(my_folder_path):
    list_files = file_paths(my_folder_path)
    list_folders = folder_paths(my_folder_path) 
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
'''
# функція створенн необхідних папок
def create_folder(my_folder_path, folder_names):
    for folder in folder_names:
        if not os.path.exists(f'{my_folder_path}\\{folder}'):
            os.mkdir(f'{my_folder_path}\\{folder}')


# функція виявлення дублів файлів:
def duplication_check(dist_folder, full_file_name):
    path = f'{dist_folder}\\{full_file_name}'
    print(full_file_name)
    print(path)
    while True:  
        path = f'{dist_folder}\\{full_file_name}'
        if os.path.exists(path) == False:
            n = 1
            full_file_name = f"{full_file_name.rsplit('.')[0]}{n}.{full_file_name.rsplit('.')[1]}"
            n += 1
        else:
            break
    return full_file_name

    # функція обробки файлів 'images': ['jpeg', 'png', 'jpg','svg']

def move_images(file_path,  file_name, extension):
    os.rename(file_path, f'{my_folder_path}\\images\\{normalize(file_name)}.{extension}')

# функція обробки файлів 'video': ['mp4', 'mov', 'avi', 'mkv']

def move_video(file_path,  file_name, extension):
    os.rename(file_path, f'{my_folder_path}\\video\\{normalize(file_name)}.{extension}')

# функція обробки файлів 'documents': ['doc', 'docx', 'txt', 'pdf', 'xlsx', 'pptx']

def move_documents(file_path,  file_name, extension):
    os.rename(file_path, f'{my_folder_path}\\documents\\{normalize(file_name)}.{extension}')

# функція обробки файлів 'audio': ['mp3', 'ogg', 'wav', 'amr']

def move_audio(file_path,  file_name, extension):
    os.rename(file_path, f'{my_folder_path}\\audio\\{normalize(file_name)}.{extension}')
    
# функція обробки файлів 'archives': ['zip', 'gz', 'tar']

def move_archives(file_path, file_name):
    archive_path = f'{my_folder_path}\\archives\\{normalize(file_name)}'
    if os.path.exists(archive_path) == False:
        os.mkdir(f'{my_folder_path}\\archives\\{normalize(file_name)}')
        shutil.unpack_archive(file_path, archive_path)
        os.remove(file_path)

# функція сортування файлів

def sort_files(my_folder_path):
    list_files = file_paths(my_folder_path)
    for file_path in list_files:
       
        full_file_name = os.path.basename(file_path)
        file_name = full_file_name.rsplit('.', 1)[0]
        extension = file_path.split('.')[-1]
        if extension in ['jpeg', 'png', 'jpg','svg']:
            dist_folder = f'{my_folder_path}\\images\\'
            duplication_check(dist_folder, full_file_name) 
            move_images(file_path,  file_name, extension)
        elif extension in ['mp4', 'mov', 'avi', 'mkv']:
            dist_folder = f'{my_folder_path}\\video\\'
            duplication_check(dist_folder, full_file_name)
            print(duplication_check(dist_folder, full_file_name))
            move_video(file_path,  file_name, extension)
        elif extension in ['doc', 'docx', 'txt', 'pdf', 'xlsx', 'pptx']:
            dist_folder = f'{my_folder_path}\\documents\\'
            duplication_check(dist_folder, full_file_name)
            move_documents(file_path,  file_name, extension)
        elif extension in ['mp3', 'ogg', 'wav', 'amr']:
            dist_folder = f'{my_folder_path}\\audio\\'
            duplication_check(dist_folder, full_file_name)
            move_audio(file_path,  file_name, extension)
        elif extension in ['zip', 'gz', 'tar']:
            dist_folder = f'{my_folder_path}\\archives\\'
            duplication_check(dist_folder, full_file_name)
            move_archives(file_path, file_name)

# функція видалення пустих папок
def remove_empty_folders(folder_path):

    folder_path = folder_paths(my_folder_path)
    for folder in folder_path:
        if not os.listdir(folder):
            os.rmdir(folder)


def main():
    folder_paths(my_folder_path)
    #my_folder_path = input('Введіть шлях до папки яку будемо сортувати: ')
    #normalize_item(my_folder_path)
    create_folder(my_folder_path, extensions)    
    sort_files(my_folder_path)
    remove_empty_folders(my_folder_path)

if __name__ == '__main__':
    main()
