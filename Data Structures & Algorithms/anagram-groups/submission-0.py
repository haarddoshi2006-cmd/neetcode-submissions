class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ss = defaultdict(list)
        for i in strs:
            s = ''.join(sorted(i))
            ss[s].append(i)
        return list(ss.values())

