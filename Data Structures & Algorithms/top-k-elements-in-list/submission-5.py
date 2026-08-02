class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = {}
        for num in nums:
            if num in dictionary: 
                dictionary[num] += 1
            else: 
                dictionary[num] = 1
        print(dictionary)
        values = sorted(dictionary.items(),key=lambda item: item[1],reverse=True)[:k]
        print(values)
        return [item[0] for item in values]
        