height = int(input("please enter height(in cm): "))
weight = int(input("please enter weight(in kg): "))
height=height/100
bki=weight/(height**2)
if bki<18.5:
    print("it is lightweight")
elif bki>=18.5 and bki<=25:
    print("it is normal")
elif bki>=25 and bki<=30:
    print("it is overweight")
else:
    print("it is obese")
