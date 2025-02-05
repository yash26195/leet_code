class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        "returns the 2 indices where the numbers add up to target"

        for idx,num1 in enumerate(nums):

            if target-num1 in nums and nums.index(target-num1)!=i:
                return(i,nums.index(target-num1))
    