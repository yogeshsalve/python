#!/usr/bin/env python
# coding: utf-8

# **Basics of python**

# In[1]:


# variable assignment of Integer Numbers
x = 4
y = 2

# Showing Addition of two variables
print(x + y)


# In[2]:


# variables assignment of Floating point numbers
x = 4.0
y = 2.0

# Showing Addition
print(x + y)

# ShowingSubtraction
print(x - y)

# Showing Multiplication
print(x * y)

# Returning the quotient
print(x / y)

# Returning the remainder
print(x % y) 

# Giving Absolute value
print(abs(x))

# Showing x to the power y
print(x ** y)


# In[14]:


# variable assignment of Strings
x = 'Yogesh'
y = 'Salve'

# Concatenation of Strings 
print(x + ' ' + y)

# Repeating String
print(x * 2)


# In[15]:


# Slicing of Strings
myName = 'Yogesh'
z1 = myName[1:] 
print(z1)

z2 = myName[0] + myName[5] 
print(z2)


# In[11]:


# Addition of String
x = '2'
y = '1'

x + y


# In[16]:


str.capitalize('elephant')


# In[20]:


str1 = "I love my India"
str2 = "515"
len(str1)


# In[18]:


str1.isdigit()


# In[21]:


str2.isdigit()


# In[31]:


str3 = 'Respect'
str1.replace('love', str3)


# In[34]:


str1.find('my')


# In[35]:


# Boolean operations
x = 4
y = 4
z = (x==y) # Comparison expression (Evaluates to false)
if z: # Conditional on truth/false value of 'z'
    print("We want to be a Data Scientists")
else: print("We DO not want to be a Data Scientists")


# In[36]:


# Implicit Conversions
# A float
x = 6.0 

# An integer
y = 3 

# Divide `x` by `y`
z = x/y

# Check the type of `z`
type(z)


# In[38]:


x = 8
y = "My Favourite no. is: "
fav_no = (y) + str(x)
print(fav_no)

