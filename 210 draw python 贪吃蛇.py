
# coding: utf-8

# In[1]:


import turtle
turtle.setup(1000,600,100,100)
turtle.penup()
turtle.fd(-300)
turtle.pendown()
turtle.pensize(28)
turtle.pencolor("silver")
turtle.seth(-50)
for i in range(6):
    turtle.circle(50,60)
    turtle.pencolor("azure")
    turtle.circle(-50,60)
    turtle.pencolor("pink")
turtle.circle(50,60/2)
turtle.fd(50)
turtle.circle(25,180)
turtle.pencolor("rubine")
turtle.fd(50*2/3)

