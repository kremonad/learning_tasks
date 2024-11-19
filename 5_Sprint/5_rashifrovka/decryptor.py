# номер успешной посылки 122630276

def decrypt(command: str) -> str:
    result = ''
    digit = '0123456789'
    modifier = ''
    for i in range(len(command)):
        if command[i] in digit:
            modifier += command[i]
        elif command[i] == '[':
            start = i + 1
            end = command.index(']',-1)
            content = decrypt(command[start:end])
            result += int(modifier) * content
            modifier = ''
            return result
        else:
            result += command[i]
    return result


if __name__ == "__main__":
    short_command = input()
    result = decrypt(short_command)
    print(result)


# 3[a]2[bc]
# aaabcbc

# 3[a2[c]]
# accaccacc