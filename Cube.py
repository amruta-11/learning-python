def cube(num:int):
    x = range(1, num+1)
    for i in x:
        b = i*i*i
        print("cube of", i, "is", b)
    print("Done printing all the cubes")

cube(10)