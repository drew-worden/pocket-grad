#IMPORTS
import math
import torch
import numpy as np
import matplotlib.pyplot as plt
from graphviz import Digraph

#SAMPLE FUNCTION
def f(x):
    return x**2 + 3*x + 4

#GRAPH SAMPLE FUNCTION
x_ticks = np.arange(-10, 11)
y_ticks = f(x_ticks)

plt.plot(x_ticks, y_ticks)
#UNCOMMENT TO SHOW GRAPH
#plt.show()

#NUMERICAL DERIVATIVE
def numerical_derivative(function, variable):
    offset = 0.001
    return (function(variable + offset) - function(variable)) / offset

#TAKING DERIVATES WITH RESPECT TO ANOTHER VARIABLE
def derivate_with_respect_to_a():
    #INPUTS
    a = 1
    b = 2
    c = 3

    #EQUATION
    equation = a * b + c

    #TAKE DERIVATIVE WITH RESPECT TO A
    a += 0.0001
    equation_respect_to_a = a * b + c

    derivative = (equation_respect_to_a - equation) / 0.0001
    return derivative

#NODE DATA STRUCTURE
class Node:
    #CONSTRUCTOR
    def __init__(self, value, children = (), operation = ""):
        self.value = value
        self.children = children
        self.operation = operation

    #NICE PRINT REPRESENTATION
    def __repr__(self):
        return f"Node(value = {self.value}, children = {self.children}, operation = {self.operation})"

    #ADDITION OPERATION
    def __add__(self, other):
        output = Node(self.value + other.value, (self, other), "+")
        return output

    #MULTIPLICATION OPERATION
    def __mul__(self, other):
        output = Node(self.value * other.value, (self, other), "*")
        return output

#GRAPH NODES
def node_graph(end_node):
    #GRAPH OBJECT
    graph = Digraph(format = "png", graph_attr = {"rankdir": "TB"})

a = Node(1)
b = Node (2)
c = Node(3)

d = a * b + c