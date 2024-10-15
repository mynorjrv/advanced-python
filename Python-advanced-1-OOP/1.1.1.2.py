class Duck:
    def __init__(self, height, weight, sex):
        self.height = height
        self.weight = weight
        self.sex = sex

    def walk(self):
        pass

    def quack(self):
        return print('Quack')
        
duckie = Duck(10, 10, 'm')

print(duckie)
print(duckie.sex)

duckie.quack()
