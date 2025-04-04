# python3


def compute_optimal_summands(n):
    assert 1 <= n <= 10 ** 9
    summands = []

    # for i in range (1, n + 1):
    #     if n - i < i:
    #         summands.append(n)
    #         break
    #     summands.append(i)
    #     n -= i
    i = 1
    while n > 0:
        n = n-i
        if n < i+1:
            summands.append(n+i)
            return summands
        summands.append(i)
        i+=1
    return summands


if __name__ == '__main__':
    input_n = int(input())
    output_summands = compute_optimal_summands(input_n)
    print(len(output_summands))
    print(*output_summands)
