import sys


def load_nums(file_path):
    with open(file_path, 'r') as file:
        nums = [int(line.strip()) for line in file if line.strip()]
    return nums


def steps_to_median(nums):
    nums.sort()
    median = nums[len(nums) // 2]
    return sum(abs(num - median) for num in nums)


def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <nums_file>")
        return
    nums_file = sys.argv[1]
    nums = load_nums(nums_file)
    result = steps_to_median(nums)
    print(result)


if __name__ == "__main__":
    main()
