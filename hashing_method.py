
''' Haashing Method '''

# nums = [5, 6, 7, 7, 1, 9, 11, 1, 1, 5, 1, 1]

# hash_map = {}
# n = len(nums)

# for i in range(0, n):
#     hash_map[nums[i]] = hash_map.get(nums[i], 0) + 1

# print(hash_map)

n = [5, 3, 2, 2, 1, 5, 5, 7, 5, 10]

m = [10, 111, 1, 9, 5, 67, 2]

for num in m:
    count = 0
    for x in n:
        if x == num:
            count += 1

    print(count, end=" ")

