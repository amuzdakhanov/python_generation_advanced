"""
Переворот числа

Дано пятизначное или шестизначное натуральное число.
Напишите программу, которая изменит порядок его последних пяти цифр на обратный.

Формат входных данных
На вход программе подается одно натуральное пятизначное или шестизначное число.

Формат выходных данных
Программа должна вывести число, которое получится в результате разворота, указанного в условии задачи. Число нужно выводить без незначащих нулей.


Sample Input 1:

12345

Sample Output 1:

54321

Sample Input 2:

987654
"""
n = input()
len_n = len(n)

if len_n == 5:
    print(int(n[::-1]))
elif len_n == 6:
    print(n[0]+n[:-6:-1])
