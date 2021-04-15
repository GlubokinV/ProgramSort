from re import findall


class DataInput:
    """Ввод данных пользователем"""

    def example(self, userInput):
        """Обработка введённых данных пользователя"""

        split_text = map(str, userInput)
        inplett = list(split_text)
        if not findall(r'[КСЗ]', str(inplett)):
            raise ValueError('Введённые данные не содержат элементов для сортировки!')
        return inplett
