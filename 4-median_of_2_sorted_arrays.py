class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1+nums2
        nums.sort()
        print(nums)
        if len(nums)%2!=0:
            return nums[ceil(len(nums)/2)-1]
        else:
            return float(nums[ceil(len(nums)/2)-1]+ nums[ceil(len(nums)/2)])/2