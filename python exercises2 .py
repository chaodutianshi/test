# 学生信息管理系统
allStuList = []
while True:
    pwd = input("请输入密码:")
    if pwd != 'good':
        pass
    else:
        while True:
            print("=========欢迎使用========")
            print("当前学生总数:", len(allStuList))
            print("1.学生添加")
            print("2.学生退学")
            print("3.学生信息更改")
            print("4.显示所有学生")
            

            choice = int(input("请输入菜单编号:"))
            if choice == 1:
                stuId = input("请输入学生学号:")
                stuName = input("请输入学生姓名:")
                oneStuInfo = dict()  # 定义一个字典、映射结构
                oneStuInfo["id"] = stuId
                oneStuInfo["name"] = stuName
                allStuList.append(oneStuInfo)
            elif choice == 2:
                del_id = input("输入要退学的学号:")
                flag = -1
                for num in range(len(allStuList)):
                    if allStuList[num]['id'] == del_id:
                        flag = num
                        print("找到了")
                        break
                print("flag=", flag)
                del allStuList[flag]
                if flag == -1:
                    print("查无此人，请再试")
                else:
                    print("删除成功")
            elif choice == 3:
                update_id = input("输入要修改信息的学生编号:")
                update_name = input("输入修改后的学生姓名")
                flag = 1
                for stu in allStuList:
                    if update_id == stu['id']:
                        stu['name'] = update_name
                        flag = 0
                if flag == 1:
                    print("查无此人，请再试")
                else:
                    print("修改成功")
            elif choice == 4:
                print("===========================================================")
                print("序号\t\t\t学号\t\t\t姓名")
                for num in range(len(allStuList)):
                    print(num+1, "\t\t\t", allStuList[num]['id'], "\t\t\t",allStuList[num]['name'])
                print("===========================================================")
            else:
                print("输入错误")
                
                
 
