# a=[1,5,7,3]
# i=0
# result=0
# while i<len(a):
#     result=result+a[i]
#     i=i+1
# print(result)





li = [-10, 2, 5, 4, -3, 9]

i = 0
while i < len(li):
    if li[i] < 0:
        li[i] = 0
    i += 1  
print(li)


