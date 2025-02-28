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

Some examples of other dunder methos are in the following table:

| Function or  operator | Dunder method               |
|-----------------------|-----------------------------|
| +                     | `__add__(self, other)`      |
| -                     | `__sub__(self, other)`      |
| *                     | `__mul__(self, other)`      |
| //                    | `__floordiv__(self, other)` |

For more information on dunder methods refer to <https://docs.python.org/3/reference/datamodel.html#special-method-names>.

## Inheritance and polymorphism

Inheritance express a fundamental relationship between classes: superclasses (partents) and subclasses (descendants). Inheritance creates a hierarchy, any objet bound to a specific level of the class hierarchy inherits all the traits defined inside any of the superclasses.

With this, inheritance is a way of building new classes, not from scratch, but from an already defined repertoire of traits. The new class inherits the traits of its parent, but its also able to add new features if needed.

Each subclass is more specialized (or more specific) than its superclass. Conversely, each superclass is more general (more abstract) than any of its subclasses.

```Python
class Vehicle:
    pass

class LandVehicle(Vehicle):
    pass

class TrackedVehicle(LandVehicle):
    pass
```


### Multiple inheritance

In Python, it is possible to derive a new class from more than one previously defined class.

> Even though it exists... Is not recommended.

#### MRO - Method Resolution Order

Python defines a MRO algorithm to define which traits are used in case of multiple inheritance.

```Python
class A:
    def info(self):
        print('Class A')

class B(A):
    def info(self):
        print('Class B')

class C(A):
    def info(self):
        print('Class C')

class D(B, C):
    pass

D().info()
```

In the example, `D().info()` will go a level up and then left to right, calling the method in B as a result.

Even with this algorithm it is possible to create inconsistencies.

### Polymorphism

Polymorphism refers to the provision of a single interface to object of different types. This refers on how two different types are handled differently even if the same operator is applied to them. This creates an abstraction to treat those types in a uniform way.

> This was partially introduce in core syntax

One way of implementing polymorphism is inheritance. A subclass can make use of base class methods or override them to fit the new type. 

Another way of achieving polymorphism is by the implementation of Duck Typing: "If it walks like a duck and it quacks like a duck, then it must be a duck". This refers to an object suitability being determined by the presence of certain attribute, rather than the type itself.

In duck typing, we believe that objects own the methods that are called. If they do not own them, then we should be prepared to handle exceptions.

## Functions arguments

Functions in Python can work with an arbitrary number of positional or keyword arguments. When working with them, the `*args` and `**kwargs` identifiers are used, the names can be changed but it is important to respect the order of them and the leading asterisks.

```Python
def g(a, b, *args, kw_only, **kwargs):
	print(f'{a=}, {b=}, {args=}, {kw_only}, {kwargs}')
```

- `*args` refers to a tuple of all not explicitly expected positional arguments.
- `**kwargs` refers to a dictionary of all unexpected arguments passed in the form keyword=value pair.

In Python, the asterisk denotes an 'unpacking'. Using the asterisks in the function definition means these parameters carry multiple items and should be unpacked.

> You can use ** outside function definitions (in function calls and dictionaries definitions) to unpack dictionaries. For example:\
> `first = {'a': 3, 'b': 5}`\
> `second = {'c': 4, 'd': 7}`\
> `another = {**first, **second}`\
> Would result in \
> `another = {'a': 3, 'b': 5, 'c': 4, 'd': 7}`

The order is important because since the `*` symbol takes all the not expected positional arguments, all arguments after it must be keyword arguments. Also, the `*` symbol can be used without an identifier to invalidate not expected positional arguments, this way receiving non expected positional arguments raises an error.

> keyword only arguments are usually used as options for a function. A simple example is `print('something', end='\t')`. Another usage is when it is important to not get data confused.

In the same fashion of `*` separating positional and keyword only arguments, it is possible to use `/` to separate positional only arguments. 

```Python
def g(pos_only, /, a, b, *args, kw_only, **kwargs):
	print(f'{pos_only=}, {a=}, {b=}, {args=}, {kw_only}, {kwargs}')
```


## Decorators

Decorators are a design pattern that allows behavior to be added to an object without affecting other instances of the same class. 

In Python, a decorator's operation is based on wrapping a function with a new "decorating" function (or class). This is done by passing the original (**decorated**) function as a parameter to the **decorating** function. The decorating function then returns a new function.

Decorators are used to perform operations before or after a call to the decorated (wrapped) object, or even prevent its execution.

Some common case of use are:

- the validation of arguments;
- the modification of arguments;
- the modification of returned objects;
- the measurement of execution time;
- message logging;
- thread synchronization;
- code refactoring;
- caching.

Decorators are described in PEP 318 and PEP 3129.

### Function decorators

```Python
def simple_hello():
    print("Hello from simple function!")

def simple_decorator(function):
    print(
		'We are about to call "{}"'.format(function.__name__)
	 )
    return function

decorated = simple_decorator(simple_hello)
decorated()
```

Decorators for functions accepts another function as argument and return a new function with some extra behavior.

In python this is done with the following syntax:

```Python
def simple_decorator(function):
    print('We are about to call "{}"'.format(function.__name__))
    return function

@simple_decorator
def simple_hello():
    print("Hello from simple function!")

simple_hello()
```

In this case, the definition of `simple_hello()` is decorated with `@simple_decorator`. The operation is performed on the object (the function) name, which means the object name cease to indicate the original object and then indicates the object returned by the decorator.

Decorators are specially useful when debugging or refactoring code.

### Decorators should be universal

Decorators must support any function, regardless of the number and type of arguments passed. `*args` and `**kwargs` are used to achieve this, in combination with a closure technique to persist the arguments.

> In programming languages, a closure, also lexical closure or function closure, is a technique for implementing lexically scoped name binding in a language with first-class functions. Operationally, a closure is a record storing a function together with an environment.
> In Python, this can be done using nested functions.

```Python
def simple_decorator(own_function):

    def internal_wrapper(*args, **kwargs):
        print('"{}" was called with the following arguments'.format(own_function.__name__))
        print('\t{}\n\t{}\n'.format(args, kwargs))
        own_function(*args, **kwargs)
        print('Decorator is still operating')

    return internal_wrapper


@simple_decorator
def combiner(*args, **kwargs):
    print("\tHello from the decorated function; received arguments:", args, kwargs)

combiner('a', 'b', exec='yes')
```

Arguments passed to the decorated function are available to the decorator, so the decorator can use them.

A nested function (`internal_wrapper()`) could reference an object (`own_function()`) in its enclosing scope thanks to the closure.

### Decorators can accept their own arguments

In Python, it is possible to create a decorator with arguments. In this case, the decorator is enriched with one more nested function to make it available to handle arguments at all call levels. 

One advantage of decorator is that we do not have to change every function to achieve some behavior, we just add one line over the function.

```Python
def warehouse_decorator(material):
    def wrapper(our_function):
        def internal_wrapper(*args):
            print('<strong>*</strong> Wrapping items from {} with {}'.format(our_function.__name__, material))
            our_function(*args)
            print()
        return internal_wrapper
    return wrapper


@warehouse_decorator('kraft')
def pack_books(*args):
    print("We'll pack books:", args)


@warehouse_decorator('foil')
def pack_toys(*args):
    print("We'll pack toys:", args)


@warehouse_decorator('cardboard')
def pack_fruits(*args):
    print("We'll pack fruits:", args)


pack_books('Alice in Wonderland', 'Winnie the Pooh')
pack_toys('doll', 'car')
pack_fruits('plum', 'pear')
```

### Decorator stacking

Python allows to apply multiple decorator to a callable object (function, method or class).

When using this stacking it is important to remember the order in which the decorators are listed. In the example, `inner_decorator` is executed over the function, then `outer_decorator` is executed over the previous result.

```Python
@outer_decorator
@inner_decorator
def function():
    pass

abcd = subject_matter_function()
```

### Decorating functions with classes

A decorator does not have to be a function. In Python, it could be a class that plays the role of a decorator as a function.

We can define a decorator as a class, and in order to do that, we have to use a `__call__` special class method. When a user needs to create an object that acts as a function (i.e., it is callable) then the function decorator needs to return an object that is callable, so the `__call__` special method will be very useful.

```Python
class SimpleDecorator:
    def __init__(self, own_function):
        self.func = own_function

    def __call__(self, *args, **kwargs):
        print('"{}" was called with the following arguments'.format(self.func.__name__))
        print('\t{}\n\t{}\n'.format(args, kwargs))
        self.func(*args, **kwargs)
        print('Decorator is still operating')


@SimpleDecorator
def combiner(*args, **kwargs):
    print("\tHello from the decorated function; received arguments:", args, kwargs)


combiner('a', 'b', exec='yes')

```

An advantage of this approach is the subsidiarity classes can offer, like creating dedicated supportive methods.

> For info about python callables: <https://eli.thegreenplace.net/2012/03/23/python-internals-how-callables-work/>

### Class decorators

Class decorator use the same syntax and implement the same concepts as function decorators.

Instead of wrapping individual methods with functions decorators, class decorators are ways to manage classes or wrap special method calls into additional logic that manages or extends instances that are created.

The syntax is the same as function decorators, class decorators appear before the `class` declaration and they operate over the class name.

```Python
@my_decorator
class MyClass:

obj = MyClass()

'''Is equivalent to'''
'''Doc sting because markdown gets crazy with #''' 
def my_decorator(A):
   ...

class MyClass:
   ...

MyClass = my_decorator(MyClass())

obj = MyClass()

```

A more extensive example is given bellow:

```Python
def object_counter(class_):
    class_.__getattr__orig = class_.__getattribute__

    def new_getattr(self, name):
        if name == 'mileage':
            print('We noticed that the mileage attribute was read')
        return class_.__getattr__orig(self, name)

    class_.__getattribute__ = new_getattr
    return class_

@object_counter
class Car:
    def __init__(self, VIN):
        self.mileage = 0
        self.VIN = VIN

car = Car('ABC123')
print('The mileage is', car.mileage)
print('The VIN is', car.VIN)
```


## Static and class methods

### Instance methods

Until now, we have implemented methods that perform operations on the instances, and in particular over attributes of the instances. For this, they are called instance methods.

Instances methods takes `self` as the first parameter, which is their hallmark. The name `self` is a convention, and allows you to refer to the instance. It follows that in order t successfully use the instance method, the instance must have previously existed.

```Python
class Example:
    def __init__(self, value):
        self.__internal = value

    def get_internal(self):
        return self.__internal

example1 = Example(10)
example2 = Example(99)
print(example1.get_internal())
print(example2.get_internal())
```


### Class methods

This methods, like class variables, work on the class itself, and not on the objects that are instantiated. To signal a class method, it is decorator with `@classmethod` before the definition of the method.

The two most popular reasons why this methods are useful are 
- to control access to class variables;
- to implement an alternative constructor, to create instances in an alternative way.

By convention, class methods receives `cls` as the first parameter instead of `self`, and is used to refer to the class methods and class attributes.

```Python
class Example:
    __internal_counter = 0

    def __init__(self, value):
        Example.__internal_counter +=1

    @classmethod
    def get_internal(cls):
        return '# of objects created: {}'.format(cls.__internal_counter)

print(Example.get_internal())

example1 = Example(10)
print(Example.get_internal())

example2 = Example(99)
print(Example.get_internal())
```

In the example above, the class method is used to access a class variable. It would be possible to use `Example.__internal_counter` but this will be inconsistent with the convention and the code loses its effectiveness in communicating its own meaning. (?)

An exception is the `__init__()` method, which by definition is an instance method, so it can’t use “cls”, and as a result it references the class variable by the “Example” prefix.

```Python
class Car:
    def __init__(self, vin):
        print('Ordinary __init__ was called for', vin)
        self.vin = vin
        self.brand = ''

    @classmethod
    def including_brand(cls, vin, brand):
        print('Class method was called')
        _car = cls(vin)
        _car.brand = brand
        return _car

car1 = Car('ABCD1234')
car2 = Car.including_brand('DEF567', 'NewBrand')

print(car1.vin, car1.brand)
print(car2.vin, car2.brand)
```

In the second example, it is show how to use the class method as an alternative constructor, allowing you to handle an additional argument.

In this case, `cls(vin)` is used to create the instance, using the normal constructor and then performing the additional of including brand.

### Static methods
Static methods are methods that do not require (and do not expect!) a parameter indicating a class instance or the class itself in order to be executed. To signal a static method, it is decorator with `@staticmethod` before the definition of the method.

They are use useful:
- When you need a utility method that is semantically related to the class, but does not require an object of that class or the class itself;
- When the method do not need to know the state of the objects or classes.

Static methods do not have the hability to modify the state of object or classes, because they lack the parameters that would allow this. (There is no `self` or `cls`).

```Python
class Bank_Account:
    def __init__(self, iban):
        print('__init__ called')
        self.iban = iban
            
    @staticmethod
    def validate(iban):
        if len(iban) == 20:
            return True
        else:
            return False

account_numbers = ['8' * 20, '7' * 4, '2222']

for element in account_numbers:
    if Bank_Account.validate(element):
        print('We can use', element, ' to create a bank account')
    else:
        print('The account number', element, 'is invalid')
```

From Arjan: Some methods can (and should) be replaced by functions, classes that just use static methods should be replaced by modules n.n .

In the example, a validation can be done without creating instances or using information from the class itself, but it make sense to group the method inside the class.

## Abstract classes

Abstract classes should be considered as a blue print for other classes, a contract between the class designer and the programmer:

- The class designer sets requirements regarding methods that must be implemented. In an abstract class this methods are declared but not defined in detail. Such methods are called **abstract methods**.
- The programmer has to deliver all method definitions by overriding the methods declarations received from the abstract class. 

This contract creates an interface between all the subclasses created from the abstract class and the user of this classes, all child classes will be equipped with a set of concrete methods imposed by the abstract class. In this sense, abstract classes are strongly related to inheritance.

Abstract classes allows polymorphism, all subclasses use common method names but each one delivers a set of their own method implementation.

Furthermore, a class which contains one or more abstract methods is called an abstract class. This means that abstract classes are not limited to containing only abstract methods – some of the methods can already be defined, but if any of the methods is an abstract one, then the class becomes abstract. This allows to design large functional units, implementing some common functionality to all subclasses.

It is important to remember that it isn’t possible to instantiate an abstract class, and it needs subclasses to provide implementations for those abstract methods which are declared in the abstract classes. This behavior is a test performed by a dedicated Python module to validate if the developer has implemented a subclass that overrides all abstract methods.

With this, we have defined the means by which to provide a common Application Program Interface (API) for a set of subclasses. This capability is specially useful when a team or third-party is going to provide implementations (for example plugins) even after the main application development is finished.

### Implementing abstract classes

Python has come up with a module which provides the helper class for defining Abstract Base Classes (ABC) and that module name is abc.

The ABC allows you to mark classes as abstract ones and distinguish which methods of the base abstract class are abstract. A method becomes abstract by being decorated with an `@abstractmethod` decorator.

```Python
import abc

class BluePrint(abc.ABC):
    @abc.abstractmethod
    def hello(self):
        pass

class GreenField(BluePrint):
    def hello(self):
        print('Welcome to Green Field!')

class RedField(BluePrint):
    def yellow(self):
        pass

gf = GreenField()
gf.hello()
``` 

As said before, the abstract class cannot be instantiated, attempting something as `bp = BluePrint()` raises a `TypeError`. Following this, if a subclass does not override an abstract method (as `RedField`), this subclass is also an abstract class and instantiating it will also raise a `TypeError`.

## Encapsulation

Encapsulation describes the idea of building attributes and methods that work on those attributes within a class(?).

Encapsulation is used to hide the attributes inside a class (like a capsule), preventing unauthorized parties direct access to them. Publicly accessible methods are provided in the class to access the values, and other object call those methods to retrieve and modify the values within the object. This can be a way to enforce a certain amount of privacy for the attributes.

Direct access to the object attribute should not be possible, but you can always invoke methods, acting like proxies, to perform some actions on the attributes.

Python introduces the concept of properties that act like proxies to encapsulated attributes.

This concept has some interesting features:

- the code calling the proxy methods might not realize if it is "talking" to the real attributes or to the methods controlling access to the attributes;
- in Python, you can change your class implementation from a class that allows simple and direct access to attributes to a class that fully controls access to the attributes, and what is most important –consumer implementation does not have to be changed; by consumer we understand someone or something (it could be a legacy code) that makes use of your objects.

Remember that this is not full access control, the programmer can still get access to your attributes intentionally as Python does not deliver true privacy.

Why?

Guido Van Rossum, best known as the author of Python, once said: "We're all consenting adults here" justifying the absence of such access restrictions.

So, if your code does intentionally access the attributes marked as private (prefixed with a double underscore) in a direct way, then remember that this behavior is unpythonic.

### Implementing properties

Python allows control over attributes with the build-in function `property()` and corresponding decorator `@property`.

This decorator plays an important role:

- it designates a method which will be called automatically when another object wants to read the encapsulated value;
- the name of the designated method will be used as the name of the instance attribute corresponding to the encapsulated attribute;
- it should be defined before the method responsible for setting the value of the encapsulated attribute, and before the method responsible for deleting the encapsulated attribute.

```Python
class TankError(Exception):
    pass


class Tank:
    def __init__(self, capacity):
        self.capacity = capacity
        self.__level = 0

    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, amount):
        if amount > 0:
            # fueling
            if amount <= self.capacity:
                self.__level = amount
            else:
                raise TankError('Too much liquid in the tank')
        elif amount < 0:
            raise TankError('Not possible to set negative liquid level')

    @level.deleter
    def level(self):
        if self.__level > 0:
            print('It is good to remember to sanitize the remains from the tank!')
        self.__level = None

# our_tank object has a capacity of 20 units
our_tank = Tank(20)

# our_tank's current liquid level is set to 10 units
our_tank.level = 10
print('Current liquid level:', our_tank.level)

# adding additional 3 units (setting liquid level to 13)
our_tank.level += 3
print('Current liquid level:', our_tank.level)

# let's try to set the current level to 21 units
# this should be rejected as the tank's capacity is 20 units
try:
    our_tank.level = 21
except TankError as e:
    print('Trying to set liquid level to 21 units, result:', e)

# similar example - let's try to add an additional 15 units
# this should be rejected as the total capacity is 20 units
try:
    our_tank.level += 15
except TankError as e:
    print('Trying to add an additional 15 units, result:', e)

# let's try to set the liquid level to a negative amount
# this should be rejected as it is senseless
try:
    our_tank.level = -3
except TankError as e:
    print('Trying to set liquid level to -3 units, result:', e)

print('Current liquid level:', our_tank.level)

del our_tank.level
```

With this, the name convention is as follows:

- the getter method is decorated with `@property`. The name of the decorated method designates the name of the attribute to be used by the external code;
- `@name.setter` decorates the setter method where 'name' is the name of the previously decorated method;
- `@name.deleter` decorates the deleter method, and again 'name' is the name of the previously decorated method.

Other code can make use of the property without even knowing about the logic hidden behind it. So, this becomes convenient when access control over an attribute is needed, for example when applying constrains over the attribute.

## Composition and Inheritance

### A review of inheritance

So far, we have been using the inheritance concept. In this relation, a subclass inherits all the methods and attributes and allows the subclass to extend what has been inherited. This creates a more specialized class and these classes are called tightly coupled.

Inheritance models an **is a** relation (a car is a vehicle). The primary use is to reuse code over a common base. As a result, inheritance could form a tree.

A problem with inheritance is that it can create huge, complex, hierarchical structures of classes. This structure would be hard to understand and debug. This problem is known as class explosion.

### Composition

Another way of constructing adaptable objects is by **composition**. 

Composition models a **has a** relation (a computer has a graphic card). In this sense, an object can be compose using other different objects. The objects used in the composition deliver a set of desired traits and together the act as building blocks of a more complicated structure.

Composition then, instead of using the idea of a common ancestor, projects a class as a container (a composite) able to use other smaller objects, where each part implements at of a desired behavior. 

A result of this implementation is that now the composite is loosely coupled with its blocks, those blocks could be exchanged at any time.

```Python
class Car:
    def __init__(self, engine):
        self.engine = engine


class GasEngine:
    def __init__(self, horse_power):
        self.hp = horse_power

    def start(self):
        print('Starting {}hp gas engine'.format(self.hp))


class DieselEngine:
    def __init__(self, horse_power):
        self.hp = horse_power

    def start(self):
        print('Starting {}hp diesel engine'.format(self.hp))


my_car = Car(GasEngine(4))
my_car.engine.start()
my_car.engine = DieselEngine(2)
my_car.engine.start()
```

As you can see, a new class is created with an object of another class as an argument. Now the responsibility of the developer is to provide methods to the possible blocks.

### Composition over inheritance

It is common to favor composition over inheritance. Composition offers higher flexibility, it is not needed to build wide hierarchy structures and requirements changes could be managed more easily since dependencies are reduced.

In the other hand, composition transfers responsibilities to the developer, who now should assure that all possible component classes implement the methods in a proper manner. While in inheritance not all inherited methods should be re implemented.

An important fact is that these approaches are not mutually exclusive. A combination of both can be implemented and used as supplementary means of solving problems.

### Some words on Protocols

Python can implement a pattern called Protocol. Protocols, as ABC, implements a layer of abstraction, they both implement interfaces.

Protocols relies on duck typing and ABCs relies on nominal (explicit) typing.

## Inheriting from built-in classes

Python gives you the ability to create a class that inherits properties from any Python build-in class in order to get a new class that can enrich the parent's attributes or methods. As a result, your newly-created class has the advantage of all of the well-known functionalities inherited from its parent or even parents and you can still access those attributes and methods.

Later, you can override the methods by delivering your own modifications for the selected methods. 

As an example, we can implement a list that just accepts integers as elements. But... Why might you need such object? The idea is to validate the type of elements so the new IntegersList can focus on implementation an not on type control.