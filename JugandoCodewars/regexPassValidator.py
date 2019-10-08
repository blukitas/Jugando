# You need to write regex that will validate a password to make sure it meets the following criteria:

# At least six characters long
# contains a lowercase letter
# contains an uppercase letter
# contains a number
# Valid passwords will only be alphanumeric characters.

def regpass(p):
    return len(p) > 5 and p != p.lower() and p.isalnum() and not p.isalpha()

print(regpass('a'))
print(regpass('aB'))
print(regpass('aaaaaaaa'))
print(regpass('aBdCfG'))
print(regpass('AbCdE56'))
print(regpass('666666666'))

#python regex