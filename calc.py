# Напишите программу вычисления арифметического выражения заданного строкой. 
# Используйте операции +,-,/,*. приоритет операций стандартный. 
# 2+2 => 4; 1+2*3 => 7;  1-2*3 => -5;
def calc(my_list):

    if '*' in my_list or '/' in my_list:
        for i in range(1, len(my_list), 2):
            if my_list[i] == '*':
                result = my_list.pop(i+1) * my_list.pop(i-1)
                my_list[i-1] = result
            elif my_list[i] == '/':
                result = my_list.pop(i+1) / my_list.pop(i-1)
                my_list[i-1] = result

    if '+' in my_list or '-' in my_list:
        for i in range(1, len(my_list), 2):
            if my_list[i] == '-':
                result = my_list.pop(i+1) - my_list.pop(i-1)
                my_list[i-1] = result
            elif my_list[i] == '+':
                result = my_list.pop(i+1) + my_list.pop(i-1)
                my_list[i-1] = result
    
    return my_list
   
s = '3*(10+12)'
num = ''
old_list = []
for elem in s:
    if elem.isdigit():
        num += elem
    elif elem in '()':
        old_list.append(elem)
    else:
        old_list.append(int(num))
        old_list.append(elem)
        num = ''
if s[-1] == ')':
    old_list.insert(-1, int(num))
else:    
    old_list.append(int(num))

if '(' in old_list:
    first_i = old_list.index('(')
    second_i = old_list.index(')')
    old_list = old_list[:first_i] + calc(old_list[first_i+1:second_i]) + old_list[second_i+1:]

old_list = calc(old_list)
print(old_list)