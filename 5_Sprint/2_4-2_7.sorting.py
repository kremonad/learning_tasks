import sys

def sorting(len_robots, robots, len_template, template):
    result = []
    for i in template:
        while i in robots:
            robots.remove(i)
            result.append(i)
    result.extend(sorted(robots))
    return result


if __name__ == '__main__':
    len_robots = int(input())
    robots = [int(el) for el in sys.stdin.readline().rstrip().split()]
    len_template = int(input())
    template = [int(el) for el in sys.stdin.readline().rstrip().split()]
    result = sorting(len_robots, robots, len_template, template)
    print(" ".join(str(element) for element in result))
