class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        len1 = len(s)
        count = {}
        len2 = len(t) 
        if len1 != len2:
            return False
        for ch in s:
            if ch in count:
                count[ch]+=1
            else:
                count[ch]=1
        for ch in t:
            if ch not in count:
                return False
            else:
                count[ch]-=1
        
        for ch in count.values():
            if ch!= 0:
                return False
            
        return True
        

        