class Dog(object):
    
    def __init__(self, name, age, color, breed):
        self.name = name
        self.age  = age
        self.color = color
        self.legs = 4
        self.breed = breed

    def walk(self):
        print "%s is walking" % self.name

    def wag_tail(self):
        print "%s's tail is wagging" % self.name

    def bark(self):
        print "%s is barking!" % self.name

    def sniff(self):
        print "%s is sniffing %s" % (dog1.name, dog2.name)

    def eat_food(self):
        print "%s is eating %s's food" % (dog2.name, dog1.name)

    def growl(self):
        print "%s growls at %s" % (dog1.name, dog2.name)

    def snap(self):
        print "%s snaps at %s and stands her ground!" % (dog1.name, dog2.name)

    def run(self):
        print "%s run's away!" % dog2.name

dog1 = Dog('Lily', 5, 'brown', 'pitbull')
dog2 = Dog('Comet', 6, 'white', 'lab')
print dog1.name + ' is %d ' % dog1.age
print dog1.name + ' is %s and is a %s' % (dog1.color, dog1.breed)
dog1.walk()
print dog2.name + ' is %d' % dog2.age
print dog2.name + ' is %s and is a %s' % (dog2.color, dog2.breed)
dog2.walk()
dog1.wag_tail()
dog2.bark()
dog1.bark()
dog1.sniff()
dog2.wag_tail()
dog2.eat_food()
dog1.growl()
dog1.snap()
dog2.run()
