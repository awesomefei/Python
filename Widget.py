
# coding: utf-8

# In[1]:


from ipywidgets import *


# In[2]:


from IPython.display import display
w = IntSlider()
display(w)


# In[3]:


display(w)


# In[4]:


w.close()


# In[5]:


w.keys


# In[6]:


Text(value='Hello World!', disabled=True)


# In[8]:


Text(value='Hello World!', disabled=False)


# In[9]:


from traitlets import link
a = FloatText()
b = FloatSlider()
display(a,b)

mylink = link((a, 'value'), (b, 'value'))


# In[10]:


mylink.unlink()

