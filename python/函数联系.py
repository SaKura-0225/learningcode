def avg(*num):
    sum=0
    for i in num:
        sum += i
    else:
        return sum/len(num)
    
# x=eval(input("请输入要求平均值的数字，用逗号分隔:"))     #input收入为字符串，eval可以相当于将输入字符串的”“去掉变成其他类型   ”12，3，2“   ===    12 ，3，2
# print(avg(*x))
    
print(avg(3,4))