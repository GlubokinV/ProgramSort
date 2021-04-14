from New_Class_Sort import DataSort
from InputUserData import DataInput


DataInput = DataInput()
DataSort = DataSort()


input_text = DataInput.example(input("Введите символы, содержащие З, С и К:"))
isolated_text = DataSort.isolator(input_text)
colored_text = DataSort.coloring_letter(isolated_text)
numbered_letter = DataSort.letters_to_numbers(isolated_text)
sorted_number = DataSort.sorter(*[numbered_letter])
result_list = DataSort.numbers_to_letters(sorted_number)
print('Введённые данные:\n', *colored_text)
print('\033[2;0;49mУсловие сортировки:')
print(' \033[2;32;49m З', '\033[2;0;49m<', '\033[2;34;49m С', '\033[2;0;49m <', '\033[2;31;49m К', '\033[2;0;49m ')
print('Отсортированные данные:\n', *result_list)
print('\033[2;0;49mСортировка завершена')
