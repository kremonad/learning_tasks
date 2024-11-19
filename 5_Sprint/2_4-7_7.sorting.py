import sys

def sorting(n, digits):
    count = 0
    left = 0
    right = 0
    next = 0
    for i in range(n):
        right += 1
        if digits[i] == 0:
            while not max(digits[left:right]) == len(digits[left:right]) - 1:
                right += 1
            next = max(digits[:right]) + 1
            left = right = next
            count += 1
        elif next in digits[left:right]:
            count += 1
            next = max(digits[:right]) + 1
            left = right = next
        if right > n:
            return count
    return count


if __name__ == '__main__':
    n = int(input())
    digits = [int(el) for el in sys.stdin.readline().rstrip().split()]
    result = sorting(n, digits)
    print(result)

# 24
# 12 1 8 0 7 17 2 20 9 19 18 6 14 21 10 4 23 5 3 15 13 11 22 16
# 1