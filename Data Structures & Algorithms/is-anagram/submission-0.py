class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        
        if len(s) != len(t):
            return False
        n={}
        m={}
        for c in s:
            if c in n:
                n[c]+=1
            else:
                n[c]=1
        for c in t:
            if c in m:
                m[c]+=1
            else:
                m[c]=1
        return m==n