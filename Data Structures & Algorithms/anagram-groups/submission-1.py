from collections import defaultdict,Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        x=defaultdict(list)
        for i in range(len(strs)):
            n="".join(sorted(strs[i]))
            x[n].append(strs[i])
        # print(x.values())
        return list(x.values())
