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
