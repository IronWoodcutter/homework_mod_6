import os

from pathlib import Path
untouchable_folders = ['archives', 'video', 'audio', 'documents', 'images']
main_folder = r'D:\English\Prince and Pauper'
# функція створення списку файлів
def file_paths(main_folder, list_file_paths=[]):
    for item in os.listdir(main_folder):
        if Path(item).name not in untouchable_folders:  # виключаємо сканування в цілових папках
            path = os.path.join(main_folder, item)
            if not os.path.isdir(path):
                list_file_paths.append(path)
            else:
                file_paths(path)  # рекурсія в подкаталоги
    return list_file_paths

print (file_paths(main_folder))