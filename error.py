try:
    with open("rea.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("Not found")