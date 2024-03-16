class Solution:
    def isPalindrome(self, x: int) -> bool:
        backwards = "".join(reversed(str(x)))
        return True if backwards == str(x) else False
    

solution = Solution()
solution.isPalindrome(121)