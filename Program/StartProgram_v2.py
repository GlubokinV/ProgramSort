from Program.New_Sorter import DataInput


def start():
    """Функция старта программы сортировки"""
    x = DataInput()
    string = input("Введите строку, содержащую З, С и К:")
    condition = input("Введите порядок сортировки в виде ЗСК:")
    print(*x.sort_condition(x.char_count(string), condition))


if __name__ == '__main__':
    start()
