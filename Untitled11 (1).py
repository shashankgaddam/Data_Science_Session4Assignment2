
# coding: utf-8

# In[13]:


def filter_long_words(words):
    counter = list()
    for i in words:
        counter.append(len(i))
    return counter
l1= input("Enter the list of words : ")
new_list = l1.split(',')
print(filter_long_words(new_list))

