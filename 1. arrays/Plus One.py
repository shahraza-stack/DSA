# Plus One
# link to the leet code ==> https://leetcode.com/problems/plus-one/submissions/1200006516/

# You are given a large integer represented as an integer array digits,
# where each digits[i] is the ith digit of the integer.
# The digits are ordered from most significant to least significant in left-to-right order.
# The large integer does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.


# Example 1:
# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].

# Example 2:
# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# Incrementing by one gives 4321 + 1 = 4322.
# Thus, the result should be [4,3,2,2].


def plusOne(digits):
    # it reverse the list
    for i in reversed(range(len(digits))):
        # now the first digit would be last
        # now we have to is it  9 or not
        if digits[i] != 9:
            # if it is not 9 we will simply +1
            digits[i] += 1
            return digits
        # if it would be 9 we will made it 0
        digits[i] = 0

    return [1] + digits


arr = [1, 2, 3]
print(plusOne(arr))
