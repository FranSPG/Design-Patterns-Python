
# coding: utf-8

# In[82]:


import abc
class Component(object):
    
    @abc.abstractmethod
    def do(self):
        pass

class Leaf(Component):
    
    def __init__(self, name):
        self._name = name
        Component.__init__(self)
        
    def do(self):
        print(self._name)

class Composite(Component):
    
    def __init__(self):
        Component.__init__(self)
        self.children = []

    def add(self, child):
        self.children.append(child)

    def remove(self, child):
        self.children.remove(child)
        
    def do(self):
        for child in self.children:
            child.do()

