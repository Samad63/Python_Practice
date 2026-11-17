def find_max(nums):
    largest = nums[0]

    for x in nums[1:]:
        if x > largest:
            largest = x

    return largest

numbers = [12, 45, 7, 89, 23, 56]
print("The largest number is:", find_max(numbers))
