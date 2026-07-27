class Solution:
    def twoSum(self, arr, target):
        for i in range(len(arr)):
            for j in range (i+1, len(arr)):
                if(arr[i]+arr[j] == target):
                    return i, j
arr = [12,34,20,98]
obj = Solution()

print(obj.twoSum(arr,54))