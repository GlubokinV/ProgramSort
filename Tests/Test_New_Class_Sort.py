import unittest
from Program.New_Class_Sort import DataSort


class TestIsolator(unittest.TestCase):
    """Тестирование функции, вычленяющей из вводимой строки буквы З, С, и К"""

    def test_isolator_cut_excess(self):
        """Функция вычленяет только необходимые символы из вводимой строки?"""
        x = DataSort()
        res = x.isolator(['З', 'К', 'З', 'С', 'r'])
        self.assertEqual(res, ['З', 'К', 'З', 'С'])

    def test_isolator_long_line(self):
        """Функция вычленяет только необходимые символы из длинной вводимой строки?"""
        x = DataSort()
        res = x.isolator(['З', 'К', 'ЗДРАВСТВУЙТЕ', 'С', 'r', 'З', 'hello', 'r', '1', '555', 'r'])
        self.assertEqual(res, ['З', 'К', 'З', 'С', 'С', 'З'])

    def test_isolator_cut(self):
        """Функция вычленяет только необходимые символы из вводимой строки со спецсимволами?"""
        x = DataSort()
        res = x.isolator(['ЗК;%:?*(фывожщш203845102=9С84\124щшЗ'])
        self.assertEqual(res, ['З', 'К', 'С', 'З'])


class TestColoring(unittest.TestCase):
    """Тестирование функции покраски букв К, З, С"""

    def test_coloring_letter(self):
        """Функция производит присваивание цвета символам К, З и С?"""
        x = DataSort()
        res = x.coloring_letter(['К', 'З', 'С'])
        self.assertEqual(res, ['\x1b[2;31;49m К', '\x1b[2;32;49m З', '\x1b[2;34;49m С'])

    def test_coloring_letter_long_line(self):
        """Функция производит присваивание цвета любому количеству символов К, З и С?"""
        x = DataSort()
        res = x.coloring_letter(['К', 'З', 'С', 'К', 'З', 'С'])
        self.assertEqual(res, ['\x1b[2;31;49m К', '\x1b[2;32;49m З', '\x1b[2;34;49m С', '\x1b[2;31;49m К',
                               '\x1b[2;32;49m З', '\x1b[2;34;49m С'])

    def test_coloring_letter_one_symbol(self):
        """Функция производит присваивание цвета любому количеству символов К, З и С?"""
        x = DataSort()
        res = x.coloring_letter(['К'])
        self.assertEqual(res, ['\x1b[2;31;49m К'])


class TestLettersToNumbers(unittest.TestCase):
    """Тестирование функции покраски букв К, З, С"""

    def test_letters_to_numbers(self):
        """Функция производит конвертацию букв в цифры соответственно заданному правилу?"""
        x = DataSort()
        res = x.letters_to_numbers(['З', 'К', 'С'])
        self.assertEqual(res, [1, 3, 2])

    def test_letters_to_numbers_long_line(self):
        """Функция производит конвертацию букв в цифры соответственно заданному правилу?"""
        x = DataSort()
        res_2 = x.letters_to_numbers(['З', 'К', 'С', 'З', 'К', 'С', 'З', 'К', 'С'])
        self.assertEqual(res_2, [1, 3, 2, 1, 3, 2, 1, 3, 2])


class TestSortNumbers(unittest.TestCase):
    """Тестирование функции покраски букв К, З, С"""

    def test_sorter(self):
        """Функция производит сортировку полученных цифр по возрастанию?"""
        x = DataSort()
        res_1 = x.sorter([1, 3, 2])
        self.assertEqual(res_1, [1, 2, 3])

    def test_sorter_negative_number(self):
        """Функция производит сортировку полученных цифр с отрицательными значениями?"""
        x = DataSort()
        res_2 = x.sorter([1, -3, -222, 333, 55555, 3, 0, 3, 2, 3, 2])
        self.assertEqual(res_2, [-222, -3, 0, 1, 2, 2, 3, 3, 3, 333, 55555])

    def test_sorter_same_numbers(self):
        """Функция производит сортировку полученных одинаковых цифр?"""
        x = DataSort()
        res_2 = x.sorter([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
        self.assertEqual(res_2, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])

    def test_sorter_one_number(self):
        """Функция производит сортировку одной цифры?"""
        x = DataSort()
        res_2 = x.sorter([1])
        self.assertEqual(res_2, [1])


class TestNumbersToLetters(unittest.TestCase):
    """Тестирование функции конвертации букв в цифры и раскрашивает их
     3=К(красный), 1=З(зелёный), 2=(синий)"""

    def test_numbers_to_letters(self):
        """Функция конвертирует цифры в буквы?"""
        x = DataSort()

        res_1 = x.numbers_to_letters([1, 2, 3])
        self.assertEqual(res_1, ['\x1b[2;32;49m З', '\x1b[2;34;49m С', '\x1b[2;31;49m К'])

    def test_same_numbers_to_same_letters(self):
        """Функция конвертирует последовательность одинаковых цифр в буквы?"""
        x = DataSort()
        res_2 = x.numbers_to_letters([2, 2, 2, 2, 2, 2, 2, 2, 2])
        self.assertEqual(res_2, ['\x1b[2;34;49m С', '\x1b[2;34;49m С', '\x1b[2;34;49m С', '\x1b[2;34;49m С',
                                 '\x1b[2;34;49m С', '\x1b[2;34;49m С', '\x1b[2;34;49m С', '\x1b[2;34;49m С',
                                 '\x1b[2;34;49m С'])


if __name__ == '__main__':
    unittest.main()
