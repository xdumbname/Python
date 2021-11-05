wins = 0
count = 1
while count <= 6:
    x = input()
    if x != "W" and x != "L":
        print ("Not able to read")
    if x == "W":
        wins = wins + 1
    count += 1

if wins == 5 or wins == 6:
    print ("1")
elif wins == 3 or wins == 4:
    print ("2")
elif wins == 1 or wins == 2:
    print ("3")
else:
    print ("-1")