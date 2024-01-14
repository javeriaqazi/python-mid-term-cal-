("""addition
  substraction
  multiplication
  division""")

num1=int(input("enter the value of num1"))
num2=int(input("enter the value of num2"))
print("""addition +
substraction -
multiplication *
division /""")
opr=input("enter the opr...")

if opr =="+":
    print(num1+num2)
elif opr =="-":
    print(num1-num2)
elif opr =="*":
    print(num1*num2)
elif opr =="/":
    print(num1/num2)
else :
    print("invalid error")
