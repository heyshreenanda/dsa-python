#217. Contains Duplicate

#Given an integer array nums, return true if any value appears at least twice in the array, and return'''' false if every element is distinct

#Time complexity is O(n) and Space Complexity is O(n)

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