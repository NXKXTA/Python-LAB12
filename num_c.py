def n_ap(first_element, pribavka, element):
    if element == 1:
        return first_element
    return n_ap(first_element + pribavka, pribavka, element - 1)


while True:
    try:
        n = int(input("Введите нужный элемент прогрессии: "))
        if n > 0:
            break
        else:
            print(
                "Ошибка: Введенное число не является натуральным числом. Попробуйте еще раз."
            )
    except ValueError:
        print("Ошибка: Введенное значение не является числом. Попробуйте еще раз.")

try:
    perviy = float(input("Введите первый элемент последовательности: "))
    plus = float(input("Введите прибавку: "))
except ValueError:
    print("Вы ввели не число")
    exit()

print(n_ap(perviy, plus, n))
