class Person:
    def __init__(self, id, phoneNumber):
        # Person 클래스의 생성자 메서드입니다.
        # id와 phoneNumber 매개변수를 받아 객체의 속성으로 설정합니다.
        self.id = id  #개인의 ID
        self.phoneNumber = phoneNumber #개인의 전화번호
    
    def printinfo(self):
        # 객체의 id와 phoneNumber을 출력하는 메서드입니다.
        print(f"ID: {self.id}")
        print(f"전화번호: {self.phoneNumber}")

class Manager(Person):
    def __init__(self, id, phoneNumber, skill):
        # Manager 클래스의 생성자 메서드입니다.
        # Person 클래스의 생성자를 호출하여 id와 phoneNumber를 설정하고,
        # skill 매개변수를 추가로 받아 객체의 속성으로 설정합니다.
        super().__init__(id, phoneNumber)
        self.skill = skill
    
    def printinfo(self):
        # Person 클래스의 printinfo 메서드를 호출하여 id와 phoneNumber 출력 후,
        # Manager 클래스의 skill을 출력합니다.
        super().printinfo()
        print(f"보유 기술: {self.skill}")

class Employee(Manager):
    def __init__(self, id, phoneNumber, skill, title):
        # Employee 클래스의 생성자 메서드입니다.
        # Manager 클래스의 생성자를 호출하여 id, phoneNumber, skill을 설정하고,
        # title 매개변수를 추가로 받아 객체의 속성으로 설정합니다.
        super().__init__(id, phoneNumber, skill)
        self.title = title #직원의 직책
    
    def printinfo(self):
        # Manager 클래스의 printinfo 메서드를 호출하여 id, phoneNumber, skill 출력 후,
        # Employee 클래스의 title을 출력합니다.
        super().printinfo()
        print(f"직급: {self.title}")

# 샘플 코드
person1 = Person(1, "555-123-4567")
person1.printinfo()

manager1 = Manager(2, "555-987-6543", "리더십")
manager1.printinfo()

employee1 = Employee(3, "555-555-5555", "기술", "소프트웨어 엔지니어")
employee1.printinfo()
