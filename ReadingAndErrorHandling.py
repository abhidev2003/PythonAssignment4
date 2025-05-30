
filename=input("Enter file name")
file =None
try:
    file = open(filename,'r')
    reader = file.read()
    print(reader)
except FileNotFoundError:
    print(f'{filename} not found')
finally:
    print("Reading completed")
    if file:
        file.close()