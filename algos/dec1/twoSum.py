from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int):
        h = {}

        # iterating a list
        for i, val in enumerate(nums):
            if target - val in h:
                # check if target value - current value exists in dictionary
                return [h[target - val], i]

            # add the values into dictionary if they don't exist there already
            h[val] = i

p1 = Solution()
print(p1.twoSum([2,7,11,15], 13))

# Time complexity
# O(n) - only 1 for loops - 2n => O(n)

# Space complexity
# O(n) because only one dictionary is used
