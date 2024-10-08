### python基本语法

```python
# [这是注释] 定义一个阶乘的函数，接受参数n
def factorial(n):
    result = 1                # 初始化结果为1
    for i in range(2, n+1):   # i从2开始，一直到n循环
        result = result * i   # 累乘
    return result             # 返回结果

res = factorial(5)            # 调用函数，并赋值给res
print(res)                    # 打印结果为 120
```

#### 1.函数

? ← `函数名(参数1, 参数2, ...)`

* 内置函数：系统自带的函数，如 `print(...)`
* 自定义函数：用户自定义的函数，如 `factorial(...)`

#### 2.变量

简单理解为**等号左边的东西**，也就是我们要把一个“值”赋予谁，下次直接拿它来操作，例如result

###### 变量名（标识符）

* 所有标识符可以包括英文、数字以及下划线( _ )，但不能以数字开头，区分大小写，且不能包含系统已定义的标识符（例如函数名）

  * 合法：     `avg_price = 5.6`   ||   `BobEnglishGrade = 59`   ||    `_ = "下划线"`
  * 不合法：`2024_price = 5.6`   ||   `print = [1,2,3]`           ||    `my-age = 23`

###### 变量类型

| 名称   | 表示                                           | 示例                                                                                                                                | 说明                                                                                               |
| ------ | ---------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| 数字   | `int`, `long`, `float`,<br />`complex` | `x = 10`<br />`y = 10.14`                                                                                                       | 不需要指定类型                                                                                     |
| 字符串 | `str`                                        | `x = "hello"; y = 'hhh'`<br />`z = "这是双引号：\""`<br />`s = 'he' + 'llo'  # hello`<br />`s = 'th' * 3      # ththth` | 单引号和双引号均可<br />特殊符号用反斜杠转义<br />支持加法，表示合并<br />支持乘整数，表示复制几份 |
| 列表   | `list`                                       | `x = [2, 3, 5]`<br />`y = ['ws', 'th', 5, [2, 'hhh']]`<br />`z = y[2]    # 即 z = 5`                                        | 中括号，任何类型，可嵌套<br />用中括号访问其中的元素<br />下标从0开始                              |
| 元组   | `tuple`                                      | `x = (1, 2, 'hhh')`                                                                                                               | 只读的list                                                                                         |
| 字典   | `dict`                                       | `x = {'one': 1, 2: 'two', 'ws': 'th'}`<br />`y = x['ws']   # 即 y = 'th'`                                                     | key: value的键值对<br />利用中括号和key访问value                                                   |
| 布尔   | `bool`                                       | `True or False`                                                                                                                   |                                                                                                    |

#### 3.保留字

* 保留字不能用作常数或变数，或任何其他标识符名称
* 所有 Python 的关键字只包含小写字母。

| and      | exec    | not    |
| -------- | ------- | ------ |
| assert   | finally | or     |
| break    | for     | pass   |
| class    | from    | print  |
| continue | global  | raise  |
| def      | if      | return |
| del      | import  | try    |
| elif     | in      | while  |
| else     | is      | with   |
| except   | lambda  | yield  |

#### 4.注释

方便自己/团队读懂代码，也可注释掉无用的代码。

注意：python代码中一切有用的代码都是英文字符，不包含中文和中文符号、标点等。例如：这是 `;` 对的，这是 `；` 错的。但注释和字符串中任何字符都可以包含。

* 单行注释：用 `#` 开头
* 多行注释：用三个单引号 **`'''`** 或三个双引号 **`"""`** 包围起来
* Python里单引号和双引号是完全等效的

```python
# 定义名字name
name = "ws" # 这里的内容是一个注释
"""这里可以写注释
这里也是多行注释，不会执行'''
"""
'''这里也是注释'''
```

#### 5.空白字符（空格、空行、缩进）

* 空格：不是python的语法，用于分隔单词（单词与符号不必要用空格）
* 空行：空行用于分隔两段不同功能或含义的代码，表示一段新的代码的开始
* 缩进
  * 是python的语法，缩进里的代码表示归属于同一个模块，一般以冒号 `:` 开始，循环或控制语句
  * 缩进的空白数量是可变的，但所有代码块语句必须包含相同的缩进空白数量（一般按一个tab键就是）

```python
if 'ws' > 'th':
    print ("ws是老大！")
elif 'ws' == 'th':
    print ("ws和th一样！")
else:
    print ("th是老大！")

# 对结果思考：为什么？
```

#### 6.多行语句、单行语句

为了美化代码，不至于某些语句太长或太短

* 多行语句 -> 单行

  * python使用空行表示新的一段代码，可以用反斜杠 `\` 将一行的语句分为多行显示
  * 语句中包含 `[]` `{}` `()` 括号就不需要使用多行连接符

  ```python
  total = item_one + \
          item_two + \
          item_three

  weekdays = ['Monday', 'Tuesday', 'Wednesday',
              'Thursday', 'Friday']
  ```
* 单行语句 -> 多行

  * 使用 `;` 替代换行

```python
x = 'ws'; y = 'th'; print(x, 'misses', y)
```

#### 7.输入输出

```python
# 等待用户输入，并提醒括号中的话
x = int(input('请输入一个正整数'))   # 输入的都是字符串格式
# 输出，其中括号里的参数会分别输出，且以空格分开，最后加个回车
print(x, '的阶乘是：', factorial(x))
```
