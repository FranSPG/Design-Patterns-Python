
# coding: utf-8

# In[64]:


import abc
class strategy(object):
    
    @abc.abstractmethod
    def do(self):
        """required"""
        print("doing strategy")


# In[65]:


class strategyA(strategy):
    
    def do(self):
        print("doing one")


# In[66]:


class strategyB(strategy):
    
    def do(self):
        print("doing two")

