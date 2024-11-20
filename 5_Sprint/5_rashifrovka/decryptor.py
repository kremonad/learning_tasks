# номер успешной посылки 125682067


def decrypt(command: str) -> str:
    """Рекурсивная функция, которая преобразовывает шифр в команды"""
    result = ""
    digits = "0123456789"
    modifier = 0
    stack = []
    for symbol in command:
        if symbol in digits:
            modifier = modifier * 10 + int(symbol)
        elif symbol == "[":
            stack.append((result, modifier))
            result = ""
            modifier = 0
        elif symbol == "]":
            prev_result, modifier_new = stack.pop()
            result = prev_result + result * modifier_new
        else:
            result += symbol
    return result


if __name__ == "__main__":
    short_command = input()
    result = decrypt(short_command)
    print(result)
