# Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contains any char.
#
# Examples input/output:
#
# XO("ooxx") => true
# XO("xooxx") => false
# XO("ooxXm") => true
# XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
# XO("zzoo") => false

# original answer:
# def xo(s):
#     s = s.lower()
#
#     if s.count('o') == s.count('x'):
#         return True
#     else:
#         return False

# New Answer:
# since it's a logical, I don't need to state the output.
def xo(s):
    s = s.lower()
    return s.count('o') == s.count('x')

xo("ooxx")
xo("ooxx")
xo("xooxx")
xo("ooxXm")
xo("zpzpzpp")
xo("zzoo")
