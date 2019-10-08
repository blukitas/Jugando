# Write a function that takes a positive integer and returns the next smaller positive integer containing the same digits.

# For example:

# next_smaller(21) == 12
# next_smaller(531) == 513
# next_smaller(2071) == 2017
# Return -1 (for Haskell: return Nothing), when there is no smaller number that contains the same digits. Also return -1 when the next smaller number with the same digits would require the leading digit to be zero.

# next_smaller(9) == -1
# next_smaller(135) == -1
# next_smaller(1027) == -1  # 0721 is out since we don't write numbers with leading zeros
# some tests will include very large numbers.
# test data only employs positive integers.
# The function you write for this challenge is the inverse of this kata: "Next bigger number with the same digits."


def nextSmaller(n):
    s = str(n)
    so = sorted(s)
    iso = int(''.join(so))
    while n > iso:
        n -= 1
        if sorted(str(n)) == so:
            return n
    return -1

    # if sorted(str(n)) == sorted(s):
    #     return n
    # if n < int(''.join(sorted(s))):
    #     return -1
    # return n


print(nextSmaller(907))
print(nextSmaller(531))
print(nextSmaller(135))
print(nextSmaller(2071))
print(nextSmaller(414))
print(nextSmaller(123456798))
print(nextSmaller(123456789))
print(nextSmaller(1234567908))
print(nextSmaller(1999999999))