PLC = ["Winterfell", "Kings Landing", "Meereen"]
print (" This is a 3 player game. \n Please do not play with more than 3 people.")
print ("It is Winterfell's turn.")
WF_1 = input("What will Winterfell do: ")
if WF_1 == "stay":
    print ("Winterfell is at B2.")
elif WF_1 == "move":
    WF_1_MV = input("Which direction would you like to move in: ")
    if WF_1_MV == "up":
        print ("Winterfell is at A2.")
    elif WF_1_MV == "down":
        print ("Winterfell is at C2.")
    elif WF_1_MV == "left":
        print ("Winterfell is at B1.")
    elif WF_1_MV == "Right":
        print ("Winterfell is at B3.")
else:
    print ("Incorrect_Command.")
KL_1 = input("What will Kings Landing do: ")
if KL_1 == "stay":
    print ("Kings Landing is at E3.")
elif KL_1 == "move":
    KL_1_MV = input("Which direction would you like to move in: ")
    if KL_1_MV == "up":
        print ("Kings Landing is at A2.")
    elif KL_1_MV == "down":
        print ("Kings Landing is at C2.")
    elif KL_1_MV == "left":
        print ("Kings Landing is at B1.")
    elif KL_1_MV == "Right":
        print ("Kings Landing is at B3.")
else:
    print ("Incorrect_Command.")
MR_1 = input("What will Meereen do: ")
if MR_1 == "stay":
    print ("Meereen is at G5.")
elif MR_1 == "move":
    MR_1_MV = input("Which direction would you like to move in: ")
    if MR_1_MV == "up":
        print ("Meereen is at A2.")
    elif MR_1_MV == "down":
        print ("Meereen is at C2.")
    elif MR_1_MV == "left":
        print ("Meereen is at B1.")
    elif MR_1_MV == "Right":
        print ("Meereen is at B3.")
else:
    print ("Incorrect_Command.")
