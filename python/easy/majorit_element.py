class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        temp = {}
        for i in nums:
            temp[i] = 1 + temp.get(i, 0)
        return max(temp, key=temp.get)
    
    #another solution
    def majorityElement2(sel, nums: List[int]) -> int:
        temp = {}
        maximum = 0
        for i in nums:
            temp[i] = 1 + temp.get(i, 0)

        for k, v in temp.items():
            if v > maximum:
                maximum = v
        
        for k, v in temp.items():
            if v == maximum:
                return k
            
    #3rd solution

    def majorityElement3(sel, nums: List[int]) -> int:
        temp = {}

        for i in nums:
            temp[i] = 1 + temp.get(i, 0)

        for k, v in temp.items():
            if k >= len(nums)/2: return k

    #4th solution

    def majorityElement4(sel, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]