asc=0
bsc=0
for i in range(1,6):
    a= input("Enter ")
    b= input("Enter ")

    if((a=="stone" and b=="scissor")or(a=="paper" and b=="stone")or(a=="scissor" and b=="paper")):
        print("a wins the round")
        asc=asc+1
    elif((b=="stone" and a=="scissor")or(b=="paper" and a=="stone")or(b=="scissor" and a=="paper")):
        print("b wins the round")
        bsc=bsc+1
    else:
        print("round draw")
if(asc>bsc):
    print("a wins")
else:
    print("b wins")
