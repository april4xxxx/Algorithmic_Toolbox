# python3


def money_change(money):
    assert 0 <= money <= 10 ** 3
    coin10 = money // 10
    coin5 = (money - coin10 * 10) // 5
    coin1 = money - coin10 * 10 - coin5 * 5
    return coin10 + coin5 + coin1

if __name__ == '__main__':
    input_money = int(input())
    print(money_change(input_money))
