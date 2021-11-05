#!/usr/bin/env python
# coding: utf-8

# In[9]:


import random
when = ['A few years ago', 'Yesterday', 'Last night', 'A long time ago','On 20th Jan']
who = ['a Data Scientist', 'a teacher', 'a doctor', 'an Accountant','a salesperson']
name = ['Joy', 'Nidhi','Akash', 'Alok', 'Joita']
residence = ['Dumdum','Tollygaunj', 'Beadon Row', 'Shyambazar', 'Laketown']
went = ['cinema', 'university','seminar', 'school', 'laundry']
happened = ['made a lot of friends','Eats a burger', 'found a secret key', 'solved a mistery', 'wrote a book']
print(random.choice(when) + ', '+ random.choice(name)+ ', ' + random.choice(who) + ' that lived in ' + random.choice(residence) + ', went to the ' + random.choice(went) + ' and ' + random.choice(happened))


# In[ ]:




