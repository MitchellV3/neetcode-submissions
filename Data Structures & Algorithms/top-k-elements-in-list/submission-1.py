class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Given: List of integers, top k number of elements to return
        # Output order does not matter
        # Make map from unique values (set?)
        # Add number as key, count as value
        # Find the highest count and return key
        nums_set = list(set(nums))
        nums_map = {num:0 for num in nums_set}
        #print("set: ", nums_set)
        #print("map: ", nums_map)
        for num in nums:
            nums_map[num] += 1
            #print("map in loop: ", nums_map)
          
        #print("final map: ", nums_map)
        final_list = []
        for item in sorted(nums_map.items(),key=lambda x: x[1], reverse=True)[:k]:
            #print([item[0]])
            final_list.append(item[0])
        return final_list
        

        