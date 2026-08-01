class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final_list = []
        strs_map = {}
        for str in strs:
            if "".join(sorted(str)) in strs_map:
               strs_map["".join(sorted(str))].append(str) 
            else:
               strs_map["".join(sorted(str))] = [str]
        return list(strs_map.values())