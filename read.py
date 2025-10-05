file=open("read.txt", "r")
content=file.read()
print(content)
file.close()

# another option
with open("read.txt", "r") as f:
    content1=f.read()
    print(content1)