import functools
nums=[1,5,6,7,8]
sq_nums=list(map(lambda x:x*x, nums))
print(sq_nums)

# filter
fil_nums=list(filter(lambda x:x%2==0,nums))
print(fil_nums)

# reduce
sums=functools.reduce(lambda x,y:x+y, nums)
print(sums)


