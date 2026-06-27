class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Group anagrams into sublists within a list 
        # Steps: 
        # Loop through each string, loop through again to compare each string to the others
        # Compare by sorting the string and comparing lengths
        # If multiple strings match, add the original unsorted strings to the new list as a sublists
        map = {}
        for string in strs:
            sorted_str = "".join(sorted(string))
            if sorted_str not in map:
                map[sorted_str] = [string]
            else:
                map[sorted_str].append(string)
        return list(map.values())