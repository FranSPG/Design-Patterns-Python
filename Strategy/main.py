
# coding: utf-8

# In[73]:


from strategy import strategyA, strategyB, strategy


# In[66]:


strA = strategyA
strB = strategyB


# In[67]:


class Context:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy
        
    def get_do(self):
        return self.strategy.do(strategy)
    


# In[68]:


if __name__ == '__main__':
    
    context = Context(strA)
    context.get_do()
    
    context.set_strategy(strB)
    context.get_do()

