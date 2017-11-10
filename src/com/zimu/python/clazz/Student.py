# class后面紧接着是类名，(object)表示该类是从哪个类继承下来的
class Student(object):      # 注意：特殊方法“init”前后有两个下划线！！！
    def __init__(self, name, score):    # 通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属性绑上去
        self.name = name
        self.score = score

stu = Student("Jack",90)    # self不需要传，Python解释器自己会把实例变量传进去
print(stu.name)
print(stu.score)
print('%s: %s' % (stu.name, stu.score))

# stu2 = Student()
# stu2.name = "Bob"
# stu2.score = "80"
# print(stu2.name)
# print(stu2.score)