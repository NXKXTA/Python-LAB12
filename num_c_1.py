def rec(q, n, q1):
    if n <= 1:
        return q1
    return q + rec(q, n - 1, q1)


print(rec(2, 3, 2))
