#!/usr/bin/env python
# coding: utf-8

# # Variable (변수)
# - 기호(=)를 통해서 변수를 할당한다.
# - 변수 생성 시 특수문자,공백,숫자부터 기입은 안된다.
# - 대소문자 구분한다.
# - _는 사용가능

# In[2]:


num=100
print('정수 형 변수 사용: %d'%num)
print('정수 형 변수 사용:',num)


# In[5]:


num=5
print('변경 전 num :',num)
num=num+10
print('변경 후 num :',num)


# In[7]:


num1=5
num2=10
sum_=num1+num2
print('두 수의 합 : ',sum_)


# In[8]:


num1=5
num2=10
sum_=num1+num2
print('id num1 : ',id(num1))
print('id num2 : ',id(num2))
print('id sum_ : ',id(sum_))


# In[10]:


num1=10
num2=20
print('num1(%d)+num2(%d)=%d'%(num1,num2,num1+num2))


# In[13]:


num1=7
num2=5
print('num1+num2=%d'%(num1+num2))
print('num1-num2=%d'%(num1-num2))
print('num1*num2=%d'%(num1*num2))
print('num1/num2=%d'%(num1/num2))


# ---

# In[17]:


def python_view(python_):
    return print('파이썬 %d점'%python_)


# In[18]:


def age_view(age):
    return print('나는 %d살이다.'%age)


# In[15]:


def mean_subject(python_,c_,java_):
    sum_=python_+c_+java_
    mean_=sum_/3
    return print('sum : %d\nmean : %.2f'%(sum_,mean_))


# In[19]:


python_view(100)


# In[20]:


age_view(26)


# In[21]:


mean_subject(100,100,100)


# # 소수점 수를 자르는 함수 (round)

# In[22]:


fit=123.567
print('round(fit) : ',round(fit))
print('round(fit,1) : ',round(fit,1))
print('round(fit,2) : ',round(fit,2))

