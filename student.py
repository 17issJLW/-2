student_num=[]
student_name=[]
student_scores=[]
def main():
    while True:
        print("请输入操作的序号")
        print("1、录入信息  2、查找学生  3、查看排名   4、删除信息   5、退出系统")
        a=input("进行操作为： ")
        if a.isdigit():
            a=int(a)
        else:
            print("请输入正确序号！")
            continue
        if (a==1):
            Save()
            print("\n")
            continue
        elif a==2:
            Find()
            print("\n")
            continue
        elif a==3:
            Sort()
            print("\n")
            continue
        elif a==4:
            Del()
            continue
        elif a==5:
            break
        else:
            print("输入出错，请重新输入序号")
            print("\n")
            continue


def Save():
    num = int(input("请输入学生学号： "))
    name = input("请输入学生名字： ")
    scores = int(input("请输入学生成绩： "))
    student_num.append(num)
    student_name.append(name)
    student_scores.append(scores)
    print("学生信息录入成功")


def Sort():
    for i in range(0,len(student_scores)):
        for a in range(0,len(student_scores)-1):
            if student_scores[a]<student_scores[a+1]:
                student_scores[a],student_scores[a+1] = student_scores[a+1],student_scores[a]
                student_name[a],student_name[a+1] = student_name[a+1],student_name[a]
                student_num[a],student_num[a+1] = student_num[a+1],student_num[a]
    print("排名 学号 姓名 成绩")
    for j in range(0,len(student_scores)):
        print(j+1,"  ",student_num[j]," ",student_name[j]," ",student_scores[j])

def Del():
    num = int(input("请输入要删除学生的学号： "))
    for i in student_num:
        if i == num:
            k = student_num.index(num)
            student_num.remove(num)
            student_name.remove(student_name[k])
            student_scores.remove(student_scores[k])
            print("学生信息已删除")
            print("\n")
        else:
            print("未找到该学生")

def Find():
    num = int(input("请输入要查看学生的学号： "))
    for i in student_num:
        if i == num:
            k = student_num.index(num)
            print("该学生学号为：",num)
            print("该学生姓名为：",student_name[k])
            print("该学生成绩为：",student_scores[k])




main()