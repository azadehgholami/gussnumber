import random
number=random.randint(1,11)
count=0
while count<5:
    count += 1
    user_rand=int(input("your gusse"))
    if user_rand<number:
        print("number is bigger")
        print(count)
    elif user_rand>number:
        print("number is lower")
        print(count)
    elif user_rand==number:
        break

print("number",number,"you win")



