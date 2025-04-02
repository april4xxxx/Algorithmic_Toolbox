# python3


def last_digit_of_the_sum_of_squares_of_fibonacci_numbers_naive(n):
    assert 0 <= n <= 10 ** 18

    if n <= 1:
        return n

    fibonacci_numbers = [0] * (n + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, n + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]

    return sum([f ** 2 for f in fibonacci_numbers]) % 10


def last_digit_of_the_sum_of_squares_of_fibonacci_numbers(n):
    assert 0 <= n <= 10 ** 18

    n_mod = n%60

    fn_mod_10 = fibonacci_mod_10(n_mod)
    fn_plus_1_mod_10 = fibonacci_mod_10((n_mod+1)%60)

    return (fn_mod_10 * fn_plus_1_mod_10) % 10

def fibonacci_mod_10(n):
    if n<=1:
        return n

    prev, curr = 0,1
    for i in range(2,n+1):
        prev, curr = curr, (prev+curr)%10
    return curr

if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_the_sum_of_squares_of_fibonacci_numbers(input_n))
