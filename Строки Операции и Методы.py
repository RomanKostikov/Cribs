объект.метод(аргумент)
a.upper()  - все буквы заглавные
a.lower() - все буквы маленькие
a.capitalize() - строка с заглавной буквы все остальные с маленькой
a.swapcase() - меняет регистр каждой буквы
a.title() -  каждое слово в строке становится с заглавной буквы
a.count("о")  - сколько раз встретилась буква "о"
a.count("о",6,9)  - сколько раз встретилась буква "о" с 6й по 9ю позицию
a.startswith("о") - начинается ли строка "о"
a.endswith("о") - оканчивается ли строка "о"
a.find - ищет букву или слог и возвращает индекс, если такой нет в строке то выдаст -1
a.rfind - ищет справа а не слева и возвращает индекс
a.index("о") - возвращает индекс, если такой нет в строке то выдаст ошибку
a.rindex("о")
a.replace("o","???") - замена
a.replace(" ","") - удалит пробелы./
a.replace("д","", 2) - удалит первые две д
'asdfgasdgdfs'.isalpha() - состоит ли строка из букв целиком (True,False)
'6549675'.isdigit() - состоит ли строка из цифр целиком (True,False)
'6549sdg675'.isalnum() - состоит ли строка из букв и цифр (True,False)
.islower()
.isupper()
isinstance(obj, classinfo) -> bool - возвращает либо True либо False, в зависимости от того, является ли объект obj указанным классом classinfo
isspace() - состоит ли строка целиком из пробелов
def isEnglish(letter):   # состоит ли строка из английских букв
    return letter.isascii() and letter.isalpha()
a.rjust(9) - дополняет строку что бы она 9 символов, наши символы смещаются в конец строки(вправо)
a.ljust(6) - дополняет строку что бы она 6 символов, наши символы смещаются в начало строки(влево)
a.split() - разбивает нашу строку на элементы, по умолчанию там где пробелы ['sdf', 'sdfs','sdf']
len(a.split()) - количество слов
'='.join(a) - элементы соединяться  знаком =
','.join(a.split()) - пробелы заменит на ","
a.strip() - удаляет знаки пробелов и перенос на новые строик со всех сторон
a.lstrip() - удаляет слева
a.rstrip() - удаляет справа
`
Такой код:
s = 'Python'

print(*s)
print()
print(*s, sep='\n')

выведет:

P y t h o n

P
y
t
h
o
n

print(ord('Ё'))
print(chr(1072))
a-1072
я-1103
А-1040
Я-1071

a-97
z-122
A-65
Z-90

name = "John"
print('Hi, %s.' % name, end=" ")  - Hi, John
print('Hi, {name}'.format(name), end=" ")  - Hi, {name}
print(f'Hi, {name}.')  - Hi, John.

number = int(input('Enter your number: '))

if (number % 5 == 0 and number % 10 == 0 or number % 15 == 0) and number % 30 != 0:
    print('Your number is nice!')
else:
    print('Try again')
