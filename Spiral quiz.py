# Закручивание спирали по часовой стрелке из n элементов
n = int(input())
res = [[0 for j in range(n)] for i in range(n)]
count = 1   #заводм счетчик
for i in range(n):    #количество кругов спирали, а так же смещение
    for col in range(i, n - i):   #строка слева направо
        res[i][col] = count
        count += 1
    for row in range(i + 1, n - i):   #столбец сверху вниз
        res[row][-(i + 1)] = count
        count += 1
    for col in range(n - 2 - i, i, -1):    #строка справа налево
        res[-(1 + i)][col] = count
        count += 1
    for row in range(n - 1 - i, i, -1):    #столбец снизу вверх
        res[row][i] = count
        count += 1
        
# res      
for i in res:
    for j in i:
        print(j, end=' ')
    print()
