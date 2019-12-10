#!/usr/bin/env python
# coding: utf-8

# In[99]:


import pandas as pd


# In[100]:


from sklearn.linear_model import LogisticRegression


# In[101]:


from sklearn.model_selection import cross_val_score


# In[102]:


dataset=pd.read_csv('dataset.csv')


# In[103]:


test=pd.read_csv('test.csv')


# In[104]:


dataset


# In[105]:


test.head()


# In[106]:


name=test.name


# In[107]:


dataset.drop(dataset.columns[0:2],axis=1,inplace=True)


# In[108]:


test.drop(test.columns[0:2],axis=1,inplace=True)


# In[109]:


dataset=dataset.dropna()


# In[110]:


test=test.dropna()


# In[117]:


dataset=dataset.drop(['phone'],axis=1)


# In[118]:


test=test.drop(['phone'],axis=1)


# In[119]:


from sklearn.preprocessing import LabelEncoder

lb_make = LabelEncoder()
dataset["location_code"] = lb_make.fit_transform(dataset["location"])


# In[120]:




test["location_code"] = lb_make.fit_transform(test["location"])


# In[121]:


test.head()


# In[122]:


dataset=dataset.drop(['location'],axis=1)


# In[123]:


test=test.drop(['name'],axis=1)


# In[124]:


test.head(5)


# In[125]:


dataset["online_order"] = lb_make.fit_transform(dataset["online_order"])


# In[126]:


test["online_order"] = lb_make.fit_transform(test["online_order"])


# In[127]:


dataset["Indian"] = lb_make.fit_transform(dataset["Indian"])


# In[128]:


test["Indian"] = lb_make.fit_transform(test["Indian"])


# In[129]:


dataset["North Indian"] = lb_make.fit_transform(dataset["North Indian"])


# In[130]:


test["North Indian"] = lb_make.fit_transform(test["North Indian"])


# In[131]:





dataset["Chinese"] = lb_make.fit_transform(dataset["Chinese"])


# In[132]:


test["Chinese"] = lb_make.fit_transform(test["Chinese"])


# In[133]:


dataset["South Indian"] = lb_make.fit_transform(dataset["South Indian"])


# In[134]:


test["South Indian"] = lb_make.fit_transform(test["South Indian"])


# In[135]:


dataset["Fast Food"] = lb_make.fit_transform(dataset["Fast Food"])


# In[136]:


test["Fast Food"] = lb_make.fit_transform(test["Fast Food"])


# In[137]:


dataset["Biryani"] = lb_make.fit_transform(dataset["Biryani"])


# In[138]:


test["Biryani"] = lb_make.fit_transform(test["Biryani"])


# In[139]:


dataset["Desserts"] = lb_make.fit_transform(dataset["Desserts"])


# In[140]:


test["Desserts"] = lb_make.fit_transform(test["Desserts"])


# In[141]:


dataset["Continental"] = lb_make.fit_transform(dataset["Continental"])


# In[142]:


test["Continental"] = lb_make.fit_transform(test["Continental"])


# In[143]:



dataset["Cafe"] = lb_make.fit_transform(dataset["Cafe"])


# In[144]:


test["Cafe"] = lb_make.fit_transform(test["Cafe"])


# In[145]:


dataset["Beverages"] = lb_make.fit_transform(dataset["Beverages"])


# In[146]:



test["Beverages"] = lb_make.fit_transform(test["Beverages"])


# In[147]:


dataset["Italian"] = lb_make.fit_transform(dataset["Italian"])


# In[148]:


test["Italian"] = lb_make.fit_transform(test["Italian"])


# In[149]:


dataset["Street Food"] = lb_make.fit_transform(dataset["Street Food"])


# In[150]:


test["Street Food"] = lb_make.fit_transform(test["Street Food"])


# In[151]:


dataset["Bakery"] = lb_make.fit_transform(dataset["Bakery"])


# In[152]:


test["Bakery"] = lb_make.fit_transform(test["Bakery"])


# In[153]:


dataset["rest_type"] = lb_make.fit_transform(dataset["rest_type"])


# In[154]:


test["rest_type"] = lb_make.fit_transform(test["rest_type"])


# In[155]:


dataset["book_table"] = lb_make.fit_transform(dataset["book_table"])


# In[156]:


test["book_table"] = lb_make.fit_transform(test["book_table"])


# In[157]:


dataset["approx_cost.for.two.people."] = lb_make.fit_transform(dataset["approx_cost.for.two.people."])


# In[158]:


test["approx_cost.for.two.people."] = lb_make.fit_transform(test["approx_cost.for.two.people."])


# In[159]:


X=dataset.drop(['rating'],axis=1)


# In[160]:


X.head()


# In[161]:


X=X.drop(["name"],axis=1)


# In[162]:


Y=dataset['rating']


# In[163]:


import numpy as np


# In[164]:


a = np.quantile(Y,0.7)


# In[165]:


outcome = [Y>3.9]


# In[166]:


type(outcome)


# In[167]:


result=np.array(outcome)


# In[168]:


u = pd.DataFrame(result)


# In[169]:


u = lb_make.fit_transform(u.T)


# In[170]:


u


# In[171]:


LG = LogisticRegression()


# In[172]:


LG.fit(X,u.T)


# In[173]:


X.corr()


# In[174]:


X.head()


# In[175]:


test=test.drop(['location'],axis=1)


# In[176]:


Y_prediction=LG.predict_proba(test)[:,1]


# In[177]:


Y_prediction


# In[178]:


b = np.quantile(Y_prediction,0.8)


# In[179]:


b


# In[180]:


outcome=[Y_prediction>b]


# In[181]:


outcome


# In[191]:


result=pd.DataFrame(outcome)


# In[192]:


result=result.T


# In[198]:


result


# In[202]:


result.columns=["rating"]


# In[203]:


result


# In[220]:


result["rating"] = lb_make.fit_transform(result["rating"])


# In[228]:


list=[]
for rating in result.rating:
    if rating == 1:
        list.append("Good")
    else:
        list.append("NotGood")


# In[229]:


list


# In[231]:


result['Rating']=list


# In[236]:


result=result.drop(['rating'],axis=1)


# In[237]:


result['name']=name


# In[239]:


result.set_index('name')


# In[239]:


result.set_index('name')


# In[239]:


result.set_index('name')


# In[239]:


result.set_index('name')

