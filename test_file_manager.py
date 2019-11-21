from console_file_manager import *
from accounting import account_refill


def test_check_path():
    m_path = 'test_folder'
    assert os.path.exists(m_path) == (1 == check_path(m_path))
    if not os.path.exists(m_path):
        os.makedirs(m_path)
    assert os.path.exists(m_path) == (1 == check_path(m_path))
    if os.path.exists(m_path):
        shutil.rmtree(m_path)


def test_build_menu_item():
    assert f'*{"test":^78}*' == build_menu_item('test')
    assert f'* {"6"}. {"menu_item_name":<74}*' == build_menu_item('menu_item_name', '6')


def test_account_refill():
    assert 150 == account_refill(100, 50)
    assert 50 == account_refill(0, 50)


def test_save_listing():
    m_path = './data/listdir.txt'
    assert os.path.exists(os.path.split(m_path)[0])
    assert os.path.exists(m_path)
    m_folders, m_files = get_folder_objects('.')
    m_folders_str = 'dirs:'
    m_sep = ''
    for item in m_folders:
        m_folders_str += f' {m_sep}{item}'
        if '' == m_sep:
            m_sep = ','
    m_files_str = 'files:'
    m_sep = ''
    for item in m_files:
        m_files_str += f' {m_sep}{item}'
        if '' == m_sep:
            m_sep = ','
    with open(m_path, 'r') as f:
        m_files_f = f.readline().replace('\n', '')
        f.readline()
        m_folders_f = f.readline().replace('\n', '')
    assert m_folders_f == m_folders_str
    assert m_files_f == m_files_str
