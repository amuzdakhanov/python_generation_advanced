"""
На вход программе подается число n.
Напишите программу, которая создает и выводит построчно список, состоящий из n списков
[[1, 2, ..., n], [1, 2, ..., n], ..., [1, 2, ..., n]].

Формат входных данных
На вход программе подается натуральное число n.

Формат выходных данных
Программа должна вывести построчно указанный список.
Sample Input 1:
3

Sample Output 1:
[1, 2, 3]
[1, 2, 3]
[1, 2, 3]
"""


n = int(input())
list1 = []
for i in range(n):
    mylist = [int(i) for i in range(1,n+1)]
    list1.append(mylist)
print(*list1,sep='\n')