class people:
    # 定义基本属性
    name = ''
    # 定义私有属性，私有属性在类外部无法直接进行访问
    __weight = 0
    # 定义构造方法
    def __init__(self,n,a,w):   # self代表类的实例，而非类
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


def print_info(name, age=35, gender="male"):
   "打印任何传入的字符串"
   print("名字: ", name)
   print("年龄: ", age)
   print("性别: ", gender)