try:
    with open("data.csv") as f:
     print(f.read())
except FileNotFoundError:
   print("Not found")