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