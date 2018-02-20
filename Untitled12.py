
# coding: utf-8

# In[6]:


def checkvowels(word):
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    count = 0
    for i in vowels:
        if (word == i):
            count = count + 1
            break
    if (count >= 1):
        print('true')
    else:
        print('false')
x = input("Enter the single input character : ")
checkvowels(x)

