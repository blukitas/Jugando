# https://www.codewars.com/kata/the-millionth-fibonacci-kata/train/python

# The year is 1214. One night, Pope Innocent III awakens to find the the archangel Gabriel floating before him. Gabriel thunders to the pope:
# Gather all of the learned men in Pisa, especially Leonardo Fibonacci. In order for the crusades in the holy lands to be successful, these men must calculate the millionth number in Fibonacci's recurrence. Fail to do this, and your armies will never reclaim the holy land. It is His will.
# The angel then vanishes in an explosion of white light.
# Pope Innocent III sits in his bed in awe. How much is a million? he thinks to himself. He never was very good at math.
# He tries writing the number down, but because everyone in Europe is still using Roman numerals at this moment in history, he cannot represent this number. If he only knew about the invention of zero, it might make this sort of thing easier.
# He decides to go back to bed. He consoles himself, The Lord would never challenge me thus; this must have been some deceit by the devil. A pretty horrendous nightmare, to be sure.
# Pope Innocent III's armies would go on to conquer Constantinople (now Istanbul), but they would never reclaim the holy land as he desired.
# In this kata you will have to calculate fib(n) where:
#     fib(0) := 0
#     fib(1) := 1
#     fin(n + 2) := fib(n + 1) + fib(n)
# Write an algorithm that can handle n up to 2000000.
# Your algorithm must output the exact integer answer, to full precision. Also, it must correctly handle negative numbers as input.
#     HINT I: Can you rearrange the equation fib(n + 2) = fib(n + 1) + fib(n) to find fib(n) if you already know fib(n + 1) and fib(n + 2)? Use this to reason what value fib has to have for negative values.
#     HINT II: See https://mitpress.mit.edu/sites/default/files/sicp/full-text/book/book-Z-H-11.html#%_sec_1.2.4

# Python 3 Program to find n'th fibonacci Number in 
# with O(Log n) arithmatic operations 
MAX = 2000000
  
# Create an array for memoization 
f = [0] * MAX
  
# Returns n'th fuibonacci number using table f[] 
def fib(n): 
    signo = 1
    if (n < 0):
        signo = -1
    n = abs(n)
    
    # Base cases 
    if (n == 0) : 
        return 0
    if (n == 1 or n == 2) : 
        f[n] = 1
        return (f[n]) 
  
    # If fib(n) is already computed 
    if (f[n]) : 
        return f[n] * signo
  
    if( n & 1) : 
        k = (n + 1) // 2
    else :  
        k = n // 2
  
    # Applyting above formula [Note value n&1 is 1 
    # if n is odd, else 0. 
    if((n & 1) ) : 
        f[n] = (fib(k) * fib(k) + fib(k-1) * fib(k-1)) 
    else : 
        f[n] = (2*fib(k-1) + fib(k))*fib(k) 
  
    return f[n] * signo

#https://www.geeksforgeeks.org/program-for-nth-fibonacci-number/ (!)
#https://www.geeksforgeeks.org/find-nth-fibonacci-number-using-golden-ratio/


# #Resultados test:
# Test Results:
#  Basic tests
#  Verifying that fib(0) == 0
#  Verifying that fib(1) == 1
#  Verifying that fib(2) == 1
#  Verifying that fib(3) == 2
#  Verifying that fib(4) == 3
#  Verifying that fib(5) == 5
#  Negative values
#  Verifying that fib(-6) == -8
#  Verifying that fib(-96) == -51680708854858323072
#  Verifying that fib(-26) == -121393
#  Verifying that fib(-34) == -5702887
#  Verifying that fib(-88) == -1100087778366101931
#  Verifying that fib(-83) == 99194853094755497
# -99194853094755497 should equal 99194853094755497
#  Verifying that fib(-77) == 5527939700884757
# -5527939700884757 should equal 5527939700884757
#  Verifying that fib(-96) == -51680708854858323072
#  Verifying that fib(-31) == 1346269
# -1346269 should equal 1346269
#  Verifying that fib(-89) == 1779979416004714189
# -1779979416004714189 should equal 1779979416004714189
#  Verifying that fib(-89) == 1779979416004714189
# -1779979416004714189 should equal 1779979416004714189
#  Verifying that fib(-79) == 14472334024676221
# -14472334024676221 should equal 14472334024676221
#  Larger values
#  Verifying that fib(1000) is 4E208 and some change
#  Verifying that fib(1001) / fib(1000) is 'the golden ratio' (1 + sqrt(5)) / 2, up to floating point precision
#  Testing fib(11792)
#  Testing fib(1243240)