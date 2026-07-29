class Solution:
    def contains_dupl(self,nums):
        freq = {}
        for ch in nums:
            if ch in freq:
                return True
                
            else:
                freq[ch] = True
        return False
nums = [1,2,3,1]
obj = Solution()
print(obj.contains_dupl(nums))