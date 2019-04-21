# 7. В квадратной матрице a(n, n) в каждой строке элемент, расположенный на диагонали,
# увеличить на значение минимального элемента соответствующего столбца. Матрица —
# список списков. (2 балла)

def change():
    # Определяем длину квадратной мартицы
    n = len(a)
    # Создаем столбцы и заполняем их строками (как обычно только наоборот)
    for j in range(n):
        elem_сolumn = []
        # Построчно заполняем столбцы
        for i in range(n):
            elem_сolumn.append(a[i][j])
        # К элементам диагонали прибавляем минимальный элемент столбца
        a[j][j] += min(elem_сolumn)
    return a

a = [[1, 1, 1],
     [2, 2, 2],
     [3, 3, 3]]
print(change())
