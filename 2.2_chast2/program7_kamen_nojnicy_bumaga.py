"""
Тимур и Руслан пытаются разделить фронт работы по курсу "Python для профессионалов".
Для этого они решили сыграть в камень, ножницы и бумагу.
Помогите ребятам бросить честный жребий и определить, кто будет делать очередной модуль нового курса.

Формат входных данных
На вход программе подаются две строки текста, содержащие слова "камень", "ножницы" или "бумага".
На первой строке записан выбор Тимура, на второй – выбор Руслана.

Формат выходных данных
Программа должна вывести результат жеребьёвки, то есть кто победит: Тимур, Руслан или же они сыграют вничью.

Примечание. Правила игры стандартные: камень побеждает ножницы, но проигрывает бумаге, а ножницы побеждают бумагу.

Sample Input 1:
камень
бумага

Sample Output 1:
Руслан

Sample Input 2:
камень
камень

Sample Output 2:
ничья

Sample Input 3:
камень
ножницы

Sample Output 3:
Тимур
"""
def jesty(t,r):
    if t ==r :
        return 'ничья'
    elif t == 'бумага'  and r == 'камень' or \
         t =='камень' and r=='ножницы' or \
         t == 'ножницы' and r == 'бумага':
         return 'Тимур'
    else:
        return 'Руслан'

t = input()
r = input()

print(jesty(t,r))