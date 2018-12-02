#00P-Python面向对象
-面向对象编程
    -基础
    -公有私有
    -继承
    -组合，Mixin
-魔法函数
    -魔法函数概述
    -构造类魔法函数
    -运算类魔法函数
#1 面向对象概述 （ObjectOriented  00）
-OOP思想
    -接触到任意一个任务,首先想到的是任务这个世界的构成，是由模型构成的
    -几个名词
        -OO:面向对象
        -OOA：面向对象的分析
        -OOD：面向对象的设计
        -OOI：xxx的实现
        -OOP：xxx的编程
        -OOA->OOD->OOI：面向对象的实现过程
#2.类和对象的概念
    -类：抽象名词，代表一个集合，共性的事物
    -对象：具象的事物，单个个体
    -类跟对象的关系
        -一个具象，代表一类事物的某一个个体
        -一个是抽象，代表的是一大类事物
    -类中的内容，应该具有俩个内容
        -表明事物的特征，叫做属性（变量）
        -表明事物功能或动作，称为成员方法（函数）
#2.类的基本实现
    -类的命名
        -遵守变量命名的规范
        -大驼峰（由一个或者对个单词构成，每个单词首字母大写，单词跟单词直接相连）
        -尽量避开跟系统命名相似的命名
    -如何声明一个类
        -必须用class关键字
        -类由属性和方法构成，其他不允许出现
        -成员属性定义可以直接使用变量赋值，如果没有值，允许用None
        -案例01.py
-实例化类
        变量 = 类名（）#实例化了一个对象
-访问对象成员
    -使用点操作符
    obj.成员属性名称
    obj.成员方法
-可以通过默认内置变量检查类和对象的所有成员
    -对象所有成员检查
        #dict前后各有俩个下划线
        obj.__dict__
    -类所有的成员
        #dict前后各有俩个下划线
        class_name.__dict__
,,,
定义一个学生类，用来形容学生
,,,
#class Student():
    #一个空类，pass代表直接跳过
    #此处pass必须有
    pass
#定义一个对象
mingyue = Student()
#在定义一个类，用来描述听python 的学生
class PythonStudent():
    #用None 给不确定的值赋值
    name = None
    age = 18
    course = "Python"
    #需要注意
    #1.def dohomework 的缩进层数
    #2. 系统默认由一个self参数
    def dohomework(self):
        print("i 在做作业")
        #推荐使用函数末尾使用return语句
        return None
#实例化一个叫yueyue 的学生，是一个具体的人
yueyue = PythonStudent()
print(yueyue.name)
print(yueyue.age)
#注意成员函数的调用没有传递进入参数
yueyue.dohomework()
#3.anaconda基本使用
-anaconda主要是一个虚拟环境管理器
-还是一个安装包管理器
-conda list:显示anaconda安装的包
-conda env list：显示anconda 的虚拟环境列表
-conda create -n xxx python = 3.6:创建python版本为3.6的虚拟环境，名称为xxx
