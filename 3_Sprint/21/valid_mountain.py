def valid_mountain_array(test_array):
    top_count = 0
    down_count = 0
    for i in range(1, len(test_array) - 1):
        previous = test_array[i-1]
        now = test_array[i]
        next = test_array[i+1]
        if previous < now > next:
            top_count += 1
        if now > next:
            down_count += 1
        elif next == now:
            return False
        if down_count > 0 and next > now:
            return False
    if down_count > 0 and top_count == 1:
        return True
    else:
        return False

if __name__ == '__main__':
    mountain = input()
    mountain_list = [int(x) for x in mountain.split()]
    print(valid_mountain_array(mountain_list))