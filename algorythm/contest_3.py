import sys

def main(num_list, number):
    left = 0
    right = len(num_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if num_list[0] >= number:
            return 0
        elif num_list[mid] == number:
            return mid
        elif num_list[mid] < number:
            left = mid + 1
        else:
            return mid
    return mid + 1


if __name__ == '__main__':
    ore_string = [int(el) for el in sys.stdin.readline().rstrip().split()]
    needed_number = int(input())
    result = main(ore_string, needed_number)
    print(result)
