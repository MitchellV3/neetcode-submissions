class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Need to find: Indecies of numbers in nums that equal target
        # Have: List of numbers, a  target int   
        # Steps:
        # For each number in nums, compare it to the other numbers in nums
        # If they add to 10, return positions (nums[x], nums[y])
        # 
        # Initial Solution
        #outer_index = 0
        #for outer_num in nums:
        #    print("outer", outer_num)
        #    inner_index = 0
        #    for inner_num in nums: 
        #        print("inner", inner_num)
        #        if target == outer_num + inner_num and outer_index != inner_index:
        #            print(nums[outer_index],"|",nums[inner_index])
        #            return [outer_index, inner_index]
        #        inner_index+= 1    
        #            
        #    outer_index+= 1
        index = 0
        map = dict()
        for num in nums:
            compliment = target - num
            if compliment in map:
                return [map[compliment], index]
            map[num] = index
            index+=1