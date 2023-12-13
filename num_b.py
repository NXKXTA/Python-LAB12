def sum_gp(a, q, n):
    if n == 0:
        return 0
    return a + sum_gp(a * q, q, n - 1)


while True:
    try:
        element = int(input("Введите кол-во элементов прогрессии: "))
        if element > 0:
            break
        else:
            print(
                "Ошибка: Введенное число не является натуральным числом. Попробуйте еще раз."
            )
    except ValueError:
        print("Ошибка: Введенное значение не является числом. Попробуйте еще раз.")

try:
    perviy = float(input("Введите первый элемент последовательности: "))
    multiplier = float(input("Введите множитель: "))
except ValueError:
    print("Вы ввели не число")
    exit()

print(sum_gp(perviy, multiplier, element))
