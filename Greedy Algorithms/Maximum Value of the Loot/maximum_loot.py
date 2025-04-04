# python3

from sys import stdin


def maximum_loot_value(capacity, weights, prices):
    assert 0 <= capacity <= 2 * 10 ** 6
    assert len(weights) == len(prices)
    assert 1 <= len(weights) <= 10 ** 3
    assert all(0 < w <= 2 * 10 ** 6 for w in weights)
    assert all(0 <= p <= 2 * 10 ** 6 for p in prices)
    final_value = 0
    while capacity>0:
        # max_single = max(prices/weights)
        max_index = max(range(len(prices)), key=lambda i: prices[i] / weights[i])
        # ratios = [p / w for p, w in zip(prices, weights)]
        # max_index = ratios.index(max(ratios))
        if weights[max_index] <= capacity:
            capacity -= weights[max_index]
        else:
            final_value += prices[max_index] / weights[max_index] * capacity
            # print(f"final_value: {final_value}")
            return final_value
        final_value += prices[max_index]/weights[max_index] * weights[max_index]
        # print(f"final_value: {final_value}")
        prices[max_index] = 0
    return final_value
if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, input_capacity = data[0:2]
    input_weights = data[3:(2 * n + 2):2]
    input_prices = data[2:(2 * n + 2):2]
    opt_value = maximum_loot_value(input_capacity, input_weights, input_prices)
    print("{:.10f}".format(opt_value))
    # print(data)
