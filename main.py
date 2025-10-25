def getPivot(numbers):
    """
    ########################################
    Code Your Program here
    ########################################
    """
    avg = sum(numbers) / len(numbers)
    pivot = numbers[0]
    min_diff = abs(pivot - avg)
    for num in numbers:
        diff = abs(num - avg)
        if diff < min_diff:
            pivot = num
            min_diff = diff
    return pivot

def split(number):
    """
    ########################################
    Code Your Program here
    ########################################
    """
    pivot = getPivot(number)
    left = [x for x in number if x <= pivot]
    right = [x for x in number if x > pivot]
    return left + [pivot] + right


def main():
    # number = list(map(int, input().split()))
    number = [65, 15, 10, 20, 40, 55]
    number = split(number)
    print(number)


if __name__ == '__main__':
    main()
