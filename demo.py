
s=['a','b']
for i, v in enumerate(s):
    s[i] = 'c'
print(s)


#
# s = "   abc   "
# while s[:1] == ' ':
#     s=s[1:]
#     print(-1)
# print(s)



# def f1(a,*,b):
#     print(b)
# f1(1,**{'b':1})