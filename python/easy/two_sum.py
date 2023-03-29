class Solution:
    #Time complexity O(n^2)
    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
    
    #Time complexity O(n) hash map solution:
    def twoSum2(self, nums: List[int], target:int) -> List[int]:
        matches = {}
        for number in nums:
            match = target - number
            if match in matches:
                return [match, number]
            else:
                matches[number] = True
        return []
    
    #Time complexity O(log(n)) pointers:
    def twoSum3(self, nums: List[int], target:int) -> List[int]:
        nums.sort()
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[left] + nums[right] == target:
                return [nums[left], nums[right]]
            elif nums[left] + nums[right] < target:
                left +=1
            elif nums[left] + nums[right] > target:
                right -=1
        return []
