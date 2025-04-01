# This is a more advanced version of the max_pairwise_product.py program.
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
def max_pairwise_product_one(numbers): # 2n comparisons
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


if __name__ == '__main__':
    _ = int(input())
    input_numbers = list(map(int, input().split()))
    print(max_pairwise_product_one(input_numbers))

