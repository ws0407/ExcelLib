"""
[这是注释] 定义一个阶乘的函数，接受一个整数参数n
"""
def factorial(n):
    result = 1                  # 初始化结果为1
    for i in range(2, n + 1):   # i从2开始，一直到n循环
        result = result * i     # 累乘
    return result               # 返回结果


res = factorial(5)              # 调用函数，并赋值给res
print(res)                      # 打印结果为 120

