print("Your Average Grade")
print("Prelim Grade: ")
pre = int(input())
print("Midterm Grade: ")
mid = int(input())
print("Semi Final Grade: ")
semi = int(input())
print("Final Grade: ")
fin = int(input())

total= pre+mid+semi+fin
ave= int(total/4)

print("Your Average is {}".format(ave))

if ave >= 75:
    print("You Passed :D")
else:
    print("You Failed :(")

if ave >= 99 <=100:
    print("Your Mark is A")
elif ave >=90 <=99:
    print("Your Mark is B")
elif ave >=80 <=89:
    print("Your Mark is C")
elif ave >=71 <=79:
    print("Your Mark is D")
elif ave >=61 <=70:
    print("Your Mark is E")
elif ave >= 60:
    print("Your Mark is F")
else:
    print("Invalid Input")


