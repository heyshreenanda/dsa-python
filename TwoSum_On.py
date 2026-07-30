#two sum optimised O(n)

class Solution(object):
    def twoSum(self,nums,target):
       freq = {}

       for i in range(len(nums)):
           value = target - nums[i]
           if value in freq:
               return [freq[value],i]
           freq[nums[i]] = i

obj = Solution()
print(obj.twoSum([2,7,11],18))
