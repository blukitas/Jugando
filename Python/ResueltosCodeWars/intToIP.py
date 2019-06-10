# Take the following IPv4 address: 128.32.10.1
# This address has 4 octets where each octet is a single byte (or 8 bits).
#   1st octet 128 has the binary representation: 10000000
#   2nd octet 32 has the binary representation: 00100000
#   3rd octet 10 has the binary representation: 00001010
#   4th octet 1 has the binary representation: 00000001
# So 128.32.10.1 == 10000000.00100000.00001010.00000001
# Because the above IP address has 32 bits, we can represent it as the unsigned 32 bit number: 2149583361

# Complete the function that takes an unsigned 32 bit number and returns a string representation of its IPv4 address.
# Examples
#   2149583361 ==> "128.32.10.1"
#   32         ==> "0.0.0.32"
#   0          ==> "0.0.0.0"
# https://www.codewars.com/kata/int32-to-ipv4/train/python


def int32_to_ip(i):    
    b = bin(i)
    nums = []
    i = len(str(b))
    variacion = 8
    while i > 2:
        # print(i, i-variacion, variacion)
        # print(nums)
        # print(b[i-variacion:i])
        nums.append(int(b[i-variacion:i], 2))
        i -= 8
        if ( 2 < i < 10):
            variacion = i-2
    nums += [0, 0, 0, 0]
    salida = ''
    for i in range(0, 4):
        salida = str(nums[i]) + '.' + salida

    return salida[:-1]

print(int32_to_ip(2149583361))  #|# 128.32.10.1
print(int32_to_ip(1739988596))  #|# 103.182.30.116
print(int32_to_ip(5045066))  #|# 0.76.251.74

# Mejor solucion:
# return '{}.{}.{}.{}'.format(*int32.to_bytes(4, 'big'))
