class Solution(object):
    def isAnagram(self, s, t):
        freqS = {}
        freqT = {}
        #check the lengths
        if len(s) != len(t):    return False
        #s frequency
        for ch in s:
            if ch in freqS:
                freqS[ch] += 1
            else:
                freqS[ch] = 1

        #same goes to t 
        for char in t:
            if char in freqT:
                freqT[char] += 1
            else:
                freqT[char] = 1

        if freqS == freqT:
            return True
        else: 
            return False

obj = Solution()

print(obj.isAnagram("ananya","yanana"))
print(obj.isAnagram("ananya","banana"))



#first leet-code problem solved with no error submitted once yasssss😭😭 big brain tymmmm

#242 Valid Anagram - Time Complexity : O(n) and Space Complexity : O(n)