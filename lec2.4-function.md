### 函数

函数是组织好的，可重复使用的，用来实现单一，或相关联功能的代码段。

函数能提高应用的模块性，和代码的重复利用率。py内部有很多内置函数，例如`print()`，用户也可根据代码需要，自定义函数。

#### 函数定义

```python
def 函数名(参数1, 参数2, ...):
    功能语句
    return xx   # 返回值，也可无返回值
```

```python
# 有参数，无返回值
def print_stu_info(stu):
    print('Name:', stu['name'], 
          '\nClass:', stu['class'],
          '\nGender:', stu['gender'])

stu1 = {'name': 'ws', 'class': '2', 'gender': 'male', 'age': 23}
print_stu_info(stu1)    # 调用函数
```

```python
# 有参数，有返回值
def _max(var1, var2):
    if var1 > var2:
        return var1
    else:
        return var2
a = 4
b = 5
print(_max(var1=a, var2=b))    # 调用函数
```

```python
# 函数有默认值，有默认值的参数必须在参数列表的最后
def print_info(name, age=35):
   "打印任何传入的字符串"
   print("名字: ", name)
   print("年龄: ", age)

# def print_info(age=35, name):	则不合法

# print(age=10, name="John") 合法
# print(age=10, "John") 不合法
```

```python
# 不定长参数

def printinfo( arg1, **vardict ):
   # 打印任何传入的参数
   vardict['arg1'] = arg1
   print (vardict)

printinfo(1, a=2,b=3)

# 加了两个星号 ** 的参数会以字典的形式导入，单个 * 是元组形式
# 如果没有传入多余的参数，则为空字典或空元组
```

```python
# 匿名函数 —— lambda表达式，可以写在一行，但不等同于 C 或 C++ 的内联函数

# x, y之间所有的整数和
my_sum = lambda x, y : (x + y) * (abs(x - y) + 1) // 2   
print(my_sum(1, 100))	# 5050

# 求字符串每个单词的长度
sentence = "Welcome To Beijing!"
words = sentence.split()
lengths  = map(lambda x:len(x),words)
print(list(lengths))	# [7,2,8]
```
