from re import findall



class DataInput:
    def char_count(self, input_data):
        template = r"[КЗС]"
        input_data = findall(template, str(input_data))
        if not findall(template, str(input_data)):
            raise ValueError('Введена пустая строка или введённые данные не содержат элементов для сортировки!')
        s, k, z = 0, 0, 0
        for i in input_data:
            if i == 'С':
                s += 1
            if i == 'З':
                z += 1
            if i == 'К':
                k += 1
        result_count = [s, k, z]
        return result_count

    def sort_condition(self, calc_char, input_data):
        template = r"[КЗС]"
        if not findall(template, str(input_data)):
            raise ValueError('Неверный формат сортировки!')
        condition = findall(template, str(input_data))
        word_list = []
        list_z = ""
        list_k = ""
        list_s = ""
        unique = []
        [unique.append(item) for item in condition if item not in unique]
        n = 0
        while n != len(unique):
            if unique[n] == 'З':
                list_z += ("\033[2;32;49m З" * calc_char[2])
                word_list.append(list_z)
                n += 1
            else:
                if unique[n] == 'К':
                    list_k += ("\033[2;31;49m К" * calc_char[1])
                    word_list.append(list_k)
                    n += 1
                else:
                    if unique[n] == 'С':
                        list_s += ("\033[2;34;49m С" * calc_char[0])
                        word_list.append(list_s)
                        n += 1
        print('Порядок сортировки:', '<'.join(unique))
        return word_list
