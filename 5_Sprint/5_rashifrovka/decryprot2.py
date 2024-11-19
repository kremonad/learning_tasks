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
            decrypt(command[start:])
        elif command[i] == ']':
            return result
        else:
            result += command[i]
    return result * int(modifier)


if __name__ == "__main__":
    short_command = input()
    result = decrypt(short_command)
    print(result)


# 3[a]2[bc]
# aaabcbc

# 3[a2[c]]
# accaccacc