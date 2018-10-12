
# coding: utf-8

# In[2]:


from proxy import Proxy, RealObject, ProxyImpl
import time


# In[17]:


if __name__ == '__main__':
    
    proxyStatus = True
    
    if proxyStatus: 
        obj = ProxyImpl(RealObject())
        obj.doone()
        try:
            obj.dotwo()
        except:
            print("u cant do two ... yikes")
    
    print("\nDisabled Proxy*\n")
    
    proxyStatus = False
    
    if not proxyStatus: 
        obj = RealObject()
        obj.doone()
        obj.dotwo()
        obj.dothree()

