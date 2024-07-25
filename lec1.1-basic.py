"""
[这是注释] 定义一个阶乘的函数，接受一个整数参数n
"""
def factorial(n: int):
    result = 1                  # 初始化结果为1
    for i in range(2, n + 1):   # i从2开始，一直到n循环，左闭右开区间
        result = result * i     # 累乘
    return result               # 返回结果

def find_point():   
     return 1, 2

print(find_point())

for i in range(1, 11):
        print(i)

x = input('请输入一个正整数:')
if x.isdigit():
    x = int(x)
    res = factorial(x)              # 调用函数，并赋值给res
    print(res)                      # 打印结果为 120
else:
    print("输入格式错误")
