import os
import sys
import platform
import shutil
from celebrities import do_play
from accounting import do_accounting, user_input


def build_menu_item(p_name, p_key=None):
    if p_key is None:
        return f'*{p_name:^78}*'
    else:
        return f'* {p_key}. {p_name:<74}*'


def check_path(p_path):
    """
    Проверяет корректность предоставленного пути до директории
    :param p_path: - путь до директории для проверки
    :return: возвращает целое со знаком:
        1 - путь уже существует
        0 - путь не существует
        -1 - плохая строка адреса
    """
    m_rez = 0
    if p_path is not None and len(p_path) > 0:
        if os.path.exists(p_path):
            m_rez = 1
    else:
        m_rez = -1
    return m_rez


def default_func():
    # функция-заглушка на время разработки требуемого функционала.
    print('Выбранный функционал находится в разработке.\n')


def make_folder():
    m_path = user_input(str, 'Укажите наименование новой директории')
    m_mode = check_path(m_path)
    if -1 == m_mode:
        print('  -!-> Введённый путь не является корректным. Команда не выполнена.')
    elif 1 == m_mode:
        print('  -!-> Директория уже существует. Команда не выполнена.')
    elif 0 == m_mode:
        os.makedirs(m_path)
        print('  Директория успешно создана.\n')


def remove_object():
    m_path = user_input(str, 'Укажите путь к объекту, который хотите удалить')
    m_mode = check_path(m_path)
    if -1 == m_mode:
        print('  -!-> Введённый путь не является корректным. Команда не выполнена.')
    elif 1 == m_mode:
        if os.path.isdir(m_path):
            shutil.rmtree(m_path)
            print('  Директория удалена.')
        elif os.path.isfile(m_path):
            os.remove(m_path)
            print('  Файл удален.')
    elif 0 == m_mode:
        print('  -!-> Объект не существует. Команда не выполнена.')


def copy_object():
    m_src = user_input(str, 'Укажите путь к объекту, который хотите скопировать')
    m_src_mode = check_path(m_src)
    if -1 == m_src_mode:
        print('  -!-> Некорректный путь к источнику. Команда не выполнена.')
    elif 1 == m_src_mode:
        m_dst = user_input(str, 'Укажите путь, куда хотите скопировать')
        m_dst_mode = check_path(m_dst)
        if -1 == m_dst_mode:
            print('  -!-> Некорректный путь для результата. Команда не выполнена.')
        elif 1 == m_dst_mode:
            if os.path.isfile(m_src) and os.path.isdir(m_dst):
                m_dst = os.path.join(os.path.normpath(m_dst), os.path.split(m_src)[1])
                if os.path.exists(m_dst):
                    print(f'    -!-> Файл "{m_dst}" уже существует. Команда не выполнена.')
                else:
                    shutil.copy2(m_src, m_dst)
                    print('  Данные скопированы')
            else:
                print('  -!-> Копирование невозможно. Команда не выполнена.')
        elif 0 == m_dst_mode:
            if os.path.isfile(m_src):
                if len(os.path.split(m_dst)[1]) == 0:
                    m_dst = os.path.join(os.path.normpath(m_dst), os.path.split(m_src)[1])
                m_paths = os.path.split(m_dst)
                if len(m_paths[0]) > 0 and not os.path.exists(m_paths[0]):
                    os.makedirs(m_paths[0])
                shutil.copy2(m_src, m_dst)
            elif os.path.isdir(m_src):
                shutil.copytree(m_src, m_dst)
            print('  Данные скопированы')
    elif 0 == m_src_mode:
        print('  -!-> Источник не существует. Команда не выполнена.')


def show_listing(p_mode=0):
    print(build_menu_item('*' * 78))
    m_info = "директорий" if 1 == p_mode else "файлов" if 2 == p_mode else "всех объектов"
    print(build_menu_item(f'Список {m_info} для'))
    print(build_menu_item(os.getcwd()))
    print(build_menu_item('-' * 78))
    m_folders = [z for z in os.listdir('.') if 2 != p_mode and os.path.isdir(f'./{z}')]
    m_folders.sort()
    m_files = [z for z in os.listdir('.') if 1 != p_mode and os.path.isfile(f'./{z}')]
    m_files.sort()
    if 2 != p_mode:
        for x in m_folders:
            print(build_menu_item(f"  {f'< {x} >':<76}"))
    if 1 != p_mode:
        for x in m_files:
            print(build_menu_item(f'  {x:<76}'))
    print(build_menu_item('*' * 78))
    print('\n')


def show_author():
    print(build_menu_item('*' * 78))
    print(build_menu_item('Информация об авторе'))
    print(build_menu_item('-' * 78))
    print(build_menu_item('Качка Алексей'))
    print(build_menu_item('*' * 78))
    print('\n')


def show_sys_info():
    print(build_menu_item('*' * 78))
    print(build_menu_item('Информация об операционной системе'))
    print(build_menu_item('-' * 78))
    my_os = platform.uname()
    print(build_menu_item(f'Платформа: {sys.platform}, имя: {os.name}, система: {my_os.system}.{my_os.release}, версия: {my_os.version}'))
    print(build_menu_item('*' * 78))
    print('\n')


def show_current_dir():
    print(build_menu_item('*' * 78))
    print(build_menu_item('Текущая рабочая директория'))
    print(build_menu_item('-' * 78))
    m_cur_path = os.getcwd()
    print(build_menu_item(f'{m_cur_path}'))
    print(build_menu_item('*' * 78))
    print('\n')


def change_work_dir():
    my_new_path = user_input(str, 'Укажите путь к новой рабочей директории')
    path_mode = check_path(my_new_path)
    if 1 == path_mode:
        os.chdir(my_new_path)
        print('  Директория успешно изменена.')
        show_current_dir()
    elif 0 == path_mode:
        print('  -!-> Введённый путь не существует. Команда не выполнена.')
    else:
        print('  -!-> Введённый путь не является корректным. Команда не выполнена.')


def do_file_mgr():
    m_options = {
        '1': {'func': make_folder, 'args': None},
        '2': {'func': remove_object, 'args': None},
        '3': {'func': copy_object, 'args': None},
        '4': {'func': show_listing, 'args': None},
        '5': {'func': show_listing, 'args': 1},
        '6': {'func': show_listing, 'args': 2},
        '7': {'func': show_sys_info, 'args': None},
        '8': {'func': show_author, 'args': None},
        '9': {'func': change_work_dir, 'args': None},
        '0': {'func': show_current_dir, 'args': None},
        'b': {'func': do_accounting, 'args': None},
        'v': {'func': do_play, 'args': None}
    }
    while True:
        print(build_menu_item('*' * 78))
        print(build_menu_item('Консольный файловый менеджер'))
        print(build_menu_item('*' * 78))
        print(build_menu_item('создать директорию', '1'))
        print(build_menu_item('удалить объект', '2'))
        print(build_menu_item('копировать объект', '3'))
        print(build_menu_item('содержимое рабочей директории - все объекты', '4'))
        print(build_menu_item('содержимое рабочей директории - только поддиректории', '5'))
        print(build_menu_item('содержимое рабочей директории - только файлы', '6'))
        print(build_menu_item('информация об операционной системе', '7'))
        print(build_menu_item('информация об авторе', '8'))
        print(build_menu_item('сменить рабочую директорию ', '9'))
        print(build_menu_item('показать рабочую директорию ', '0'))
        print(build_menu_item('выход', 'q'))
        print(build_menu_item('викторина "День рождения знаменитости"', 'v'))
        print(build_menu_item('личный счёт', 'b'))
        print(build_menu_item('*' * 78))
        choice = input('Ваш выбор: ')
        if choice in m_options.keys():
            # из-за того, что функции из модулей викторины и счёта сделаны без параметров,
            # пришлось тут извращаться и "растить ветки" на пустом, вобщем-то, месте...
            if m_options[choice]['args'] is None:
                m_options[choice]['func']()
            else:
                m_options[choice]['func'](m_options[choice]['args'])
        elif choice == 'q':
            break
        else:
            print('  -> Неверный пункт меню, попробуйте ещё раз...')


if '__main__' == __name__:
    do_file_mgr()
