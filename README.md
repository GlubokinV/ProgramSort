# ProgramSort v.2.0
### Программа сортировки символов "К, З, С" согласно введённому порядку сортировки(*Тестовое задание*)
### Условия корректного запуска:
Для корректного отображения работы программы, а именно покраски букв,
необходима поддержка стандарта ANSI.
#### В windows 10 можно проверить этот параметр в реестре:
[HKEY_CURRENT_USER \ Console] "VirtualTerminalLevel" = DWORD: 00000001

Программа запускается файлом StartProgram_v2.py

### Описание работы программы:

1. При запуске программа запрашивает на ввод строку для сортировки.

    - Для сортировки принимаются только символы К, З и С, остальные введённые символы не будут учтены.

    - Каждая из букв "К, З и С" соответствуют цвету "Красный(К), Зелёный(З) и Синий(С)".


2. Далее программа запрашивает ввод условия сортировки вида "КЗС"
    - Учтена возможность некорректного ввода строк вида "К", "КЗ" или "3456;%:?КЗЗЗЗКЗС",
      то есть будет учитываться только символы К, З и С, а также их порядок.
    
    

3. Результатом работы программы является упорядоченный по заданному условию набор символов, определённых цветов.


### Иллюстрация результата работы программы:
![image](https://user-images.githubusercontent.com/79124989/116203366-d1e65200-a765-11eb-9426-6a0596de6ffc.png)


Тестовая документация находится в папке Documentation, в корне проекта.




# ProgramSort
### Программа сортировки символов "К, З, С" по цветам (*Тестовое задание*)

## Условия корректного запуска:
Для корректного отображения работы программы, а именно покраски букв,
необходима поддержка стандарта ANSI.

#### В windows 10 можно проверить этот параметр в реестре:

[HKEY_CURRENT_USER \ Console] "VirtualTerminalLevel" = DWORD: 00000001

Программа запускается файлом StartProgram.py

### Описание работы программы:

При запуске программа запрашивает на ввод строку для сортировки.

Для сортировки принимаются только символы К, З и С, остальные введённые символы не будут учтены.

Каждая из букв "К, З и С" соответствуют цвету "Красный(К), Зелёный(З) и Синий(С)".

Условием сортировки является: "З<С<К".

Результатом работы программы является упорядоченный по заданному условию набор символов, определённых цветов.

### Иллюстрация результата работы программы:
![image](https://user-images.githubusercontent.com/79124989/114736339-35d54780-9d70-11eb-94ba-c556c33066fd.png)