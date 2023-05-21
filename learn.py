class Person(object):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def eat(self):
        self.weight += 0.2
        print(f"刚才吃东东西了,体重增加0.2公斤,当前体重{self.weight}公斤")

    def run(self):
        self.weight -= 0.1
        print(f"刚才跑不了,体重减少0.1公斤,当前体重{round(self.weight,1)}公斤")

p1 = Person("小明",75)
p1.run()
p1.run()
p1.run()

