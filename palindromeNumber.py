class Solution:
    def isPalindrome(self, x: int) -> bool:
        xNew = str(x)
        left = 0
        right = len(xNew)-1
        while left < right :
            if xNew[left] != xNew[right]:
                return False
            left +=1
            right -=1
        return True



        


        
