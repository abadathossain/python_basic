def check_file(fileName):
    if not fileName.endswith('.txt'):
        raise ValueError("only txt file")
    print("valid")

try:
    check_file('read.txt')
except Exception as err:
    print(err)