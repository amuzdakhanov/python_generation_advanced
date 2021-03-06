"""
Напишите программу для определения, является ли число произведением двух чисел из данного набора, выводящую результат в виде ответа «ДА» или «НЕТ».

Формат входных данных
В первой строке подаётся число n(0<n<1000) – количество чисел в наборе.
В последующих nnn строках вводятся целые числа, составляющие набор (могут повторяться).
Затем следует целое число, которое является или не является произведением двух каких-то чисел из набора.

Формат выходных данных
Программа должна вывести «ДА» или «НЕТ» в соответствии с условием задачи.

Примечание 1. Само на себя число из набора умножиться не может, другими словами, два множителя должны иметь разные индексы в наборе.

Примечание 2. Для решения задачи используйте вложенные циклы.


Sample Input 1:
3
33
17
35
999

Sample Output 1:
НЕТ
"""
n = int(input())
nums = []
result = 'НЕТ'
for i in range(n):
    nums.append(int(input()))
big = int(input())

for i in range(n):
    for j in range(0,n):
        if nums[i]*nums[j] == big and i!=j:
            result = 'ДА'
            break
print(result)
