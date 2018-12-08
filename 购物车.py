python购物车程序

数据结构：
goods = [
{"name": "电脑", "price": 1999},
{"name": "鼠标", "price": 10},
{"name": "游艇", "price": 20},
{"name": "美女", "price": 998},
......
]

功能要求：
基础要求：

1、启动程序后，输入用户名密码后，让用户输入工资，然后打印商品列表

2、允许用户根据商品编号购买商品

3、用户选择商品后，检测余额是否够，够就直接扣款，不够就提醒

4、可随时退出，退出时，打印已购买商品和余额

5、在用户使用过程中， 关键输出，如余额，商品已加入购物车等消息，需高亮显示


扩展需求：

1、用户下一次登录后，输入用户名密码，直接回到上次的状态，即上次消费的余额什么的还是那些，再次登录可继续购买

2、允许查询之前的消费记录

 1 #! -*- coding:utf-8 -*-
 2 # 购物车程序
 3 
 4 goods = [
 5     {"name": "电脑", "price": 1999},
 6     {"name": "鼠标", "price": 10},
 7     {"name": "游艇", "price": 20},
 8     {"name": "美女", "price": 998},
 9 ]
10 data = {}
11 while True:
12     username = input("用户名: ")
13     password = input("密码: ")
14     n = open("data.txt", "a+")  # 打开文件
15     n.seek(0, 0)
16     d = n.read()
17     n.close()
18     if d == "":
19         d += "{}"
20     data = eval(d)  # 字符串转字典
21     if username in data:  # 判断用户是否存在
22         if password == data[username][0]:  # 判断密码是否正确
23             wages_1 = data[username][1]  # 读取余额
24             print("登录成功!")
25             f = username + ".txt"
26             record = open(f, "a+")  # 打开消费记录文件
27             record.seek(0, 0)
28             consume = record.read()  # 消费记录
29             record.seek(0, 2)
30             break
31         else:
32             print("密码错误!")
33             enumerate
34     else:
35         wages = input("工资: ")
36         if wages.isdigit():
37             wages_1 = int(wages)  # 存放余额
38             data[username] = [password, wages_1]  # 添加用户信息,hex加密密码
39             f = username + ".txt"
40             record = open(f, "a+")  # 打开消费记录文件
41             consume = ""
42             break
43         else:
44             print("您输入的工资有误,请重新输入!")
45 
46 list_0 = []  # 存放所有商品
47 list_1 = []  # 存放已购买的商品
48 for info in goods:
49     list_0.append([info['name'], info['price']])  # 把商品信息添加到列表
50 while True:
51     print('-' * 7, " 商品列表 ", '-' * 7)
52     for index, p in enumerate(list_0):
53         print("%s.%s   %s" % (index, p[0], p[1]))  # 打印商品列表
54     print("请在下方输入商品编号,或 n 查看消费记录,或 q/Q 退出\n", '-' * 26)
55     select = input(">>> ")
56     if select == "q" or select == "Q" or select == "n":
57         if select == "n":
58             print('-' * 7, " 消费记录 ", '-' * 7)
59             print(consume)
60             break
61         else:
62             print('-' * 6, " 已购商品列表 ", '-' * 6)
63             for index_1, p_1 in enumerate(list_1):
64                 print("%s.%s   %s" % (index_1, p_1[0], p_1[1]))  # 打印已购商品列表
65                 c = p_1[0]
66                 consume += str(c)
67                 consume += "\n"
68             print("余额: ", wages_1, "\n", '-' * 26)
69             nn = open("data.txt", "w")
70             dd = str(data)  # 字典转字符串
71             nn.write(dd)
72             nn.close()  # 关闭文件
73             record.write(consume)  # 写入消费记录
74             consume = ""
75             record.close()
76             break
77     else:
78         if select.isdigit():  # 判断是否是数字
79             select = int(select)
80             if select <= 3:
81                 price = list_0[select][1]  # 以select为索引获取对应的商品价格
82                 if wages_1 >= price:  # 判断余额是否大于或等于商品价格
83                     wages_1 = wages_1 - price  # 扣钱
84                     list_1.append(list_0[select])  # 把购买的商品添加到已购商品列表
85                     data[username][1] = wages_1  # 修改余额
86                     print("购买成功!")
87                 else:
88                     print("余额不足!")
89             else:
90                 print("没有这个选项,请重新输入!")
91         else:
92             print("没有这个选项,请重新输入!")
--------------------- 
