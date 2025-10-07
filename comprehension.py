b=[1,2,3,4,5,6]

s_result=[item ** 2 for item in b if item%2==0]
print(s_result)

ss_result=[item**2 if item %2==0 else item for item in b]
print(ss_result)