"""
Дана квадратная матрица чисел. Напишите программу, которая зеркально отображает её элементы относительно
горизонтальной оси симметрии.

Формат входных данных
На вход программе подаётся натуральное число n — количество строк и столбцов в матрице, затем элементы матрицы построчно
через пробел.

Формат выходных данных
Программа должна вывести матрицу в которой зеркально отображены элементы относительно горизонтальной оси симметрии.
Sample Input 1:
4
1 2 3 4
5 6 7 8
8 6 4 2
3 4 5 6

Sample Output 1:
3 4 5 6
8 6 4 2
5 6 7 8
1 2 3 4
"""

n = int(input())
matrix = []
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)

matrix = matrix[::-1]

for row in matrix:
    print(*row)