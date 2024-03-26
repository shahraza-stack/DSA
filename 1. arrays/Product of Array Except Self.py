# Product of Array Except Self

# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

def productExceptSelf(nums):
    answer = [1] * len(nums)
    prefix = 1
    for i in range(len(nums)):
        # Store the prefix product at current index
        answer[i] = prefix
        # Update prefix product for next iteration
        prefix *= nums[i]

    # Calculate postfix products
    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        # Multiply the postfix product with the current answerult value
        answer[i] *= postfix
        # Update postfix product for next iteration
        postfix *= nums[i]

    # Return the final answerult array
    return answer

n = [1,0,30]
print(productExceptSelf(n))