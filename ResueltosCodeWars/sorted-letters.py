# https://www.codewars.com/kata/two-to-one/python
# Take 2 strings s1 and s2 including only letters from ato z. Return a new sorted string, the longest possible, containing distinct letters,

# each taken only once - coming from s1 or s2.
# Examples:
#   a = "xyaabbbccccdefww"
#   b = "xxxxyyyyabklmopq"
#   longest(a, b) -> "abcdefklmopqwxy"

#   a = "abcdefghijklmnopqrstuvwxyz"
#   longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"

def longest(s1, s2):
    # your code
    distinct = set(s1+s2) # sets are distinct values! 
    distinctSorted = sorted(distinct) # turn into sorted list
    return ''.join(distinctSorted) # concatenate to string with 'join'