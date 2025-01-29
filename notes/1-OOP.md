# OOP

## Basic concepts
- **Class**: an idea, blueprint, or recipe for an instance.
- **Instance**: an instantiation of the class; often used interchangeably with the term 'object'.
- **Object**: Python's representation of data and methods; objects could be aggregates of instances.
- **Attribute**: any object or class trait; could be a variable or method.
- **Method**: a function built into a class that is executed on behalf of the class or object; some say that it’s a 'callable attribute'.
- **Type**: refers to the class that was used to instantiate the object.

### Basic definition of a class
```Python
class Duck:
    def __init__(self, height, weight, sex):
        self.height = height
        self.weight = weight
        self.sex = sex

    def walk(self):
        pass

    def quack(self):
        return print('Quack')
```

Classes can be build from scratch or employ inheritance to get a more specialized class based on another class.

Additionally, a new built class could be use as a superclass for other derived classes (subclasses).

### Instances and objects

```Python
duckling = Duck(height=10, weight=3.4, sex="male")
drake = Duck(height=25, weight=3.7, sex="male")
hen = Duck(height=20, weight=3.4, sex="female")
```

An **instance** is one particular physical instantiation of a class that occupies memory and has data elements. This is what 'self' refers to when we deal with class instances.

An **object** is everything in Python that you can operate on, like a class, instance, list, or dictionary.

The term instance is very often used interchangeably with the term object, because object refers to a particular instance of a class. It’s a bit of a simplification, because the term object is more general than instance.

### Attributes and methods

```Python
drake.quack()
print(duckling.height)
```

An **attribute** is a capacious term that can refer to two major kinds of class traits:

- **variables**: containing information about the class itself or a class instance; classes and class instances can own many variables;
- **methods**: formulated as Python functions; they represent a behavior that could be applied to the object.

### Type

```Python
print(Duck.__class__)
print(duckling.__class__)
print(duckling.sex.__class__)
print(duckling.quack.__class__)

print(type(Duck))
print(type(duckling))
print(type(duckling.sex))
print(type(duckling.quack))
```

A type is one of the most fundamental and abstract terms of Python:

- it is the foremost type that any class can be inherited from;
- as a result, if you’re looking for the type of class, then type is returned;
- in all other cases, it refers to the class that was used to instantiate the object; it’s a general term describing the type/kind of any object;
- it’s the name of a very handy Python function that returns the class information about the objects passed as arguments to that function;
- it returns a new type object when type() is called with three arguments; we'll talk about this in the 'metaclass' section.

## A bit more depth
### Instance variables
```Python
class Demo:
    def __init__(self, value):
        self.instance_var = value

d1 = Demo(100)
d2 = Demo(200)

d1.another_var = 'another variable in the object'

print('contents of d1:', d1.__dict__)
print('contents of d2:', d2.__dict__)
```

Instances variables exists when and only when they are explicitly created and added to an object. This can be done during initialization (using the `__init__` method) or later at any moment of the object's life. Furthermore, any existing instance variable can be removed at any time.

Instance variables are accessed using the syntax `instance.variable`.

Each instance carries it own set of variables, modifying the instance variables of one instance has no impact in other instances of the same class. Instance variables are completely isolated from each other. 

Every python object has a `__dict__` property that lists the content of each object.

### Class variables
```Python
class Demo:
    class_var = 'shared variable'

d1 = Demo()
d2 = Demo()

print(Demo.class_var)
print(d1.class_var)
print(d2.class_var)

print('contents of d1:', d1.__dict__)
```

Class variables are defined within the class construction, so they are available before any class instance is created. 

Class variables are accessed using the syntax `Class.variable`.

Class variables are used to store metadata relevant to the class in general, rather than to the instances. An example could be the number of instances created of that specific class. Since class variables are stored in the class itself and it exists in just one copy, all class variables are shared by all the instances of that class. 

A class variable can be read from a class instance, but using `__dict__` over an instance will not list the class variable.

Class variables can also be created later or modified. When setting a value it is necessary to use the class itself, if an instances is used a instance variable is created.

### Strange mention of isinstance()
You can use a class variable to mimic the functionality of is instance().

### Instance variables and class variables in inheritance
```Python
class Phone:
    counter = 0

    def __init__(self, number):
        self.number = number
        Phone.counter += 1

    def call(self, number):
        message = 'Calling {} using own number {}'.format(number, self.number)
        return message


class FixedPhone(Phone):
    last_SN = 0

    def __init__(self, number):
        super().__init__(number)
        FixedPhone.last_SN += 1
        self.SN = 'FP-{}'.format(FixedPhone.last_SN)


class MobilePhone(Phone):
    last_SN = 0

    def __init__(self, number):
        super().__init__(number)
        MobilePhone.last_SN += 1
        self.SN = 'MP-{}'.format(MobilePhone.last_SN)


print('Total number of phone devices created:', Phone.counter)
print('Creating 2 devices')
fphone = FixedPhone('555-2368')
mphone = MobilePhone('01632-960004')

print('Total number of phone devices created:', Phone.counter)
print('Total number of mobile phones created:', MobilePhone.last_SN)

print(fphone.call('01632-960004'))
print('Fixed phone received "{}" serial number'.format(fphone.SN))
print('Mobile phone received "{}" serial number'.format(mphone.SN))

```

## Core syntax
Core syntax refers to the ability of core operations to perform specific operations on different data types, using the same operator.

This means you are able to 'add' two strings, which results in concatenation, or add two integers. Both operations using + but on respective data types.

Core syntax covers:
- +, -, *, /, %, and others
- ==, >, <, in, and othes
- indexing, slicing, subscripting
- some build-in functions like str(), len()
- reflexion - isinstance(), issubclass()

Python allows to employ core operators on programmer defined objects. This is done using special purpose methods ('magic methods'), which are designated to handle specific operations.

Magic methods names are surrounded by dunders (double underscores). This dunders indicate that these methods are not called directly, but in a process of expression evaluation. For this, they are also called dunder methods.

An example of these methods is `__add__()`, which is the corresponding dunder method for the + operator.

```Python
number = 10
print(number + 20)

number = 10
print(number.__add__(20))
```

Core operands can be used with programmer defined objects implementing the appropriated dunder method in the class definition:

```Python
class Person:
    def __init__(self, weight, age, salary):
        self.weight = weight
        self.age = age
        self.salary = salary

    def __add__(self, other):
        return self.weight + other.weight


p1 = Person(30, 40, 50)
p2 = Person(35, 45, 55)

print(p1 + p2)

```

`dir()` and `help()` functions can be used to know more about an object. `dir()` lists the attributes and methods of an object, while `help()` displays more information about each attribute and method. 

`help()` is also used to display documentation (if delivered) of modules, functions, classes, and keywords.

For more information on dunder methods refer to <https://docs.python.org/3/reference/datamodel.html#special-method-names>.

