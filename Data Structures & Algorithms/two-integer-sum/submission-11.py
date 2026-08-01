class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = dict(zip(nums,range(len(nums))))
        print(nums_map)
        index = 0 
        for num in nums_map:
            unknown = target - num
            if unknown in nums_map and nums_map[unknown] != index:
                return [index, nums_map[unknown]]
            index+=1


