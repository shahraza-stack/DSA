# Move Zeroes
# link to leetcode ==> https://leetcode.com/problems/move-zeroes/description/

# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.


# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:

# Input: nums = [0]
# Output: [0]


def moveZeroes(nums):
    left = 0
    for right in range(len(nums)):
        # if the current element at right pointer is non-zero
        if nums[right]:
            # Swap the non-zero element at right with the element at left
            nums[left], nums[right] = nums[right], nums[left]
            # Move the left pointer to the next position for the next non-zero element
            left += 1
    return nums


nums = [0, 1, 0, 12, 13]
print(moveZeroes(nums))
