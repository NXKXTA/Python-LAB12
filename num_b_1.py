def rec(q, n, q1):
    if n <= 1:
        return [q1, q1]
    rem = rec(q, n - 1, q1)
    w = rem[0] * q
    return [w, rem[1] + w]


print(rec(2, 3, 2)[1])
