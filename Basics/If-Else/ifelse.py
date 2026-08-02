# if-else

email = input("Enter email = ")
paswd = input("Enter paswd = ")

if email == "saitanmy19@gmail.com" and paswd == 1234:
    print("welcome")

elif email == "saitanmy19@gmail.com" and paswd != 1234:
    print("Wrong paswd")
    paswd = input("Enter paswd again")
    if paswd == "1234":
        print("welcome finally!")
    else:
        print("u aint gonna make it happen")
else:
    print("Not correct")
