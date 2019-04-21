#В матрице a(n, m) поменять местами столбцы с минимальным и максимальным
# количествами четных элементов. Матрица — список списков.
def change(a):

    n = len(a)
    m = len(a[0])


    for j in range(m):
        b = []
        count = 0
        for i in range(n):
            if a[i][j] % 2 == 0:
                count += 1
        b.append(count)
    a.append(b)
    print(a)




a = [[1, 2, 3], [4, 6, 7], [8, 8, 2]]
c = change(a)