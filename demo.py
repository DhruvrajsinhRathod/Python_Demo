name = input("What is your name : ")
age = input(name + ", What is your age : ")
age = int(age)

if age>=18:
    print(name + ", You are adult!")

else:
    print(name + ", Wait for few more years!")