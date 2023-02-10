text = '   heLlo woRld!***'  # строка для тестов

#                           КОНВЕРТАЦИЯ РЕГИСТРА

# Возвращает копию строки, в которой: первый символ имеет верхний регистр, а все остальные нижний регистр
cap = text.capitalize()
print(f'text.capitalize() = {cap}')  # результат = Hello world!

# Возвращает копию строки, в которой: символы имеют зеркальный регистр
swap = text.swapcase()
print(f'text.swapcase() = {swap}')  # результат = HElLO WOrLD!

# Возвращает копию строки, в которой: первый символ каждого слова в верхнем регистре
t = text.title()
print(f'text.title() = {t}')  # результат = Hello World!

low = text.lower()  # Возвращает копию строки, в которой: все символы в нижнем регистре
print(f'text.lower() = {low}')  # результат = hello world!***

upp = text.upper()  # Возвращает копию строки, в которой: все символы в верхнем регистре
print(f'text.upper() = {upp}')  # результат = HELLO WORLD!***

#                           ПОИСК И ЗАМЕНА

# Считает количество непересекающихся вхождений подстроки в исходную строку. Возвращает int
coun = text.count('l')
print(f'text.count("l") = {coun}')  # результат = 2

# Определяет начинается ли исходная строка заданной подстрокой. Возвращает True/False
swi = text.startswith('he')
# результат = False (т.к. в начале строки пробелы)
print(f'text.startswith(\'he\') = {swi}')

# Определяет оканчивается ли исходная строка заданной подстрокой. Возвращает True/False
endswi = text.endswith('ld!')
# результат = False (т.к. в конце строки пробелы)
print(f'text.endswith(\'ld!\') = {endswi}')

find = text.find(
    'w')  # Находит индекс первого вхождения подстроки в исходной строке. Возвращет int или -1, если не найдено.
print(f'text.find(\'w\') = {find}')  # результат = 9

rfind = text.rfind('d')  # Аналогичен find(), НО ищет с конца строки.
print(f'text.rfind(\'d\') = {rfind}')  # результат = 13

# Аналогичен find(), НО если  не найдено возвращает исключение ValueError: substring not found
index = text.index('l')
print(f'text.index(\'l\') = {index}')  # результат = 6

rindex = text.rindex('R')  # Аналогичен index(), НО ищет с конца строки
print(f'text.rindex(\'R\') = {rindex}')  # результат = 11

# Возвращает копию строки у которой удалены пробелы в начале и в конце строки.
strip = text.strip()
print(f'text.strip() = {strip}')  # результат = heLlo woRld!***

# Возвращает копию строки у которой удалены пробелы в начале строки.
lstrip = text.lstrip()
print(f'text.lstrip() = {lstrip}')  # результат = heLlo woRld!***

# Возвращает копию строки у которой удалены пробелы в конце строки.
rstrip = text.rstrip()
print(f'text.rstrip() = {rstrip}')  # результат =    heLlo woRld!***

del_strip = text.rstrip(
    '*')  # strip(), lstrip(), rstrip() могут принимать опциональный аргумент <chars>, который определяет набор символов для удаления.
print(f'text.rstrip(\'*\') = {del_strip}')  # результат =    heLlo woRld!

# Возвращает копию строки со всеми вхождениями строки <old> замененными на <new>.
replace = text.replace('l', 'L')
# результат =    heLLo woRLd!***
print(f'text.replace(\'l\', \'L\') = {replace}')

#                           КЛАССИФИКАЦИЯ СИМВОЛОВ

# Определяет состоит ли строка из буквенно-цифровых символов. Возвращает True/False
alnum = text.isalnum()
print(f'text.isalnum() = {alnum}')  # результат = False

# Определяет состоит ли строка из только буквенных символов. Возвращает True/False
alpha = text.isalpha()
print(f'text.isalpha() = {alpha}')  # результат = False

# Определяет состоит ли строка из только из цифровых символов. Возвращает True/False
digit = text.isdigit()
print(f'text.isdigit() = {digit}')  # результат = False

# Определяет состоит ли строка только из символов нижнего регистра. Возвращает True/False
lower = text.islower()
print(f'text.islower() = {lower}')  # результат = False

# Определяет состоит ли строка только из символов верхнего регистра. Возвращает True/False
upper = text.isupper()
print(f'text.isupper() = {upper}')  # результат = False

# Определяет состоит ли строка только из символов пробела. Возвращает True/False
space = text.isspace()
print(f'text.isspace() = {space}')  # результат = False

#                           ЮНИКОД

# Позволяет определить код символа в таблице Unicode. Аргументом является char. Возвращает int.
inord = ord('a')
print(f'ord(\'a\') = {inord}')  # результат = 97

# Позволяет по коду символа определить сам символ. Аргументом является int. Возвращает char.
inchr = chr(65)
print(f'chr(65) = {inchr}')  # результат = A
