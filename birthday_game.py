secret_day=18
while True:
   your_estimate=int(input("please enter your estimated day:"))
   if your_estimate < secret_day:
    print("your estimate is too low")
   elif your_estimate > secret_day:
    print("your estimate is too high")
   else:
    print("your estimate is ok")
    break