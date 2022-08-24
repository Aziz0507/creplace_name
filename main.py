import os
from datetime import datetime


BASEDIR = r'Z:\лайфхаки от русакова\lesson_1\test'

def rename_files(rename):
    for root, dirs, files in os.walk(rename):
        for names in files:
            root_and_files(root, names)


def root_and_files(root, names):
    asdasd   = print('замена из ' + names)
    new_name_input = input('Введите свое новое название: ')
    new_name = new_name_input + str(datetime.now().date()) +'.jpg'
    old_name = os.path.join(root, names)
    new_name = os.path.join(root, new_name)
    os.rename(old_name, new_name)
    



def rename_file(names):
    names = names.replace('Без названия (1)', 'img')

    return names


rename_files(BASEDIR)
