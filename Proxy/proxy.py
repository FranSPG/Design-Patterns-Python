
# coding: utf-8

# In[117]:


import abc


# In[118]:


class Proxy(object):
    
    @abc.abstractmethod
    def doone(self):
        """required"""


# In[119]:


class ProxyImpl(Proxy):
    
    def __init__(self, realObject):
        self._realObject = realObject
    
    def doone(self):
        self._realObject.doone()


# In[120]:


class RealObject(Proxy):
       
    def doone(self):
        print("RealObject doing one...")
        
    def dotwo(self):
        print("RealObject doing two...")
        
    def dothree(self):
        print("RealObject doing three...")

