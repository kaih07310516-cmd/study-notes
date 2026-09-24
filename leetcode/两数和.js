/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    const n = nums.length;
    for(let i = 0; i<n;i++){
        for(let j = i +1;j<n;j++){
            if(nums[i] + nums[j] ==target){
                return [i,j];
            }
        }
    }
    return[];
};

var twoSum = function(nums, target) {
    const seen = new Map();
    for(let i = 0;i<nums.length;i++){
        const num = nums[i];
        const need = target - num;
        if(seen.has(need)){
            return [seen.has(need),i];
        }
        seen.set(num,i);
    }
    return [];
}