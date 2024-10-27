def counting(people: list, takt: int) -> int:
    i = 0
    while len(people) != 1:
        i = (i + takt) % len(people)
        people.pop(i)
    return people[0]


if __name__ == '__main__':
    people = [i for i in range(1, int(input()) + 1)]
    takt = int(input())
    result = counting(people, takt - 1)
    print(result)
