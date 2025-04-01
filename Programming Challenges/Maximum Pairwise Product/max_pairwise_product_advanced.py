# This is a more advanced version of the max_pairwise_product.py program.

import math

def max_pairwise_product_fast(numbers): # AI generated
    n = len(numbers)
    if n == 0:
        return 0
    elif n == 1:
        return 0

    max_index1 = -1
    max_index2 = -1

    for i in range(n):
        if max_index1 == -1 or numbers[i] > numbers[max_index1]:
            max_index2 = max_index1
            max_index1 = i
        elif max_index2 == -1 or numbers[i] > numbers[max_index2]:
            max_index2 = i

    return numbers[max_index1] * numbers[max_index2]



# Following instructions in Toolbox_statement
def max_pairwise_product_2n(numbers): # 2n comparisons
    index1 = -1 # not a valid index, no selection has been made, forces 1st value to be selected
    index2 = -1 # if index = 0, setting the best as numbers[0] is not correct
    n = len(numbers)
    for i in range(n):
        if index1 == -1 or numbers[i] > numbers[index1]:  # if index1 = -1, select the first value
            index1 = i
    for i in range(n):
        if i != index1: #avoid selecting the same index
            if index2 == -1 or numbers[i] > numbers[index2]:
                index2 = i

    return (numbers[index1] * numbers[index2])

# 1.5n comparisons
def max_pairwise_product_1point5n(numbers):
    n = len(numbers)
    if numbers[0] > numbers[1]:
        max1 = numbers[0]
        max2 = numbers[1]
    else:
        max1 = numbers[1]
        max2 = numbers[0]
    for i in range(2,n):
        if numbers[i] > max1:
            max2 = max1
            max1 = numbers[i]
        elif numbers[i] > max2:
            max2 = numbers[i]
    return max1 * max2

import math

class Node:
    def __init__(self, winner, beaten):
        self.winner = winner
        self.beaten = beaten  # list of values this winner defeated

def build_tournament(arr):
    # Wrap elements into leaf nodes
    nodes = [Node(x, []) for x in arr]

    while len(nodes) > 1:
        next_round = []
        for i in range(0, len(nodes), 2):
            if i + 1 == len(nodes):
                # odd number, pass node to next round
                next_round.append(nodes[i])
            else:
                a, b = nodes[i], nodes[i + 1]
                if a.winner > b.winner:
                    next_round.append(Node(a.winner, a.beaten + [b.winner]))
                else:
                    next_round.append(Node(b.winner, b.beaten + [a.winner]))
        nodes = next_round

    return nodes[0]  # final winner node

def find_two_largest(arr):
    tournament = build_tournament(arr)
    max1 = tournament.winner
    max2 = max(tournament.beaten)
    return arr[max1] * arr[max2]


if __name__ == '__main__':
    _ = int(input())
    input_numbers = list(map(int, input().split()))
    print(find_two_largest(input_numbers))

