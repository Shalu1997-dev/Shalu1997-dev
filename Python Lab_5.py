f =open("test1.txt", "r")
data = f.readline()
text =list(data.split(" "))
print(text)
