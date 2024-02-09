import numpy as np

vect = np.zeros(10)
print(vect)
 
vect = np.zeros(10)
vect[3::4] = 5

print(vect)

vect = np.arange(25, 51)

print(vect)

matrix = np.random.randint(1, 50, size=(4, 4))

print(matrix)
print("Елементи першого ряду: ", matrix[0, :])
print("Елементи другого стовпця: ", matrix[:, 1])
print("Сума елементів третього ряду: ", np.sum(matrix[2, :]))
print("Середнє значення елементів 4 стовпця:", np.mean(matrix[:, 3]))

min_element = np.min(matrix)
max_element = np.max(matrix)
min_index = np.unravel_index(np.argmin(matrix), matrix.shape)
max_index = np.unravel_index(np.argmax(matrix), matrix.shape)
print("Мінімальний елемент:", min_element, "Індекс:", min_index)
print("Максимальний елемент:", max_element, "Індекс:", max_index)

diag_elements = np.diagonal(matrix)
non_zero_diag_elements = diag_elements[diag_elements != 0]
product_non_zero_diag = np.prod(non_zero_diag_elements)
print("Добуток ненульових елементів головної діагоналі:", product_non_zero_diag)

matrix[:, [1, 3]] = matrix[:, [3, 1]]
print("Матриця після перестановки 2-го та 4-го стовпців:")
print(matrix)

data = np.array([
    [-8, -14, -19, -18],
    [25, 28, 26, 20],
    [11, 18, 20, 25]
])
fourday = data[1, 3]
print("Температура на 2-й метеостанції за 4 день: ", fourday)

twoday = data[:, 1]
print("Показники всіх метеостанцій за 2-й день: ", twoday)

average = np.mean(data[2])
print("Середня температура за 4 дні по 3 метеостанції:", average)

from24_to26 = np.where((data >= 24) & (data <= 26))
print("Температура в діапазоні 24-26 градусів тепла:")
for station, day in zip(from24_to26[0], from24_to26[1]):
    print("Метеостанція", {station + 1}, "День", {day + 1})

array_2x2 = np.array([[4, 2],
                      [3, 1]])

print("Оригінальний масив: ")
print(array_2x2)

first_axis= np.sort(array_2x2, axis=0)
print("Сортування вздовж першої вісі: ")
print(first_axis)

last_axis = np.sort(array_2x2, axis=1)
print("Сортування вздовж останньої вісі: ")
print(last_axis)

arraynan = np.array([[1, 2, np.nan],
                           [4, np.nan, 6],
                           [7, 8, 9]])

array = np.array([[10, 20, 30],
                            [40, 50, 60],
                            [70, 80, 90]])
mean_value = np.nanmean(array)
arraynan[np.isnan(arraynan)] = mean_value

print("Масив замість NaN: ")
print(arraynan)

array = np.array([[2, 9, 4, 7, 12],
                    [5, 3, 15, 8, 6],
                    [10, 1, 6, 9, 4],
                    [7, 8, 3, 11, 2]])

result = array[(array > 6) | (array % 3 == 0)]
print("Елементи більше 6 або кратні 3:")
print(result)

def has_zero(matrix):
    return np.any(np.all(matrix == 0, axis=0))

n = 4 
matrix = np.array([[1, 0, 3, 4],
                     [0, 0, 0, 2],
                     [5, 0, 7, 8],
                     [0, 0, 0, 0]])

if has_zero(matrix):
    print("Матриця має хоча б один нульовий стовпець.")
else:
    print("Матриця не має нульових стовпців.")


def diagonal_sum(matrix):
    if matrix.shape[0] != matrix.shape[1]:
        raise ValueError("Матриця не є квадратною")

    return np.trace(matrix)

my_matrix = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])

try:
    result = diagonal_sum(my_matrix)
    print("Сума діагональних елементів:", result)
except ValueError as e:
    print(e)


def modify_array(arr):
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            if 10 <= arr[i, j] <= 20:
                arr[i, j] = -arr[i, j] 
            elif 0 <= arr[i, j] <= 9:
                arr[i, j] *= 3 

array = np.array([[5, 15, 25],
                     [10, 12, 18],
                     [3, 8, 14]])

print("Початковий масив:")
print(array)

modify_array(array)

print("Масив після модифікації:")
print(array)