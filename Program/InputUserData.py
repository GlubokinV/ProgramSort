from re import findall


class DataInput:
    """Ввод данных пользователем"""

    # def example(self, userInput):
    #     """Обработка введённых данных пользователя"""
    #     self.userInput = userInput
    #     if not self.userInput:
    #         raise print('Вы ничего не ввели')
    #     __splitted_text = map(str, userInput)
    #     inplett = list(__splitted_text)
    #     fitr = r'[КСЗ]'
    #     if not findall(fitr, userInput):
    #         raise print('Нет символов для сортировки')
    #     # print('результат работы example:', inplett)
    #     return inplett



    def example(self, userInput):
        """Обработка введённых данных пользователя"""

        split_text = map(str, userInput)
        inplett = list(split_text)
        if findall(r'[КСЗ]', str(userInput)) == []:
            raise ValueError('Введённые данные не содержат элементов для сортировки!')
        return inplett


