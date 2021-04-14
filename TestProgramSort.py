import unittest
from New_Class_Sort import DataSort
from InputUserData import DataInput
DataInput = DataInput()
DataSort = DataSort()


class TestProgramSort(unittest.TestCase):
    """Тестирование полного цикла работы программы"""
    def test_correctInput(self):
        """Программа отсортирует и покрасит буквы КЗС в соответствии З(зелёный)<С(синий)<К(красный)?"""
        input_text = DataInput.example('КЗС')
        isolated_text = DataSort.isolator(input_text)
        numbered_letter = DataSort.letters_to_numbers(isolated_text)
        sorted_number = DataSort.sorter(*[numbered_letter])
        res = DataSort.numbers_to_letters(sorted_number)
        self.assertEqual(res, ['\x1b[2;32;49m З', '\x1b[2;34;49m С', '\x1b[2;31;49m К'])


if __name__ == '__main__':
    unittest.main()
