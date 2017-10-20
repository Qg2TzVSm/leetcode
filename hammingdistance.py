# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

# Given two integers x and y, calculate the Hamming distance.
# Input: x = 1, y = 4

# Output: 2

# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑   ↑

# The above arrows point to positions where the corresponding bits are different.
class Solution(object):
	def hammingDistance(self, x, y):
		"""
        :type x: int
        :type y: int
        :rtype: int
        """
		if (x < 0) or (y >= 2147483648):
		    return 'out of range'
		else :
		    a = bin(x)[2:]
		    b = bin(y)[2:]
		    aa = []
		    bb = []
		    answer = 0
		    abmax = max(len(a),len(b))
		    if len(a)>len(b):
		    	for x in a:
		    		aa.append(x)
		    	for x in range(len(a)-len(b)):
		    		bb.append(0)
		    	for x in b:
		    		bb.append(x)
		    elif len(b)>len(a):
		    	for x in b:
		    		bb.append(x)
		    	for x in range(len(b)-len(a)):
		    	    aa.append('0')
		    	for x in a:
		    		aa.append(x)
		    else:
		    	for x in a:
		    		aa.append(x)
		    	for x in b:
		    		bb.append(x)
		    for x in range(abmax):
		    	if aa[x]!=bb[x]:
		    		answer += 1
		    print(answer)
		    return answer


a = Solution()
b = a.hammingDistance(1,4)
