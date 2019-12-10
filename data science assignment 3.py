
# coding: utf-8

# ---
# 
# _You are currently looking at **version 1.5** of this notebook. To download notebooks and datafiles, as well as get help on Jupyter notebooks in the Coursera platform, visit the [Jupyter Notebook FAQ](https://www.coursera.org/learn/python-data-analysis/resources/0dhYG) course resource._
# 
# ---

# # Assignment 3 - More Pandas
# This assignment requires more individual learning then the last one did - you are encouraged to check out the [pandas documentation](http://pandas.pydata.org/pandas-docs/stable/) to find functions or methods you might not have used yet, or ask questions on [Stack Overflow](http://stackoverflow.com/) and tag them as pandas and python related. And of course, the discussion forums are open for interaction with your peers and the course staff.

# ### Question 1 (20%)
# Load the energy data from the file `Energy Indicators.xls`, which is a list of indicators of [energy supply and renewable electricity production](Energy%20Indicators.xls) from the [United Nations](http://unstats.un.org/unsd/environment/excel_file_tables/2013/Energy%20Indicators.xls) for the year 2013, and should be put into a DataFrame with the variable name of **energy**.
# 
# Keep in mind that this is an Excel file, and not a comma separated values file. Also, make sure to exclude the footer and header information from the datafile. The first two columns are unneccessary, so you should get rid of them, and you should change the column labels so that the columns are:
# 
# `['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable']`
# 
# Convert `Energy Supply` to gigajoules (there are 1,000,000 gigajoules in a petajoule). For all countries which have missing data (e.g. data with "...") make sure this is reflected as `np.NaN` values.
# 
# Rename the following list of countries (for use in later questions):
# 
# ```"Republic of Korea": "South Korea",
# "United States of America": "United States",
# "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
# "China, Hong Kong Special Administrative Region": "Hong Kong"```
# 
# There are also several countries with numbers and/or parenthesis in their name. Be sure to remove these, 
# 
# e.g. 
# 
# `'Bolivia (Plurinational State of)'` should be `'Bolivia'`, 
# 
# `'Switzerland17'` should be `'Switzerland'`.
# 
# <br>
# 
# Next, load the GDP data from the file `world_bank.csv`, whixch is a csv containing countries' GDP from 1960 to 2015 from [World Bank](http://data.worldbank.org/indicator/NY.GDP.MKTP.CD). Call this DataFrame **GDP**. 
# 
# Make sure to skip the header, and rename the following list of countries:
# 
# ```"Korea, Rep.": "South Korea", 
# "Iran, Islamic Rep.": "Iran",
# "Hong Kong SAR, China": "Hong Kong"```
# 
# <br>
# 
# Finally, load the [Sciamgo Journal and Country Rank data for Energy Engineering and Power Technology](http://www.scimagojr.com/countryrank.php?category=2102) from the file `scimagojr-3.xlsx`, which ranks countries based on their journal contributions in the aforementioned area. Call this DataFrame **ScimEn**.
# 
# Join the three datasets: GDP, Energy, and ScimEn into a new dataset (using the intersection of country names). Use only the last 10 years (2006-2015) of GDP data and only the top 15 countries by Scimagojr 'Rank' (Rank 1 through 15). 
# 
# The index of this DataFrame should be the name of the country, and the columns should be ['Rank', 'Documents', 'Citable documents', 'Citations', 'Self-citations',
#        'Citations per document', 'H index', 'Energy Supply',
#        'Energy Supply per Capita', '% Renewable', '2006', '2007', '2008',
#        '2009', '2010', '2011', '2012', '2013', '2014', '2015'].
# 
# *This function should return a DataFrame with 20 columns and 15 entries.*

# In[5]:


import pandas as pd
import numpy as np


# In[6]:





energy = pd.read_excel('Energy Indicators.xls',header=None)

    


# In[7]:



energy.columns = ['a','b','Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable']


# In[8]:










energy.drop(energy.columns[0:2], axis=1, inplace =True)


# In[9]:



energy_1=energy.iloc[18:245,]


# In[10]:







energy_1=energy_1.replace('...',np.nan)


# In[11]:








energy_1['Energy Supply'] = energy_1['Energy Supply']*1000000


# In[12]:


country = []


# In[13]:


for name in energy_1['Country']:
    head, sep, tail = name.partition("(")
    country.append(head)


# In[14]:


energy_1.drop(energy_1.columns[0:1], axis=1, inplace =True)


# In[15]:


country_1=[]
for name in country:
    name=''.join(c if c not in map(str,range(0,10)) else "" for c in name)
    country_1.append(name)


# In[16]:


energy_1['Country'] = country_1


# In[17]:


energy_1 = energy_1.replace("Korea, Rep.","South Korea")
energy_1 = energy_1.replace("United States of America", "United States")
energy_1 = energy_1.replace("United Kingdom of Great Britain and Northern ireland", "United Kingdom")


# In[18]:


energy_1 = energy_1.set_index('Country')


# # GDP

# In[19]:



df = pd.read_csv('world_bank.csv',header =None)


# In[20]:


GDP=df.iloc[5:268,]


# In[21]:


GDP = GDP.rename(columns = {0:'Country'})


# In[22]:


GDP = GDP.replace("Korea, Rep.", "South Korea")
GDP = GDP.replace("Iran, Islamic Rep.", "Iran",)
GDP = GDP.replace("Hong Kong SAR, China", "Hong Kong")


# In[23]:








GDP = GDP.set_index('Country') 


# In[24]:


GDP =GDP.iloc[:,49:59]


# In[25]:


GDP.columns = ['2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']


# # ScimEn

# In[26]:


ScinEn = pd.read_excel('scimagojr-3.xlsx', header = None)


# In[27]:





ScinEn = ScinEn.iloc[0:16]


# In[28]:


ScinEn.columns = ['Rank','Country','Documents','Citable documents','Citations','Self-citations','Citations per document','H index']


# In[29]:


ScinEn = ScinEn.iloc[1:16]


# In[30]:


ScinEn = ScinEn.set_index('Country')


# In[31]:



data_frames=[energy_1,GDP,ScinEn]
result = pd.concat(data_frames, axis=1, join_axes =[ScinEn.index])


# In[32]:


result = result.sort('Rank')


# In[33]:



result = result.iloc[0:15]


# In[34]:



result


# ### Question 2 (6.6%)
# The previous question joined three datasets then reduced this to just the top 15 entries. When you joined the datasets, but before you reduced this to the top 15 items, how many entries did you lose?
# 
# *This function should return a single number.*

# In[35]:



get_ipython().run_cell_magic('HTML', '', '<svg width="800" height="300">\n  <circle cx="150" cy="180" r="80" fill-opacity="0.2" stroke="black" stroke-width="2" fill="blue" />\n  <circle cx="200" cy="100" r="80" fill-opacity="0.2" stroke="black" stroke-width="2" fill="red" />\n  <circle cx="100" cy="100" r="80" fill-opacity="0.2" stroke="black" stroke-width="2" fill="green" />\n  <line x1="150" y1="125" x2="300" y2="150" stroke="black" stroke-width="2" fill="black" stroke-dasharray="5,3"/>\n  <text  x="300" y="165" font-family="Verdana" font-size="35">Everything but this!</text>\n</svg>')


# In[36]:


def answer_two():
    e1, e2 = energy_1.shape
    g1, g2 = GDP.shape
    s1, s2 = ScinEn.shape
    r1, r2 = result.shape
    return  e1*e2+g1*g2+s1*s2-r1*r2
answer_two()


# ## Answer the following questions in the context of only the top 15 countries by Scimagojr Rank (aka the DataFrame returned by `answer_one()`)

# ### Question 3 (6.6%)
# What is the average GDP over the last 10 years for each country? (exclude missing values from this calculation.)
# 
# *This function should return a Series named `avgGDP` with 15 countries and their average GDP sorted in descending order.*

# In[37]:



def answer_three():
    result['average']= (result['2006']+result['2007']+result['2008']+result['2009']+result['2010']+result['2011']+result['2012']+result['2013']+result['2014']+result['2015'])/10
    
    return  result.average.sort_values(ascending = False)
answer_three()


# ### Question 4 (6.6%)
# By how much had the GDP changed over the 10 year span for the country with the 6th largest average GDP?
# 
# *This function should return a single number.*

# In[38]:



def answer_four():
    result_1=result.iloc[3:4]
    return  result_1['2015']-result_1['2006']
answer_four()


# ### Question 5 (6.6%)
# What is the mean `Energy Supply per Capita`?
# 
# *This function should return a single number.*

# In[39]:


def answer_five():
    #result.loc[:," Energy Supply per Capita"].mean()
    return result.loc[:,"Energy Supply per Capita"].mean()
answer_five()


# ### Question 6 (6.6%)
# What country has the maximum % Renewable and what is the percentage?
# 
# *This function should return a tuple with the name of the country and the percentage.*

# In[40]:


def answer_six():
    
    return result['% Renewable'].max()
answer_six()


# ### Question 7 (6.6%)
# Create a new column that is the ratio of Self-Citations to Total Citations. 
# What is the maximum value for this new column, and what country has the highest ratio?
# 
# *This function should return a tuple with the name of the country and the ratio.*

# In[41]:


def answer_seven():
    result['ratio'] = result['Self-citations']/result['Citations']
    return result['ratio'].max()
answer_seven()


# ### Question 8 (6.6%)
# Create a new column with a 1 if the country's % Renewable value is at or above the median for all countries in the top 15, and a 0 if the country's % Renewable value is below the median.
# 
# *This function should return a series named `HighRenew` whose index is the country name sorted in ascending order of rank.*

# In[42]:


def answer_eight():
    HighRenew = []
    x=result['% Renewable'].median()
    for number in result['% Renewable']:
        if number >=x:
            HighRenew.append(1)
        else:
             HighRenew.append(0)
    result['highRenew'] = HighRenew
    cols = result.columns.tolist()
    cols = cols[-1:] + cols[:-1]
    return  result[cols].iloc[:,0:1]
answer_eight()


# ### Question 11 (6.6%)
# Use the following dictionary to group the Countries by Continent, then create a dateframe that displays the sample size (the number of countries in each continent bin), and the sum, mean, and std deviation for the estimated population of each country.
# 
# ```python
# ContinentDict  = {'China':'Asia', 
#                   'United States':'North America', 
#                   'Japan':'Asia', 
#                   'United Kingdom':'Europe', 
#                   'Russian Federation':'Europe', 
#                   'Canada':'North America', 
#                   'Germany':'Europe', 
#                   'India':'Asia',
#                   'France':'Europe', 
#                   'South Korea':'Asia', 
#                   'Italy':'Europe', 
#                   'Spain':'Europe', 
#                   'Iran':'Asia',
#                   'Australia':'Australia', 
#                   'Brazil':'South America'}"
# ```
# 
# *This function should return a DataFrame with index named Continent `['Asia', 'Australia', 'Europe', 'North America', 'South America']` and columns `['size', 'sum', 'mean', 'std']`*

# In[80]:


def answer_eleven():
    result['Continent']= ['Asia','North America','Asia','Europe','Europe','North America', 'Europe','Asia', 'Europe','Asia','Europe','Europe','Asia','Australia','South America']
    result['Population']= result['Energy Supply']/result['Energy Supply per Capita']
    new = result.reset_index()
    mean = new.groupby(['Continent'])['Population'].mean()
    std = new.groupby(['Continent'])['Population'].std()
    add = new.groupby(['Continent'])['Population'].sum()
    data_frames_1=[mean,std,add]
    df = pd.concat(data_frames_1, axis=1, join = 'outer')
    df.columns=['mean','std','sum']
    return df
answer_eleven()


# ### Question 12 (6.6%)
# Cut % Renewable into 5 bins. Group Top15 by the Continent, as well as these new % Renewable bins. How many countries are in each of these groups?
# 
# *This function should return a __Series__ with a MultiIndex of `Continent`, then the bins for `% Renewable`. Do not include groups with no countries.*

# In[ ]:


def answer_twelve():
    Top15 = answer_one()
    return "ANSWER"


# ### Question 13 (6.6%)
# Convert the Population Estimate series to a string with thousands separator (using commas). Do not round the results.
# 
# e.g. 317615384.61538464 -> 317,615,384.61538464
# 
# *This function should return a Series `PopEst` whose index is the country name and whose values are the population estimate string.*

# In[ ]:


def answer_thirteen():
    Top15 = answer_one()
    return "ANSWER"


# ### Optional
# 
# Use the built in function `plot_optional()` to see an example visualization.

# In[ ]:


def plot_optional():
    import matplotlib as plt
    get_ipython().magic('matplotlib inline')
    Top15 = answer_one()
    ax = Top15.plot(x='Rank', y='% Renewable', kind='scatter', 
                    c=['#e41a1c','#377eb8','#e41a1c','#4daf4a','#4daf4a','#377eb8','#4daf4a','#e41a1c',
                       '#4daf4a','#e41a1c','#4daf4a','#4daf4a','#e41a1c','#dede00','#ff7f00'], 
                    xticks=range(1,16), s=6*Top15['2014']/10**10, alpha=.75, figsize=[16,6]);

    for i, txt in enumerate(Top15.index):
        ax.annotate(txt, [Top15['Rank'][i], Top15['% Renewable'][i]], ha='center')

    print("This is an example of a visualization that can be created to help understand the data. This is a bubble chart showing % Renewable vs. Rank. The size of the bubble corresponds to the countries' 2014 GDP, and the color corresponds to the continent.")


# In[ ]:


#plot_optional() # Be sure to comment out plot_optional() before submitting the assignment!

