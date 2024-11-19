# номер успешной посылки 125682067

def decrypt(command: str) -> str:
    result = ''
    modifier = 0
    stack = []
    for i in command:
        if i.isdigit():
            modifier = modifier * 10 + int(i)
        elif i == '[':
            stack.append([result, modifier])
            result = ''
            modifier = 0
        elif i == ']':
            prev_result, modifier_new = stack.pop()
            result = prev_result + result * modifier_new
        else:
            result += i
    return result


if __name__ == "__main__":
    short_command = input()
    result = decrypt(short_command)
    print(result)