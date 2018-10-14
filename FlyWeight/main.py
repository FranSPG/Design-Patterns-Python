
# coding: utf-8

# In[6]:


from flyweight import SoldierFactory, Soldier, SoldierConcrete


# In[70]:


if __name__ == '__main__':
    
    soldier_factory = SoldierFactory()
    concrete_soldier_a = soldier_factory.get_flyweight("soldiera")
    concrete_soldier_b = soldier_factory.get_flyweight("soldierb")
    
    concrete_soldier_a is concrete_soldier_b
    
    concrete_soldier_a.attack()
    concrete_soldier_b.attack()
    
    


# In[99]:


for x in soldier_factory._soldier:
        print(x)
        v = [i for i in dir(soldier_factory._soldier[x]) if not i.startswith('__')]
        for y in v:
            print(y , getattr(soldier_factory._soldier[x] ,y))


# In[111]:


concrete_soldier_a.defen.__str__


# In[112]:


concrete_soldier_b.defen.__str__


# In[113]:


concrete_soldier_a.hp.__str__


# In[114]:


concrete_soldier_b.hp.__str__

