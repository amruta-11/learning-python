
LineName = ["line1", "line2","line3", "line4"]
eg1File = open("C:\Data\Amruta\Python Example\Eg1.txt", "a")
for name in LineName:
    eg1File.write(name + "\n")

eg1File.close()

eg1File = open("C:\Data\Amruta\Python Example\Eg1.txt", "r")
print(eg1File.read())


