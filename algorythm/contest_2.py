import sys

def main():
    elements_count = int(sys.stdin.readline().rstrip())
    result = []
    result_2 = []
    ore_string = [int(el) for el in sys.stdin.readline().rstrip().split()]
    for index in range(elements_count):
        if ore_string[index] not in result:
            result.extend([ore_string[index]])
        else:
            ore_string[index] = '_'
            result_2.extend([ore_string[index]])
    sort_list = sorted(result)
    full_list = sort_list + result_2
    print(*full_list, sep=' ')
    

if __name__ == '__main__':
    main()