b=[1,2,3,4,5,6]

result=[]
for i in b:
    if i % 2==0:
        i=i*3
        result.append(i)      
print(result)




s_result=[item ** 2 for item in b if item%2==0]
print(s_result)

ss_result=[item**2 if item %2==0 else item for item in b]
print(ss_result)





