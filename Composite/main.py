
# coding: utf-8

# In[1]:


from composite import Component, Leaf, Composite


# In[6]:


if __name__ == '__main__':

    composite = Composite()
    leaf1 = Leaf('leaf1')
    leaf2 = Leaf('leaf2')
    leaf3 = Leaf('leaf3')
    leaf4 = Leaf('leaf4')
    
    print('Adding leafs')
    
    composite.add(leaf1)
    composite.add(leaf2)
    composite.add(leaf3)
    composite.add(leaf4)
    composite.do()


    print('\nRemoving some leafs')
    composite.remove(leaf3)
    composite.remove(leaf1)
    composite.do()

