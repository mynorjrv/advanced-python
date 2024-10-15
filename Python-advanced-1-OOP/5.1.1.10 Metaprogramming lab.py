import datetime
import time

class Time_Meta(type):
    children = None

    def __new__(mcs, name, bases, dictionary):
        dictionary['instanciation_time'] = datetime.datetime.now().time()
        dictionary['get_instanciation_time'] = lambda : dictionary['instanciation_time']
        if mcs.children == None:
            mcs.children = [name]
        else:
            mcs.children.append(name)
        obj = super().__new__(mcs, name, bases, dictionary)
        return obj
    
# Escrito por ChatGPT
class TimeStampedMeta(type):
    # Class variable to store the names of instantiated classes
    instantiated_classes = []

    def __new__(cls, name, bases, class_dict):
        # Create the new class
        new_class = super().__new__(cls, name, bases, class_dict)
        
        # Add the class name to the list of instantiated classes
        cls.instantiated_classes.append(name)
        
        # Add the instantiation_time attribute to the class
        new_class.instantiation_time = time.time()
        
        # Add the get_instantiation_time method to the class
        def get_instantiation_time(self):
            return self.instantiation_time
        
        new_class.get_instantiation_time = get_instantiation_time
        
        return new_class

class My_Class1(metaclass=Time_Meta):
    pass

print(My_Class1.get_instanciation_time())
print(Time_Meta.children)

class My_Class2(metaclass=Time_Meta):
    def greetings(self):
        print('We are ready to greet you!')

print(My_Class2.get_instanciation_time())
print(Time_Meta.children)

object10 = My_Class1()
object11 = My_Class1()

print(My_Class1.get_instanciation_time())
print(Time_Meta.children)

object20 = My_Class2()
object21 = My_Class2()

print(My_Class2.get_instanciation_time())
print(Time_Meta.children)