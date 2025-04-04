# python3


def fibonacci_number_again_naive(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    if n <= 1:
        return n

    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % m

    return current


def fibonacci_number_again(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3
    p = pisano_period(m)
    n = n % p
    return fibonacci_number_again_naive(n, m)

def pisano_period(m):
    previous, current = 0, 1
    for i in range(m * m + 1):
        previous, current = current, (previous + current) % m
        # If we see '0, 1' again, the period restarts
        if previous == 0 and current == 1:
            return i + 1

if __name__ == '__main__':
    input_n, input_m = map(int, input().split())
    print(fibonacci_number_again(input_n, input_m))
