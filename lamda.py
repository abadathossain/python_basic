def square(x):
    return x*x
result=square(4)
# print(result)


square=lambda x: x*x
# print(square(5))


students=[("A",50),("B",30),("C",60)]
sort_std=sorted(students, key=lambda x:x[1])
# print(sort_std)

addition=lambda a,b:a+b
# print(addition(4,5))
res=addition(4,5)
print(res)
