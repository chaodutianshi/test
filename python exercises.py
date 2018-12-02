#给定一个整数数组和一个目标值，找出数组中和为目标值的俩位数
class Solution(object):
    def twoSum(self,nums,target):
        #type nums:List[int]
        #type target:int
        #type:List[int]
        d = {}
        for i, num in enumerate(nums):
            if target - num in d:
                return[d[target - num], i]
            d[num] = i
        #no special case handing becasue it is assumed that it has only one solution
        
        
        
        #给定一个32位有符号整数，将整数中的数字进行反转
#Reverse integer
class Solution(object):
    def reverse (self,x):
        #type x:int 
        #type x
        sign = x < 0 and -1 or 1
        x = abs(x)
        ans = 0
        while x:
            ans = ans*10 + x%10
            x/= 10
        return sign*ans if ans <= 0x7ffffff else 0
