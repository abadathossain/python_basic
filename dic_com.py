a=list(range(0,11))
# print(a)

# result=[]
# for i in a:
    # print(i)

#     result.append(i)

# print(result)

result=[i for i in a]
# print(result)

result1= {i:"Even" if i%2==0 else "Odd" for i in a}
# print(result1)



student = {
    "name": "Rahim",
    "age": 21,
    "department": "Physics"
}

for i in student.keys():
    print(i)

for item in student.values():
    print(item)

for k,v in student.items():
    print(k,v)
    print(f"{k},{v}")
