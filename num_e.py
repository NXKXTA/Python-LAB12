def my_gcd(a, b):
    if b == 0:
        return a
    return my_gcd(b, a % b)


def my_lcm(a, b):
    return a * b // my_gcd(a, b)


print(my_lcm(761457, 614573))
