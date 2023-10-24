#인스턴스 객체를 생성
account1 = BankAccount(100, "전우치", 15000)
account1.deposit(5000)
account1.withdraw(3000)
account1.balance = 15000000
print(account1)

#읽기
print(account1.__balance)

#부모클래스
class Person(object):
    def __init__(self, name, phoneNmber)
        self.name = name
        self.phoneNumber = phoneNmber
    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(self.name, self,phoneNumber))
    def working(self):
        print("현재 작업중")
    def sleeping(self):
        print("현재 수면중")      

#자식클래스
class Student(Person):
    #초기화 메서드 덮어쓰기(재정의, override)
    def __init__(self, name, phoneNmber, subject, studentID):
        Person.__init__(self, name, phoneNmber)
        self.subject = subject
        self.studentID = studentID
    #상속받은 메서드 덮어쓰기
    def printInfo(self):
        print("Info(name:{0}, Phone Number: {1})".format(self.name, self.phoneNumber))
        print("Info(학과:{0}, 학번:{1})".fornat(self.subject, selt.studentID))


#인스턴스
p = Person("전우치", "010-2445-8888")
s = Student()
p.printInfo
s.
s.working()
s.sleeping()