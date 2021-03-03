#It's a guess game of entering the predefined right number. You have limited number of chances

n=18

print("You have 10 attempts!")

for x in range(10):
    a = int(input("Enter a number:"))
    if (0<a< n):
        print("You entered less!")
    elif (a > n):
        print("You entered more!")
    elif (a <= 0):
        print("Boom!\nNegative numbers and zero are not allowed")
    else:
        print("Congrats you entered the right number!")
        print("You took",x+1, "chances")
        exit(1)

    if x < 9:
        print("You are left with",9-x,"chances")
        continue
    else:
        print("Game over!\n You used all of your chances")