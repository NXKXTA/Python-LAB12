def n_geom_progression(n, first, multiplier):
    if n == 1:
        return first
    return multiplier * n_geom_progression(n - 1, first, multiplier)


while True:
    try:
        element = int(input("Введите натуральное число: "))
        if element > 0:
            break
        else:
            print("Ошибка: Введенное число не является натуральным числом. Попробуйте еще раз.")
    except ValueError:
        print("Ошибка: Введенное значение не является числом. Попробуйте еще раз.")

try:
    perviy = float(input("Введите первый элемент последовательности: "))
    q = float(input("Введите множитель: "))
except ValueError:
    print("Вы ввели не число")
    exit()

print(n_geom_progression(element, perviy, q))
