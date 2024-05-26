class Solution(object):
    def isPalindrome(self, x):
        if x < 0: 
            return False #Negative numbers cannot be palindromes
        
        str_x = str(x) #Converts integer to String
        return str_x == str_x[::-1] #Compares string with its reverse
        
