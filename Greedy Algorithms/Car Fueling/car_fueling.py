# python3


def compute_min_number_of_refills(d, m, stops):
    assert 1 <= d <= 10 ** 5
    assert 1 <= m <= 400
    assert 1 <= len(stops) <= 300
    assert 0 < stops[0] and all(stops[i] < stops[i + 1] for i in range(len(stops) - 1)) and stops[-1] < d

    stops = [0] + stops + [d]
    num_refills = 0
    current_refill = 0
    while current_refill < len(stops) - 1:
        last_refill = current_refill
        while (current_refill < len(stops) - 1 and # Move i forward while the next stop is within reach of the last refill stop
               stops[current_refill + 1] - stops[last_refill] <= m):
            current_refill += 1

        if current_refill == last_refill:
            return -1

        if current_refill < len(stops) - 1:
            num_refills += 1
    return num_refills

if __name__ == '__main__':
    input_d = int(input())
    input_m = int(input())
    input_n = int(input())
    input_stops = list(map(int, input().split()))
    assert len(input_stops) == input_n

    print(compute_min_number_of_refills(input_d, input_m, input_stops))
