#Given nums = [2, 7, 11, 15], target = 9,

#Because nums[0] + nums[1] = 2 + 7 = 9,
#return [0, 1].

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums.sort()
        nums_len = len(nums)
        arr = []
        answer = []
        if nums[0] > target:
        	return 'error'
        for x in range(nums_len):
            if nums[x] <= target:
        	    arr.append(nums[x])    
        for y in arr:
        	if y == target:
        	    return y
        	else :
        		    for i in range(len(arr)):
        			    for j in range(1,len(arr)):
        				    if (arr[i]+arr[j]) == target:
        					    answer.append(i)
        					    answer.append(j)
        					    return answer


sol = Solution()
answer = sol.twoSum([2, 7, 11, 15], 9)
print('answer is: ', answer)

