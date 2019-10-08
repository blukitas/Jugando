# You have to create a function that takes a positive integer number and returns the next bigger number formed by the same digits:

# 12 ==> 21
# 513 ==> 531
# 2017 ==> 2071
# If no bigger number can be composed using those digits, return -1:

# 9 ==> -1
# 111 ==> -1
# 531 ==> -1


def nextBigger(n):
    s = str(n)
    while 1:
        n += 1
        if n > int(''.join(sorted(s, reverse=True))):
            return -1
        if sorted(str(n)) == sorted(s):
            return n

print(nextBigger(9))
print(nextBigger(12))
print(nextBigger(21))
print(nextBigger(111))
print(nextBigger(513))
print(nextBigger(135))
print(nextBigger(2017))


# Solucion más votada:
# import itertools
# def next_bigger(n):
#     s = list(str(n))
#     for i in range(len(s)-2,-1,-1):
#         if s[i] < s[i+1]:
#             t = s[i:]
#             m = min(filter(lambda x: x>t[0], t))
#             t.remove(m)
#             t.sort()
#             s[i:] = [m] + t
#             return int("".join(s))
#     return -1

# Solución más creativa:
# def next_bigger(n):
#   n = str(n)[::-1]
#   try:
#     i = min(i+1 for i in range(len(n[:-1])) if n[i] > n[i+1])
#     j = n[:i].index(min([a for a in n[:i] if a > n[i]]))
#     return int(n[i+1::][::-1]+n[j]+''.join(sorted(n[j+1:i+1]+n[:j]))) 
#   except:
#     return -1