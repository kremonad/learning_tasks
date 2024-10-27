def main(nums):
    nums_list = [int(x) for x in nums.split()]
    result = []
    for num in nums_list:
        count = 0
        for num_compare in nums_list:
            if num > num_compare:
                count += 1
        result.append(str(count))
    return " ".join(result)


if __name__ == "__main__":
    nums = input()
    print(main(nums))