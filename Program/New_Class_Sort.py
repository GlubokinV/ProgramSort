from re import findall


class DataSort:
    """Класс работы с введённой пользователем строкой"""

    def isolator(self, user_data):
        """Вычленение букв З,С,К из вводимой строки"""
        self.user_data = user_data
        _template = r"[КЗС]"
        result = findall(_template, str(self.user_data))
        return result

    def coloring_letter(self, isol_data):
        """Присваивание цвета буквам К, З и С"""
        my_dictionary = {'К': '\033[2;31;49m К', 'З': '\033[2;32;49m З', 'С': '\033[2;34;49m С'}
        self.isol_data = isol_data
        my_message = self.isol_data
        my_number = []
        for letter in my_message:
            my_number.append(my_dictionary[letter])
        return my_number

    def letters_to_numbers(self, color_string):
        """Перевод букв в цифры"""
        _my_dictionary = {'К': 3, 'З': 1, 'С': 2}
        self.color_string = color_string
        _my_message = color_string
        _my_numbers = []
        for letter in _my_message:
            _my_numbers.append(_my_dictionary[letter])
        return _my_numbers

    def sorter(self, num_list):
        """Сортировка полученных цифр"""
        self.num_list = num_list
        count = 0
        mas = num_list
        n = len(mas)
        for run in range(n - 1):
            for i in range(n - 1):
                if mas[i] > mas[i + 1]:
                    count += 1
                    mas[i], mas[i + 1] = mas[i + 1], mas[i]
        return mas

    def numbers_to_letters(self, sorted_numbers):
        """Перевод отсортированного массива в цветные буквы"""
        my_dictionary = {3: '\033[2;31;49m К', 1: '\033[2;32;49m З', 2: '\033[2;34;49m С'}
        self.sorted_numbers = sorted_numbers
        _my_message = [*sorted_numbers]
        sorted_text = []
        for number in _my_message:
            sorted_text.append(my_dictionary[number])
        return sorted_text
