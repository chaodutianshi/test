#给定一个整数数组和一个目标值，找出数组中和为目标值的俩位数
class Solution(object):
    def twoSum(self,nums,target):
        #type nums:List[int]
        #type target:int
        #type:List[int]
        d = {}
        for i, num in enumerate(nums):
            if target - num in d:
                return[d[target - num], i]
            d[num] = i
        #no special case handing becasue it is assumed that it has only one solution
        
        
        
        #给定一个32位有符号整数，将整数中的数字进行反转
#Reverse integer
class Solution(object):
    def reverse (self,x):
        #type x:int 
        #type x
        sign = x < 0 and -1 or 1
        x = abs(x)
        ans = 0
        while x:
            ans = ans*10 + x%10
            x/= 10
        return sign*ans if ans <= 0x7ffffff else 0

    
    #如果想表达出Let's go来
#1.可以使用嵌套引导，即外层使用双引号
#2.转义字符
s="Let's go"
print(s)
ss='Let\'s go'
print(ss)
sss="c:\\user"
print(sss)
#回车换行符
s1="i love \r\n eang"
print(s1)


#向大家问好
#所有的字母的首字母大写
print("Hello python people!".title())
#所有的字母都大写
print("hello python people!".upper())
#所有的字母都小写
print("hello python people!".lower())
#第一个单词使用制表符，后俩个单词进行换行，并且所有的单词的首字母都大写
print("\thello \npython \npeople!".title())


#使用列表中的值
bicycles = ['trek','cannondable','redline','specialized']
message = "my first bicycle was a ".title() + bicycles[2].title() + "."
print( message)


#修改列表中的元素
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
motorcycles[1] = 'ducati'
print(motorcycles)


# 在列表末尾添加元素
motorcycles = ['honda','yamaha','suzuki']
motorcycles.append('ducati')
print(motorcycles)


#从列表中删除元素
#使用del语句删除元素
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
del motorcycles[1]
print(motorcycles)


#使用方法pop（）删除元素
motorcycles =['honda','tamaha','suzuki']
print(motorcycles)
#将单个值存储到另一个列表中
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)


#根据具体值来制定删除
motorcycles = ['honda','yamaha','suzuki','ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)


motorcycles = ['honda','yamaha','suzuki','ducati']
print(motorcycles)
#将要删除的元素另存储到一个单元内，然后使用这个单元将此元素打印出来
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title()+ "is too expensive for me.")

# score 存放学生成绩
#注意input的返回值
score = input("请输入学生成绩")
#需要把str转换成int
score = int (score)

if score>=90:
    print("A")
if score>=80 and score<90:
    print("B")
if score>=70 and score<80:
    print("C")
if score>=60 and score<70:
    print("D")
if score<60:
    print("起开，我没你这学生")
    
    
    # input的作用是
# 1. 在屏幕上输出括号内的字符串
# 2. 接受用户输入的内容并返回到程序
# 3. input返回的内容一定是字符串类型
gender = input("请输入性别：")
print("你输入的性别是：{0}".format(gender))

if  gender == "nan":
    print("来，我们纪念一下今天吧，代码敲十遍")
else:
    print("发糖喽发糖喽")
    print("你是女生，特殊照顾喽")
        
print("开始上课喽")


#return语句的基本使用
def hello (person):
    print ("{0},你怎么了".format(person))
    print ("sir,你不理我我就走了")
    
    return "我已经跟{0}打招呼了，{1}不理我".format(person,person)
p = "明月"
rst = hello (p)
print(rst)


#九九乘法表
for row in range (1,10):
    #打印一行
    for col in range (1,row+1):
        #print函数默认打印完毕后自动换行
        print ( row * col, end=' ')
    print(" ")
        
    
    
    #count 计算制定数据出现的次数
t = (2,1,2,3,45,1,1,2)
print(t.count(2))
#index 求制定元素在元组中的索引位置
print(t.index(45))
#如果需要查找的数字是多个，则返回第一个
print(t.index(1))


#集合序列操作
#成员检测
#in ，not in
s = {4,5, "i","love","wangxiaojing"}
print(s)
if "love" in s:
    print("哎呀")
if "hah " not in s:
    print("锤子")
    
    
    #集合的内涵
#普通集合内涵
s = {23,223,545,3,1,2,3,4,3,2,3,1,2,4,3}
print(s)

ss = {i for i in s}
print(ss)

#带条件的集合内涵
sss = {i for i in s if i %2 == 0}
print(sss)
sss = {i for i in s if i %2 != 0}
print(sss)

#多循环的集合内涵
s1 = {1,2,3,4}
s2 = {"i","love","wangxiaojing"}
s = {m*n for m in s1 for n in s2}
print(s)

s = {m*n for m in s1 for n in s2 if n ==2}
print(s)


#集合函数
#intersection; 交集
#difference 差集
#union 并集
#issubset 检查一个集合是否为另一个子集
#issuperset 检查一个集合是否为另一个超集
s1 = {1,2,3,4,5,6}
s2 = {5,6,7,8,9,10}
s_1 = s1.intersection(s2)
print(s_1)
s_2 = s1.difference(s2)
print(s_2)



#成员检测 in ， not in
#成员检测检测的是key的内容
d = {"one":1, "two":2, "three":3}
if 2 in d:
    print("value")
if "two" in d:
    print("key")
if ("two",2) in d :
    print("kv")
    
    
    responses = { }
polling_active = True
while polling_active:
    name = input("\nWhat is your name? ")
    response = input("\nWhich mountion would you like to climb someday? ")
    responses[name] = response
    repeat = input ("\nWould you like to let another person response? (yes/no) ")
    if repeat == 'no':
        polling_active = False
print("\n--- Poll Results --- ")
for name, response in responses.items():
    print(name + "would like to climb " + response + ".")
    
    
    #收集参数
#把关键字格参数字典格式存入收集参数
#kwargs一般约定俗成
#访问kwargs需要按字典格式访问
def stu (**kwargs):
    print ("hello,大家好，我先自我介绍一下：")
    print (type(kwargs))
    for k,v in kwargs.items():
        print (k,"___",v)
        
stu (name = "liuying",age = 19,addr = "北京海淀区",over = "王晓静",work="teacher")
print ("*" * 50)
stu (name = "周大神")


def stu (name,age,*args,hobby="没有",**kwargs):
    print("Hello 大家好")
    print("我叫{0},我今年{1}大了 。".format(name,age))
    if hobby =="没有":
          print ("我没有爱好 so sorry")
    else:
          print ("我的爱好是{0}".format(hobby))
  
    print("*"*30)
    for i in args:
          print(i)
    print("*"*20)
    for k,v in kwargs.items():
          print (k,"___",v)
name ="liuying"
age =19
stu(name,age)
stu(name,age,hobby="游泳")
stu(name,age,"王晓静","刘石头",hobby="游泳",hobby2="烹饪",hobby3="跟不同女生聊天")


my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[ : ]
#俩个列表分别各添加一种食品（用添加元素法）
my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)


import random
import math
 
from pyneurgen.neuralnet import NeuralNet
from pyneurgen.nodes import BiasNode, Connection
 
pop_len = 360
factor = 1.0 / float(pop_len)
population = [
    (i, math.sin(float(i) * factor )) for i in range(pop_len)
]
 
all_inputs = []
all_targets = []
 
def population_gen(population):
    pop_sort = [item for item in population]
    random.shuffle(pop_sort)
    for item in pop_sort:
        yield item
 
#   Build the inputs
for position, target in population_gen(population):
    pos = float(position)
    all_inputs.append([random.random(), pos * factor])
    all_targets.append([target])
 
net = NeuralNet()
net.init_layers(2, [10], 1)
net.randomize_network()
net.learnrate = .20
 
net.randomize_network()
net.set_all_inputs(all_inputs)
net.set_all_targets(all_targets)
length = len(all_inputs)
 
learn_end_point = int(length * .8)
net.set_learn_range(0, learn_end_point)
net.set_test_range(learn_end_point + 1, length - 1)
net.layers[1].set_activation_type('tanh')
net.learn(epochs=125, show_epoch_results=True,random_testing=False)
mse = net.test()
 
import matplotlib
from pylab import plot, legend, subplot, grid
from pylab import xlabel, ylabel, show, title
 
test_positions = [item[0][1] * 1000.0 for item in net.get_test_data()]
 
all_targets1 = [item[0][0] for item in net.test_actuals_targets]
allactuals = [item[1][0] for item in net.test_actuals_targets]
 
#   This is quick and dirty, but it will show the results
subplot(3, 1, 1)
plot([i[1] for i in population])
title("Population")
grid(True)
 
subplot(3, 1, 2)
plot(test_positions, all_targets1, 'bo', label='targets')
plot(test_positions, allactuals, 'ro', label='actuals')
grid(True)
legend(loc='lower left', numpoints=1)
title("Test Target Points vs Actual Points")
 
subplot(3, 1, 3)
plot(range(1, len(net.accum_mse) + 1, 1), net.accum_mse)
xlabel('epochs')
ylabel('mean squared error')
grid(True)
title("Mean Squared Error by Epoch")
 
show()


#传值和传地址的区别
#对于简单的数值，采用传值操作，即在函数内对参数的操作不影响外面的变量
#对于复杂变量，采用传地址变量，此时函数内的参数和外部变量是同一份内容，任何地方对此内容的更改都影响另外的变量或参数的使用
def a (n):
    n[2] = 300
    print(n)
    return None
def b (n):
    n +=100
    print (n)
    return None
an = [1,2,3,4,5,6]
bn = 9
print (an)
a (an)
print (an)
print (bn)
b (bn)
print (bn)


#remove 在列表中删除指定的值的元素
#如果被删除的值没在list中，则报错
#即，删除list 指定值的操作应该使用try...excepty语句，或者先行进行判断‘
# if x in list:
#    list.remove(x)
a.insert(4,666)
print(a)

a.remove(666)
print(a)
print(id(a))
#输出俩个id值一样，说明remove操作是在原list直接操作


#序列相加
t1 = (1,2,3)
t2 = (5,6,7)
#传址操作
print(t1)
print(id(t1))
t1 = t1 + t2
print(t1)
print(id(t1))
#以上操作类似于
t1 = (1,2,3)
t2 = (5,6,7)
#tuple 的不可修改，指的是内容的不可修改
#修改的tuple内容会导致报错
ti[1] = 100





