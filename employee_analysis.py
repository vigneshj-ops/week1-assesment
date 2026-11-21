#!/usr/bin/env python
# coding: utf-8

# # Employee Data Analysis
# 
# ## Week 1 Assessment - Task 4
# 
# ### Objective
# Analyze employee information using Python and Pandas.
# 
# ### Analysis Questions
# 1. How many employees are in the dataset?
# 2. What is the average salary?
# 3. Which department has the highest average salary?
# 4. How many employees work in each city?
# 5. What is the highest salary?

# In[2]:


import pandas as pd

print(pd.__version__)


# In[1]:


import sys
import os

print("Python location:", sys.executable)
print("Current folder:", os.getcwd())


# In[3]:


import sys

print(sys.executable)


# In[4]:


import os
print(os.getcwd())


# In[8]:


import pandas as pd
import os
import sys

print("Python:", sys.executable)
print("Current folder:", os.getcwd())

df = pd.read_csv("data/employees.csv")

display(df.head())


# In[1]:


import sys
print(sys.executable)


# In[2]:


import pandas as pd

df = pd.read_csv("data/employees.csv")

df.head()


# ## Dataset Information
# 
# This section explores the employee dataset.
# 

# In[3]:


df.info()


# ## Basic Statistical Analysis
# 
# This section calculates the average, minimum and maximum employee salaries.

# In[4]:


df.describe()


# ## Department-wise Salary Analysis
# 
# This section calculates the average salary for each department.

# In[5]:


department_salary = df.groupby("department")["salary"].mean()

print(department_salary)


# In[6]:


highest_department = department_salary.idxmax()

highest_salary = department_salary.max()

print("Highest-paying department:", highest_department)

print("Average salary:", highest_salary)


# ## City-wise Employee Analysis
# 
# This section counts employees working in each city.

# In[7]:


city_count = df["city"].value_counts()

print(city_count)


# In[8]:


print("Average salary:", df["salary"].mean())

print("Highest salary:", df["salary"].max())

print("Lowest salary:", df["salary"].min())


# ## Performance Measurement

# In[9]:


get_ipython().run_line_magic('timeit', 'df["salary"].mean()')


# In[ ]:




