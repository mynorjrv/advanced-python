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
