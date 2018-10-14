
# coding: utf-8

# In[2]:


import abc


# In[41]:


class SoldierFactory:
    
    def __init__(self):
        self._soldier = {}
        
    def get_flyweight(self, key):
        try:
            flyweight = self._soldier[key]
        except KeyError:
            flyweight = SoldierConcrete()
            self._soldier[key] = flyweight
        return flyweight    


# In[42]:


class Soldier():
    
    maxHP = 100
    atck = 20
    defen = 5
    
    @abc.abstractmethod
    class attack():
        pass


# In[43]:


class SoldierConcrete(Soldier):
    
    hp = Soldier.maxHP
    
    def attack(self):
        print("SoldierConcrete doing...")


# In[44]:


soldier_factory = SoldierFactory()


# In[45]:


concrete_soldier_a = soldier_factory.get_flyweight("soldiera")


# In[48]:


concrete_soldier_b = soldier_factory.get_flyweight("soldierb")


# In[49]:


concrete_soldier_a is concrete_soldier_b


# In[50]:


concrete_soldier_a.attack()

