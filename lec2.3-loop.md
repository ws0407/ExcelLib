### 循环语句

#### `for` 和 `while`

```python
# 利用循环打印一个高为5的等腰三角形
# 定义三角形的高度
height = 5

# 打印等边三角形
for i in range(height):
    # 打印空格
    for j in range(height - i - 1):
        print(" ", end="")
    # 打印星号
    for k in range(2 * i + 1):
        print("*", end="")
    # 换行
    print()


# 利用while循环打印一个倒立的等腰三角形
height = 5	# 定义三角形的高度
row = height	# 初始化行数
# 打印倒立的等边三角形
while row > 0:
    print(" " * (height - row), end="")		# 打印空格
    print("*" * (2 * row - 1))			# 打印星号
    row -= 1	# 递减行数
```

```python
list(range(3))		# [0, 1, 2]
list(range(1, 3))	# [1, 2]
list(range(1, 11, 3))	# [1, 4, 7, 10]
```

#### break 和 continue 语句

* `break`：跳出整个 `for`或 `while`循环
* `continue`：跳过当前循环块中的剩余语句，继续下一轮循环
* break和continue终止的都是当前的循环

```python
price, quantity = 0, 0		# 初始化
while True:
    # 输入商品价格和购买数量
    try:
        price = float(input("请输入商品价格："))
        quantity = int(input("请输入购买数量："))
        break
    except ValueError:
        print("输入错误，请重新输入！")
        continue

# 判断购买数量并计算销量
if price > 0 and quantity > 0:
    if quantity >= 10 and price > 50:	# 嵌套if
        discount_rate = 0.8 # 打八折
    elif quantity < 10 or (quantity >= 10 and price <= 50):
        discount_rate = 1   # 无折扣
else:
    print("输入错误！")
    exit()
 
total_sales = price * quantity * discount_rate
print("销量为：", total_sales)
```

#### try 和 except 语句

* 表示异常处理
* try: 你要测试的代码，可能报错的代码
* except: 发生异常会执行的代码，如果try里没有异常，这里不会执行。如果这里还有异常，报错

#### pass语句

非常不常用，表示啥也不做，占位使用

```python
for i in range(10):
    if i % 2 == 0:
        pass
    else:
        print(str(i) + '是奇数。')
```

#### 高阶——推导式

`if - else` 赋值语句

```python
price, quantity = 52.5, 12
discount_rate = 0.8 if price > 50 and quantity >= 10 else 1

# 等价于下面的语句
if price > 50 and quantity >= 10:
   discount_rate = 0.8
else:
   discount_rate = 1
```

`for` 语句

```python
L1 = [1, 2, 3, 4]
L2 = [item * 2 for item in L1]	# [2, 4, 6, 8]
```

`for - if` 语句

```python
L1 = range(10)
L2 = [item * 2 for item in L1 if item > 5]	# [12, 14, 16, 18]
L3 = [item if item % 2 == 0 else item + 1 for item in L1 if item < 5]	# [0, 2, 2, 4, 4]

words = {'你好': 'hello', '中国': 'China', '英语': 'English'}
# 把原来没有大写的单词全部变成大写，有大写字母的不要
lower_words = {k: v.upper() for k, v in words.items() if v == v.lower()}	#lower_words: {'你好': 'HELLO'}

# 嵌套
# 矩阵中所有元素乘3
matrix = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
array = [[item * 3 for item in array] for array in matrix]	# [[3, 6, 9, 12], ..., [39, 42, 45, 48]]
```

```
enumerate
```
