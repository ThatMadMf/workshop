groups = {
    'KS_1': (125, 'Name1 Name1 Name1'),
    'KS_2': (25, 'Name2 Name2 Name2'),
    'KS_3': (69, 'Name3 Name3 Name3'),
    'KS_4': (420, 'Name4 Name4 Name4'),
    'KS_5': (15, 'Name5 Name5 Name5'),
    'KS_6': (43, 'Name6 Name6 Name6'),
}


def get_group():
    group_name = input('Enter group name\n')
    return group_name, groups.get(group_name, None)


def get_number_of_students():
    group = get_group()
    if group is not None:
        print(group[1][0])
    else:
        print('There is no group with this name')


def get_group_head():
    group = get_group()
    if group is not None:
        print(group[1][1])
    else:
        print('There is no group with this name')


def filter_groups(condition):
    result = [g for g in groups if condition(g)]
    print('Groups that pass condition are:')
    for g in result:
        print(f'{g} {groups.get(g)}')


def get_groups_less_than():
    max_amount = int(input('Enter max acceptable amount of students\n'))
    filter_groups(lambda g: groups.get(g)[0] <= max_amount)


def get_groups_more_than():
    min_amount = int(input('Enter min acceptable amount of students\n'))
    filter_groups(lambda g: groups.get(g)[0] >= min_amount)


def set_new_student_amount():
    group_name, group_value = get_group()

    if group_value is None:
        print('There is no group with this name')
        return

    new_amount = int(input(f'Enter new amount of students of group {group_name}\n'))
    groups.update({group_name: (new_amount, group_value[1])})


def set_new_group_head():
    group_name, group_value = get_group()

    if group_value is None:
        print('There is no group with this name')
        return

    new_head_name = input(f'Enter new head\'s name of group {group_name}\n')
    groups.update({group_name: (group_value[0], new_head_name)})


def add_new_group():
    group_name = input('Enter group name\n')
    student_number = int(input('Enter number of students\n'))
    group_head = input('Enter name of group\'s head\n')

    groups.update({group_name: (student_number, group_head)})


def remove_group():
    group_name, group_value = get_group()

    del groups[group_name]


menu_items = {
    1: 'Get number of students by group name',
    2: 'Get name of group\'s head',
    3: 'Get groups where number of students is more than X',
    4: 'Get groups where number of students is less than X',
    5: 'Change amount of students in a group',
    6: 'Change name of the head of a group',
    7: 'Add new group',
    8: 'Remove group',
    0: 'Exit',
}

menu_actions = {
    1: get_number_of_students,
    2: get_group_head,
    3: get_groups_less_than,
    4: get_groups_more_than,
    5: set_new_student_amount,
    6: set_new_group_head,
    7: add_new_group,
    8: remove_group,
}


def print_main_menu():
    print('')
    print('Current state of the dictionary:')
    for group_name in groups:
        print(f'{group_name} {groups.get(group_name)}')
    print('')

    for key in menu_items:
        print(f'{key} {menu_items.get(key)}')


input_key = 69

while input_key != 0:
    print_main_menu()
    input_key = int(input())
    action = menu_actions.get(input_key, lambda: 'Unknown key')
    action()
