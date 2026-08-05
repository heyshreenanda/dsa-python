class Solution(object):
    def groupAnagram(self,words):
        freq={}
        for ch in words:
            key = "".join(sorted(ch))

            if key in freq:
                freq[key].append(ch)
            else:
                freq[key]= [ch]
        return list(freq.values())

obj = Solution()
print(obj.groupAnagram(["eat","tea","tan","ate","nat","bat"]))