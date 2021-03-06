"""
Дан набор точек на координатной плоскости. Необходимо подсчитать и вывести количество точек, 
лежащих в каждой координатной четверти.

Формат входных данных
В первой строке записано количество точек. 
Каждая следующая строка состоит из двух целых чисел — координат точки (сначала абсцисса – x, затем ордината – y), разделенных символом пробела.

Формат выходных данных
Программа должна вывести количество точек, лежащих в каждой координатной четверти, как в примерах.

Примечание. Учтите, что точки, лежащие на осях координат, не принято относить к какой-либо координатной четверти.


Sample Input 1:
4
0 -1
1 2
0 9
-9 -5

Sample Output 1:
Первая четверть: 1
Вторая четверть: 0
Третья четверть: 1
Четвертая четверть: 0
"""
n = int(input())
x =[]
y=[]
for i in range(n):
    i = input().split()
    x.append(int(i[0]))
    y.append(int(i[1]))  
counter_I = 0
counter_II = 0
counter_III = 0
counter_IV = 0
for j in range(n):
    if x[j] > 0 and y[j] > 0:
        counter_I += 1
    elif x[j] < 0 and y[j] > 0:
        counter_II += 1
    elif x[j] < 0 and y[j] < 0:
        counter_III += 1
    elif x[j] > 0 and y[j] < 0:
        counter_IV += 1
        
print('Первая четверть:',counter_I)   
print('Вторая четверть:',counter_II)   
print('Третья четверть:',counter_III) 
print('Четвертая четверть:',counter_IV) 