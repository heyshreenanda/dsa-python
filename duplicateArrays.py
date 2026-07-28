class Solution:
    def removeDup(self, nums):
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[k-1]:
                nums[k]=nums[i]
                k += 1
        return k

obj = Solution()
print(obj.removeDup([1,2,2,3,4,4,4,5]))