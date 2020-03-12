
# coding: utf-8

# In[33]:


import omdb
from omdb import OMDBClient
import pandas as pd


# In[27]:


my_client = OMDBClient(apikey='a6d9196b')
OMDB_Info_List = []


# In[28]:


def collect_OMDB_Info(keyword):
    data = my_client.search(keyword)
    Titles = []
    Years = []
    IMDB_IDs = []
    Types = []
    for i in range(len(data)):
        Titles.append(data[i]['title'])
        Years.append(data[i]['year'])
        IMDB_IDs.append(data[i]['imdb_id'])
        Types.append(data[i]['type'])
        
    for i in range(len(data)):
        temp = str(Years[i])
        temp = temp.replace('–','')
        Years[i] = int(temp) 
    
    for i in range(len(data)):
        temp = []
        temp.append(Titles[i])
        temp.append(Years[i])
        temp.append(IMDB_IDs[i])
        temp.append(Types[i])
        OMDB_Info_List.append(temp)
        
    
    
    









# In[31]:


Keywords = ["Canada","University","Moncton","Halifax","Toronto","Vancouver","Alberta","Niagara"]

for key in Keywords:
    collect_OMDB_Info(key)


# In[35]:


cols = ['Title','Year','IMDB_ID','Type']
OMDB_df = pd.DataFrame(OMDB_Info_List,columns=cols)
OMDB_df.to_json("Extracted_OMDB_Data.json",orient="records",lines=True)

