# # x, y之间所有的整数和
# my_sum = lambda x, y : (x + y) * (abs(x - y) + 1) // 2   
# print(my_sum(1, 100))	# 5050

# # 求字符串每个单词的长度
# sentence = "Welcome To Beijing!"
# words = sentence.split()
# lengths  = map(lambda x:len(x),words)
# print(list(lengths))	# [7,2,8]


# # 有参数，无返回值
# def print_stu_info(stu):
#     print('Name:', stu['name'], 
#           '\nClass:', stu['class'],
#           '\nGender:', stu['gender'])

# stu1 = {'name': 'ws', 'class': '2', 'gender': 'male', 'age': 23}
# stu2 = {'name': 'th', 'class': '2', 'gender': 'female', 'age': 22}
# print_stu_info(stu1)    # 调用函数
# print_stu_info(stu2)

# # 有参数，有返回值
# def _max(var1, var2):
#     if var1 > var2:
#         return var1
#     else:
#         return var2
# a = 4
# b = 5
# print(_max(var2=a, var1=b))    # 调用函数


# 函数有默认值，有默认值的参数必须在参数列表的最后
def print_info(name, age=35, gender="male"):
   "打印任何传入的字符串"
   print("名字: ", name)
   print("年龄: ", age)

# def print_info(age=35, name):	# 则不合法

# print_info("John", 10) # 合法
# print_info(age=10, name="John") # 不合法
# print_info(age=10)


# 求所有参数的和
# def sum(a=0, *args):
#    sums = a
#    for value in args:
#        sums += value
#    return sums

# print(sum(1, 2, 3))


# def printinfo( arg1, **vardict ):
#    # 打印任何传入的参数
#    vardict['arg1'] = arg1
#    print (vardict)

# printinfo(1, a=2,b=3)


# 求字符串每个单词的长度

sentence = "Welcome To Beijing!"
words = sentence.split()
lengths  = map(len, words)  # 将一个集合映射成另一个集合
print(list(lengths))	# [7,2,8]