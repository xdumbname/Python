def write_file():

    with open("file.txt", "a") as w_file:
        w_file.write("Hello World!\n")
        w_file.write("Hello World!")
    
with open("file.txt", "r") as r_file:
    # Method 1
    for line in r_file:
        print(line)

    # Method 2 
    print(r_file.readline())

    # Method 3
    print(r_file.readlines())
