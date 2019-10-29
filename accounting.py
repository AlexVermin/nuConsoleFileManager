from datetime import datetime


def user_input(p_type, p_prompt='Введите значение'):
    m_value = None
    if p_type not in (str, int, float):
        print(f'  -> Тип "{p_type}" не допускается.')
        return None
    while True:
        if m_value is not None:
            if int == p_type:
                if m_value.isdigit():
                    return int(m_value)
                else:
                    print('  -> Не является целым числом, попробуйте ещё раз...')
            elif float == p_type:
                try:
                    x = float(m_value)
                    return x
                except ValueError:
                    print('  -> Не является вещественным числом, попробуйте ещё раз...')
            else:
                return m_value
        m_value = input(f'  {p_prompt}: ')


def account_refill(p_obj):
    print('=' * 40)
    print('=    Кошелёк - Пополнение счёта', ' ' * 6, '=')
    print('=' * 40)
    income = user_input(float, 'Сумма пополнения')
    if income is not None:
        if 'value' in p_obj:
            p_obj['value'] += income
        else:
            p_obj['value'] = income


def do_buy(p_obj):
    print('=' * 40)
    print('=    Кошелёк - Добавление покупки', '     =')
    print('=' * 40)
    obj_cost = user_input(float, 'Укажите сумму покупки')
    if 'value' not in p_obj:
        p_obj['value'] = 0
    if p_obj['value'] >= obj_cost:
        obj_name = user_input(str, 'Укажите наименование покупки')
        p_obj['value'] -= obj_cost
        p_obj['history'][datetime.strftime(datetime.today(), '%Y%m%d%H%M%S')] = {
            'cost': obj_cost,
            'name': obj_name
        }
    else:
        print(' -> Недостаточно средств на счёте, покупка не состоялась.')


def show_history(p_obj):
    print('=' * 40)
    print('=    Кошелёк - История покупок', ' ' * 7, '=')
    print(f'={"-" * 38}=')
    if 'history' not in p_obj or len(p_obj['history']) < 1:
        print(f'={"Список покупок пуст":^38}=')
    else:
        need_splitter = False
        for idx in sorted(p_obj['history'].keys()):
            if need_splitter:
                print(f'={"-" * 38}=')
            else:
                need_splitter = True
            print(f'= {idx[6:8]}.{idx[4:6]}.{idx[:4]} | {p_obj["history"][idx]["name"]:>23} =')
            print(f'=   {idx[8:10]}:{idx[10:12]}:{idx[12:]} | {p_obj["history"][idx]["cost"]:>23.2f} =')
    print(f'={"-" * 38}=')
    print(f'= Остаток средств: {p_obj["value"]:>19.2f} =')
    print('=' * 40, '\n')


def do_accounting():
    # инициализируем "кошелёк"
    my_wallet = {
        'value': 0.0,
        'history': {}
    }
    # а теперь будем над ним глумиться:
    while True:
        print('=' * 40)
        print('=    Кошелёк', ' ' * 25, '=')
        print('=' * 40)
        print('= 1. пополнение счёта', ' ' * 16, '=')
        print('= 2. покупка', ' ' * 25, '=')
        print('= 3. история покупок', ' ' * 17, '=')
        print('= 4. выход', ' ' * 27, '=')
        print('=' * 40)

        choice = input('Ваш выбор: ')
        if choice == '1':
            account_refill(my_wallet)
        elif choice == '2':
            do_buy(my_wallet)
        elif choice == '3':
            show_history(my_wallet)
        elif choice == '4':
            break
        else:
            print('  -> Неверный пункт меню, попробуйте ещё раз...')


if '__main__' == __name__:
    do_accounting()