def twoSum(self, nums: List[int], target: int) -> List[int]:     
    key = {}
    for i, n in enumerate(nums):
        x = target - n
        if x in key:
            return [key[x], i]
        else:
            key[n] = i