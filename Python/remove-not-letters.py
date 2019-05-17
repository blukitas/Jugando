# Let's assume we need "clean" strings. Clean means a string should only contain letters a-z, A-Z and spaces. We assume that there are no double spaces or line breaks.
# Write a function that takes a string and returns a string without the unnecessary characters.
# Examples
#   * remove_chars('.tree1')    ==> 'tree'
#   * remove_chars("that's a pie$ce o_f p#ie!")  ==> 'thats a piece of pie'
#   * remove_chars('john.dope@dopington.com')    ==> 'johndopedopingtoncom'
#   * remove_chars('my_list = ["a","b","c"]')    ==> 'mylist  abc'
#   * remove_chars('1 + 1 = 2')    ==> '    ' (string with 4 spaces)
#   * remove_chars("0123456789(.)+,|[]{}=@/~;^$'<>?-!*&:#%_")  ==> '' (empty string)
#   https://www.codewars.com/kata/59be6bdc4f98a8a9c700007d
import re


# print((x for x in cadena if re.match(r"[azAZ]", x)))

cadena = 'my_list = ["a","b","c"]'
salida = ''
for c in cadena:
    n = ord(c)
    if ord('a') <= n <= ord('z') or ord('A') <= n <= ord('Z') or n == ord(' '):
        salida += chr(n)
print salida