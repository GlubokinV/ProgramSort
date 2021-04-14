# ProgramSort
Тестовое задание (Программа сортировки символов "К, З, С" по цветам)

Для корректного отображения работы программы, а именно покраски букв,
необходима поддержка стандарта ANSI.

В windows 10 можно проверить этот параметр в реестре:

[HKEY_CURRENT_USER \ Console] "VirtualTerminalLevel" = DWORD: 00000001

Программа запускается файлом StartProgram.py

##Описание работы программы:

При запуске программа запрашивает на ввод строку для сортировки.

Для сортировки принимаются только символы К, З и С, остальные введённые символы не будут учтены.

Каждая из букв "К, З и С" соответствуют цвету "Красный(К), Зелёный(З) и Синий(С)".

Условием сортировки является: "З<С<К".

Результатом работы программы является упорядоченный по заданному условию набор символов, определённых цветов.