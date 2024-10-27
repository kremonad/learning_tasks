def fibonacci(version: int) -> int:
    if version <= 1:
        return 1
    else:
        return fibonacci(version - 1) + fibonacci(version - 2)


if __name__ == '__main__':
    version = int(input())
    result = fibonacci(version)
    print(result)
