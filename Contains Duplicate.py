# Contains Duplicate
# link to the leetcode ==> https://leetcode.com/problems/contains-duplicate/

def containsDuplicate(nums):
    # i=0
    # a set to store elements
    seen = set()
    for n in nums:
        #  If an element is already in the set, it means a duplicate is found
        if n in seen:
            return True
        seen.add(n)
    return False

num = [1,2,3,4]
num1 = [1,2,3,1]

print(containsDuplicate(num))
print(containsDuplicate(num1))
    