# Basic_Shape_Hierarchy
Women in AI - Python - lesson 6

Explanation

Base Class (Shape):

Contains an initializer to set the name attribute.
Defines the area method, which returns None and is intended to be overridden by subclasses.

Subclasses (Rectangle and Circle):

Each subclass initializes its specific attributes and overrides the area method to calculate the area according to its shape.

Polymorphism (print_area function):

The print_area function takes any Shape object, demonstrating polymorphism by calling the area method of the specific subclass.

Running the Code

When you run this code, it will output:

```python
The area of the Rectangle is: 50
The area of the Circle is: 153.93804002589985