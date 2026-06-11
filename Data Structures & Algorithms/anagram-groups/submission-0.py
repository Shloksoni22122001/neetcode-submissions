from collections import defaultdict,Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        x=defaultdict(list)
        for i in range(len(strs)):
            n=Counter(sorted(strs[i]))
            x[self.flatten_dict(n)].append(strs[i])
        # print(x.values())
        return list(x.values())
    def flatten_dict(self,d):
        return "".join(f"{k}{v}" for k, v in d.items())
