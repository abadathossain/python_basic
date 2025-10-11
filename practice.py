marks = int(input('Enter marks: ' ))
if marks >= 90:
    print('Marks = ',marks,'Grade = A+')
elif 80 <= marks <= 89:
    print('Marks = ',marks,'Grade = A')
elif 60 <= marks <= 79:
    print('Marks = ',marks,'Grade = B')
elif 50 <= marks <= 59:
    print('Marks = ',marks,'Grade = C')
elif 45 <= marks <= 49:
    print('Marks = ',marks,'Grade = D')
elif 25 <= marks <= 44:
    print('Marks = ',marks,'Grade = E')
else:
    print('Marks = ',marks,'Grade = F')