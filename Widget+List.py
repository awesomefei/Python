
# coding: utf-8

# In[1]:


import ipywidgets as widgets


# In[3]:


widgets.FloatSlider(
    value=7.5,
    min=5.0,
    max=10.0,
    step=0.1,
    description='Test:',
)


# In[4]:


widgets.FloatSlider(
    value=7.5,
    min=5.0,
    max=10.0,
    step=0.1,
    description='Test',
    orientation='vertical',
)


# In[5]:


widgets.FloatProgress(
    value=7.5,
    min=5.0,
    max=10.0,
    step=0.1,
    description='Loading:',
)


# In[6]:


widgets.BoundedFloatText(
    value=7.5,
    min=5.0,
    max=10.0,
    description='Text:',
)


# In[7]:


widgets.FloatText(
    value=7.5,
    description='Any:',
)


# In[8]:


widgets.ToggleButton(
    description='Click me',
    value=False,
)


# In[9]:


widgets.Checkbox(
    description='Check me',
    value=True,
)


# In[10]:


widgets.Valid(
    value=True,
)


# In[11]:


# selection widgets
# dropdown
from IPython.display import display

w = widgets.Dropdown(
    options=['1', '2', '3'],
    value='2',
    description='Number:',
)
display(w)


# In[13]:


# Show value
w.value


# In[14]:


# the following is also valid
w = widgets.Dropdown(
    options={'One': 1, 'Two': 2, 'Three': 3},
    value=2,
    description='Number:')

display(w)


# In[16]:


w.value


# In[17]:


# RadioButtons


# In[18]:


widgets.RadioButtons(
    description='Pizza topping:',
    options=['pepperoni', 'pineapple', 'anchovies'],
)


# In[19]:


#Select
widgets.Select(
    description='OS:',
    options=['Linux', 'Windows', 'OSX'],
)


# In[20]:


# ToggleButtons


# In[21]:


widgets.ToggleButtons(
    description='Speed:',
    options=['Slow', 'Regular', 'Fast'],
)


# In[23]:


# SelectMultiple
w = widgets.SelectMultiple(
    description="Fruits",
    options=['Apples', 'Oranges', 'Pears'])

display(w)


# In[25]:


w.value


# In[26]:


# String widgets


# In[27]:


widgets.Text(
    description='String:',
    value='Hello World',
)


# In[28]:


widgets.Textarea(
    description='String:',
    value='Hello World',
)


# In[30]:


widgets.HTML(
    value="Hello <b>World</b>"
)


# In[31]:


widgets.Button(description='Click me')

