import unittest
from Program.InputUserData import DataInput


class TestExample(unittest.TestCase):
    """Тестирование функции подготовки вводимых данных для обработки"""

    def test_example_only_KZS(self):
        """Разбивает строку из КЗС на отдельные символы?"""
        x = DataInput()
        res = x.example('ЗКЗС')
        self.assertEqual(res, ['З', 'К', 'З', 'С'])

    def test_example_spec_char(self):
        """Разбивает строку на отдельные символы, если есть спец. символы?"""
        x = DataInput()
        res = x.example('З!@#')
        self.assertEqual(res, ['З', '!', '@', '#'])

    def test_example_exceptions_not_KZS(self):
        """Появляется исключение, при вводе строки без КЗС?"""
        x = DataInput()
        self.assertRaises(ValueError, x.example, '!@#')

    def test_example_exceptions_empty_line(self):
        """Появляется исключение, при вводе пустой строки?"""
        x = DataInput()
        self.assertRaises(ValueError, x.example, [])

    def test_example_long_line(self):
        """Разбивает длинную строку на отдельные символы?"""
        x = DataInput()
        res = x.example('З!@sd;о;;;;qqqqqqqq')
        self.assertEqual(res, ['З', '!', '@', 's', 'd', ';', 'о', ';', ';', ';', ';', 'q', 'q',
                               'q', 'q', 'q', 'q', 'q', 'q'])


if __name__ == '__main__':
    unittest.main()
