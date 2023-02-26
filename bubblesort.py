# Bubble Sort with random list

from random import randint # import random int

nums = [] # list of nums
for i in range(10): 
    nums.append(randint(1, 99)) # append in nums random number 1 - 99
print(nums) # output list with random numbers

for i in range(len(nums)): # sort alhoritm
    for j in range(len(nums)-i-1):
        if nums[j] > nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]
print(nums) # output list with sorting number