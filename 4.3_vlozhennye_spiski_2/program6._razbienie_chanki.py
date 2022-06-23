"""
На вход программе подаются две строки, на одной символы, на другой число nnn. Из первой строки формируется список.

Реализуйте функцию chunked(), которая принимает на вход список и число, задающее размер чанка (куска), а возвращает список из чанков указанной длины.

Формат входных данных
На вход программе подается строка текста, содержащая символы, отделенные символом пробела и число nnn на отдельной строке.

Формат выходных данных
Программа должна вывести указанный вложенный список.

Примечание. Не забудьте вызвать функцию chunked(), чтобы вывести результат 😀.
Sample Input 1:
a b c d e f
2

Sample Output 1:
[['a', 'b'], ['c', 'd'], ['e', 'f']]




s = input().split()
n = int(input())
tmp = []
res = []
for i in range(len(s)):
    tmp.append(s[i])
    if len(tmp) == n:
        res.append(tmp)
        tmp = []
if len(s) % n != 0:
    res.append(tmp)
print(res)

"""
s = input().split()
n = int(input())
res = []
while len(s) != 0:
    res.append(s[:n])
    s = s[n:]
print(res)