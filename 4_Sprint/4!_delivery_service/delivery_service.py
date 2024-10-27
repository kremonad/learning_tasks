# номер успешной посылки 122630276
import sys


def main(robots_weight: list[int], limit: int) -> int:
    platforms = 0
    sorted_robots = sorted(robots_weight)
    if sorted_robots[-1] > limit:
        return "Вес отдельного робота не может превышать limit."
    for _ in range(len(sorted_robots)):
        if sorted_robots[-1] + sorted_robots[0] <= limit:
            platforms = platforms + len(sorted_robots) // 2 + len(sorted_robots) % 2
            break
        else:
            sorted_robots.pop()
            platforms += 1
    return platforms


if __name__ == "__main__":
    robots_weight = [int(el) for el in sys.stdin.readline().rstrip().split()]
    limit = int(input())
    result = main(robots_weight, limit)
    print(result)
