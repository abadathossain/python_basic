try:
    with open("data.csv") as f:
     print(f.read())
     x=[1,2,3,4]
    print(x[100])
except FileNotFoundError:
   print("Not found")
except IndexError:
   print("Invalid Index")
except Exception as e:
   print("Custom Error",e)