# python3


def last_digit_of_fibonacci_number_naive(n):
    assert 0 <= n <= 10 ** 7

    if n <= 1:
        return n

    return (last_digit_of_fibonacci_number_naive(n - 1) + last_digit_of_fibonacci_number_naive(n - 2)) % 10


def last_digit_of_fibonacci_number(n):
    assert 0 <= n <= 10 ** 7
    n = n%60 # Reduce n using the Pisano period
    fib = [0,1]
    for i in range(2, n + 1):
        fib.append((fib[i - 1] + fib[i - 2]))
    return fib[n]%10

# store only two variables instead of the whole array
def last_digit_of_fibonacci_number_one(n):
    assert 0 <= n <= 10 ** 7
    n = n % 60  # Reduce n using the Pisano period
    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append((fib[i - 1] + fib[i - 2]))
    return fib[n] % 10



if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_fibonacci_number(input_n))
