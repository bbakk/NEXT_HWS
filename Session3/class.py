class person:
    def __init__(self,name,age,height):
        self.name = name
        self.age = age
        self.height = height
    def introduce(self):
        print(f"안녕하세요 제 이름은 {self.name}입니다. 제 나이는 {self.age}입니다. 제 키는 {self.height}입니다.")
    def yell(self):
        print("아?")

class developer(person):
    def __init__(self,name,age,height):
        super().__init__(name,age,height)
        keyboard='기계식'
    def yell(self):
        print("어?")
class designer(person):
    def __init__(self,name,age,height,disease):
        self.disease = disease
        super().__init__(name,age,height)
class productmanager(person):
    def __init__(self, name, age, height):
        super().__init__(name, age, height)
    def yell(self):
        print("개발자님 여기 오류있어요")
    def aging(self):
        self.age +=2
        self.height -= 5
        print("개발자를 새로 뽑아야하나..")
        keyboard = '멤브레인'

d1= developer("경빈", 24, 190)
d2= designer("나연", 29, 160, "수족냉증")
p1= productmanager("채영", 25, 155)

d1.introduce()
d1.yell()
d2.introduce()
d2.yell()
p1.introduce()
p1.yell()
p1.aging()
p1.introduce()