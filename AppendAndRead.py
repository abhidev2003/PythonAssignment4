filename=input("Enter file name")

file = open(filename,'a')
text = input("Enter text to write to the file")
writer = file.write(text+"\n")
print(f"Data Successfully Written to {filename}/n")

text1 = input("Enter Additional text to append")
writer1 = file.write(text1+"\n")
file.close()

file = open(filename,'r')
read = file.read()
print(f"Final content of {filename}:")
print(read)