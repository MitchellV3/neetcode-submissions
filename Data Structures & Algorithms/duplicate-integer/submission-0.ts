class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums: number[]): boolean {
        /*
        Loop through the array 
        Loop again for each value 
        If any match, immediately return true 
        */
        /*
        for (const pivot of nums){
            let matches: number = 0
            for (const num of nums){
                if(num == pivot){
                    matches++
                }
      
            }
            if (matches > 1){
                return true
            }
        }
        return false
    }
    */

        /*
        Improved Solution:
        Convert array to no-dupe data structure
        Compare original array to new data structure
        If they arent equal, return true - otherwise return false
        */
        /*
        const set = new Set(nums)
        const arraySet = [...set]
        console.log(arraySet)
        let i:number = 0
        for (const num of nums){
            console.log(nums[i])
            console.log(arraySet[i])
            if (nums[i] != arraySet[i]){
                console.log('true')
                return true
            }
            i++
            
        }
        return false
          */
    
    /*
    Improved (again) solution 
    Same flow:
    Create a set
    compare length of set to length of array
    */
    const set = new Set(nums)

    console.log(set.size)
    console.log(nums.length)
    if (set.size != nums.length){
        return true
    }
    return false
    }
  
}