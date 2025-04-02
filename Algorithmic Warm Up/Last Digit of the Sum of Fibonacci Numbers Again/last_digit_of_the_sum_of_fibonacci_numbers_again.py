# python3

def last_digit_of_the_sum_of_fibonacci_numbers_again_naive(from_index, to_index):
    assert 0 <= from_index <= to_index <= 10 ** 18

    if to_index == 0:
        return 0

    fibonacci_numbers = [0] * (to_index + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, to_index + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]

    return sum(fibonacci_numbers[from_index:to_index + 1]) % 10


def last_digit_of_the_sum_of_fibonacci_numbers_again(from_index, to_index):
    assert 0 <= from_index <= to_index <= 10 ** 18

    reduced_index_t = (to_index+2) % 60
    reduced_index_f = (from_index+1) % 60

    previous, current = 0, 1
    for i in range(2, reduced_index_f+1):
        previous, current = current, (previous + current) % 10
    fib_mod_10_f = reduced_index_f if reduced_index_f <= 1 else current

    previous2, current2 = 0, 1
    for i in range(2, reduced_index_t+1):
        previous2, current2 = current2, (previous2 + current2) % 10
    fib_mod_10_t = reduced_index_t if reduced_index_t <= 1 else current2

    return (fib_mod_10_t-fib_mod_10_f) % 10

if __name__ == '__main__':
    input_from, input_to = map(int, input().split())
    print(last_digit_of_the_sum_of_fibonacci_numbers_again(input_from, input_to))
