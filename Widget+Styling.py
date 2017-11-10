
# coding: utf-8

# In[1]:


get_ipython().run_cell_magic('html', '', '<style>\n.example-container { background: #999999; padding: 2px; min-height: 100px; }\n.example-container.sm { min-height: 50px; }\n.example-box { background: #9999FF; width: 50px; height: 50px; text-align: center; vertical-align: middle; color: white; font-weight: bold; margin: 2px;}\n.example-box.med { width: 65px; height: 65px; }   \n.example-box.lrg { width: 80px; height: 80px; }   \n</style>')


# In[2]:


import ipywidgets as widgets
from IPython.display import display


# In[3]:


#Basic styling


# In[4]:


button = widgets.Button(
    description='Hello World!',
    width=100, # Integers are interpreted as pixel measurements.
    height='2em', # em is valid HTML unit of measurement.
    color='lime', # Colors can be set by name,
    background_color='#0022FF', # and also by color code.
    border_color='cyan')
display(button)


# In[5]:


#Parent/child relationships


# In[6]:


from IPython.display import display

float_range = widgets.FloatSlider()
string = widgets.Text(value='hi')
container = widgets.Box(children=[float_range, string])

container.border_color = 'red'
container.border_style = 'dotted'
container.border_width = 3
display(container) # Displays the `container` and all of it's children.


# In[7]:


container = widgets.Box()
container.border_color = 'red'
container.border_style = 'dotted'
container.border_width = 3
display(container)

int_range = widgets.IntSlider()
container.children=[int_range]


# In[8]:


#Fancy boxes


# In[9]:


name1 = widgets.Text(description='Location:')
zip1 = widgets.BoundedIntText(description='Zip:', min=0, max=99999)
page1 = widgets.Box(children=[name1, zip1])

name2 = widgets.Text(description='Location:')
zip2 = widgets.BoundedIntText(description='Zip:', min=0, max=99999)
page2 = widgets.Box(children=[name2, zip2])

accord = widgets.Accordion(children=[page1, page2], width=400)
display(accord)

accord.set_title(0, 'From')
accord.set_title(1, 'To')


# In[10]:


name = widgets.Text(description='Name:', padding=4)
color = widgets.Dropdown(description='Color:', padding=4, options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'])
page1 = widgets.Box(children=[name, color], padding=4)

age = widgets.IntSlider(description='Age:', padding=4, min=0, max=120, value=50)
gender = widgets.RadioButtons(description='Gender:', padding=4, options=['male', 'female'])
page2 = widgets.Box(children=[age, gender], padding=4)

tabs = widgets.Tab(children=[page1, page2])
display(tabs)

tabs.set_title(0, 'Name')
tabs.set_title(1, 'Details')


# In[11]:


# Alignment


# In[12]:


display(widgets.Text(description="a:"))
display(widgets.Text(description="aa:"))
display(widgets.Text(description="aaa:"))


# In[13]:


display(widgets.Text(description="a:"))
display(widgets.Text(description="aa:"))
display(widgets.Text(description="aaa:"))
display(widgets.Text(description="aaaaaaaaaaaaaaaaaa:"))


# In[14]:


display(widgets.Text(description="a:"))
display(widgets.Text(description="aa:"))
display(widgets.Text(description="aaa:"))
display(widgets.Text())


# In[15]:


buttons = [widgets.Button(description=str(i)) for i in range(3)]
display(*buttons)


# In[16]:


container = widgets.HBox(children=buttons)
display(container)


# In[18]:


form = widgets.VBox()
first = widgets.Text(description="First:")
last = widgets.Text(description="Last:")

student = widgets.Checkbox(description="Student:", value=False)
school_info = widgets.VBox(visible=False, children=[
    widgets.Text(description="School:"),
    widgets.IntText(description="Grade:", min=0, max=12)
    ])

pet = widgets.Text(description="Pet:")
form.children = [first, last, student, school_info, pet]
display(form)

def on_student_toggle(name, value):
    if value:
        school_info.visible = True
    else:
        school_info.visible = False
student.on_trait_change(on_student_toggle, 'value')

