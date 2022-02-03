print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")


A=name1.lower()
B=name2.lower()
T=A.count("t") + B.count("t")
R=A.count("r") + B.count("r")
U=A.count("u") + B.count("u")
E=A.count("e") + B.count("e")

L=A.count("l") + B.count("l")
O=A.count("o") + B.count("o")
V=A.count("v") + B.count("v")

TrUe=(T+R+U+E)*10
Love=(L+O+V+E)
TrueLove=TrUe+Love
if TrueLove < 10 or TrueLove >90:
    print(f"Your score is {TrueLove},you go together like coke and mentos.")
elif TrueLove >=40 and TrueLove <= 50:
    print(f"Your score is {TrueLove}, you are alright together.")
else:
    print(f"Your score is {TrueLove}.")

