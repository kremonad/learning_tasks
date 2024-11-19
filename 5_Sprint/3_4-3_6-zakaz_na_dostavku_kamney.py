import sys

def distribution(len_purchase, purchase, len_examples, examples):
    sorted_purchase = sorted(purchase, reverse=True)
    sorted_examples = sorted(examples, reverse=True)
    count = 0
    try:
        for i in range(max(len_examples, len_purchase)):
            if sorted_examples[0] >= sorted_purchase[0]:
                sorted_examples.pop(0)
                sorted_purchase.pop(0)
                count += 1
            else:
                sorted_purchase.pop(0)
    except IndexError:
        return count
    return count


if __name__ == '__main__':
    len_purchase = int(input())
    purchase = [int(el) for el in sys.stdin.readline().rstrip().split()]
    len_examples = int(input())
    examples = [int(el) for el in sys.stdin.readline().rstrip().split()]
    result = distribution(len_purchase, purchase, len_examples, examples)
    print(result)
