# regular dict
nums=[1,2,3,4,5,6]
nums2={}

for i in nums:
    if i % 2==0:
        nums2[i]="Even"
    else:
        nums2[i]="Odd"

print(nums2)

# dict comprehension
result={i:"Even" if i % 2==0 else "Odd" for i in nums}
print(result)