
# coding: utf-8

# In[1]:


from __future__ import print_function
import ipywidgets as widgets
print(widgets.Button.on_click.__doc__)


# In[2]:


from IPython.display import display
button = widgets.Button(description="Click Me!")
display(button)

def on_button_clicked(b):
    print("Button clicked.")

button.on_click(on_button_clicked)


# In[3]:


text = widgets.Text()
display(text)

def handle_submit(sender):
    print(text.value)

text.on_submit(handle_submit)


# In[4]:


print(widgets.Widget.on_trait_change.__doc__)


# In[13]:


int_range = widgets.IntSlider()
display(int_range)

def on_value_change(name, value):
    print(value)

int_range.observe(on_value_change, 'value')


# In[6]:


import traitlets


# In[7]:


# Create Caption
caption = widgets.Label(value = 'The values of slider1 and slider2 are synchronized')

# Create IntSlider
slider1 = widgets.IntSlider(description='Slider 1')
slider2 =  widgets.IntSlider(description='Slider 2')

# Use trailets to link
l = traitlets.link((slider1, 'value'), (slider2, 'value'))

# Display!
display(caption, slider1, slider2)


# In[8]:


# Create Caption
caption = widgets.Label(value = 'Changes in source values are reflected in target1')

# Create Sliders
source = widgets.IntSlider(description='Source')
target1 = widgets.IntSlider(description='Target 1')

# Use dlink
dl = traitlets.dlink((source, 'value'), (target1, 'value'))
display(caption, source, target1)


# In[9]:


# May get an error depending on order of cells being run!
l.unlink()
dl.unlink()


# In[10]:


# NO LAG VERSION
caption = widgets.Label(value = 'The values of range1 and range2 are synchronized')

range1 = widgets.IntSlider(description='Range 1')
range2 =  widgets.IntSlider(description='Range 2')

l = widgets.jslink((range1, 'value'), (range2, 'value'))
display(caption, range1, range2)


# In[11]:


# NO LAG VERSION
caption = widgets.Label(value = 'Changes in source_range values are reflected in target_range1')

source_range = widgets.IntSlider(description='Source range')
target_range1 = widgets.IntSlider(description='Target range ')

dl = widgets.jsdlink((source_range, 'value'), (target_range1, 'value'))
display(caption, source_range, target_range1)


# In[ ]:


l.unlink()
dl.unlink()

