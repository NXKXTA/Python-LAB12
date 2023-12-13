def decimal_to_binary(n):
    if n == 0:
        return '0'
    elif n < 0:
        return '-' + decimal_to_binary(-n)
    else:
        result = ''
        while n > 0:
            result = str(n % 2) + result
            n = n // 2
        return result


try:
    digit = int(input('Введите целое десятичное число: '))
except ValueError:
    print('Введено не целое число')
    exit()

print(decimal_to_binary(digit))
