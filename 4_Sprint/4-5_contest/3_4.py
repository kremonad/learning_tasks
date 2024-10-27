def main(string):
    char_set = set()
    max_length = 0
    left = 0
    for right in range(len(string)):
        while string[right] in char_set:
            char_set.remove(string[left])
            left += 1
        char_set.add(string[right])
        max_length = max(max_length, right - left + 1)
    return max_length


if __name__ == "__main__":
    string = input()
    print(main(string))