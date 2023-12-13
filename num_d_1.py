def rec_f(n):
    if n == 1:
        return "1"
    if n == 0:
        return "0"

    if n < 0:
        return "-" + rec_f(-int(n // 2)) + str(n % 2)
    return rec_f(int(n // 2)) + str(n % 2)


print(rec_f(-99))
