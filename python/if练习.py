num1=int(input("请输入数字1："))
num2=int(input("请输入数字2："))
op=input("请刷入想要做的运算:(平方1/四次方2)")
if op=="1":
    x=num1**2 + num2**2
    print(x)
elif op=="2":
    x=num1**4 + num2**4
    print(x)
else:
    print("请输入正确的数字或者运算规则")
