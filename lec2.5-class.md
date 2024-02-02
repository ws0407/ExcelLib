### 面向对象——类

```python
#类定义
class people:
    # 定义基本属性
    name = ''
    # 定义私有属性，私有属性在类外部无法直接进行访问
    __weight = 0
    # 定义构造方法
    def __init__(self,n,a,w):	# self代表类的实例，而非类
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("%s说：我%d岁，%.2f千克" % (self.name, self.age, self.__weight))
 
# 单继承示例
class student(people):
    grade = ''
    def __init__(self,n,a,w,g):
        # 调用父类的构函
        people.__init__(self,n,a,w)
        self.grade = g
    # 覆写父类的方法
    def speak(self):
        print("%s说: 我%d岁了，我在读%d年级" %(self.name, self.age, self.grade))
 
p = people('Tom',12,65)		# 实例化
p.speak()			# 调用方法
 
s = student('Jerry',10,60,3)
s.speak()

```

* 类，class
* 方法，def
* 方法重写，__xx.....
* 类变量（公有属性，私有属性，相当于public，private）
* 继承
  * 单继承
  * 多继承
* 实例化
  * 数据成员（类变量，实例变量）
  * 方法

#### 模块mudule

继承各种类和方法于文件之中，供所有可访问该文件的代码使用。

* 文件名：`utils.py`，包含 `student`类
* 导入：`import utils`，`from utils import *`
* 使用：`s = utils.student('Jerry',10,60,3)`，`s = student('Jerry',10,60,3)`

python内部集成了多个模块，包含多个类和方法，例如 `xlrd`库、`openpyxl`库、`pandas`库，可以处理 `Excel`数据。

###### 安装

`pip install xlrd`

###### 使用

```python
import xlrd
 
book = xlrd.open_workbook("myfile.xls")
print("当前excel文件工作表数量为 {0}".format(book.nsheets))
print("工作表名字为: {0}".format(book.sheet_names()))
 
# 获取第一张工作表
sh = book.sheet_by_index(0)
 
# 获取表的数量
print(book.nsheets)
 
# 当前工作表名, 总行数 总列数
print("{0} {1} {2}".format(sh.name, sh.nrows, sh.ncols))
 
# 单元 d30 数据为
print("Cell D30 is {0}".format(sh.cell_value(rowx=29, colx=3)))
 
# 获取所有行数据
for rx in range(sh.nrows):
  # rx 行
  print(sh.row(rx))
   
>>>  [text:'Camille Richardson', text:'2316 EVIAN CT', empty:'', empty:'', text:'DISTRICT HEIGHTS', text:'MD', text:'20747-1153', text:'US']  
 
# 获取所有行数据   
for rx in range(sh.nrows):
    print(sh.row_values(rx))
   
>>> ['Camille Richardson', '2316 EVIAN CT', '', '', 'DISTRICT HEIGHTS', 'MD', '20747-1153', 'US']
```
