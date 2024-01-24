#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df=pd.read_csv("salesdata.csv") 


# In[3]:


df


# In[4]:


df.describe()


# In[5]:


df["Market"].describe()


# In[6]:


df["Market"].value_counts()


# In[7]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[8]:


sns.barplot(x='Market',y='Quantity',data=df)
plt.title('Sales by Market')
plt.show()


# In[9]:


df['Sales'] = pd.to_numeric(df['Sales'].replace('[\$,]', '', regex=True))


# In[10]:


grouped_df = df.groupby(['Market'])['Sales'].sum().reset_index()
grouped_df['Sales'] = grouped_df['Sales'] / 1000000


# In[11]:


ax=sns.barplot(x='Market', y='Sales', data=grouped_df, palette='viridis')
plt.title('Sum of Sales in Different Markets')
plt.xlabel('Market')
plt.ylabel('Total Sales')
plt.show()


# In[12]:


df_sorted = df.sort_values(by='Sales', ascending=False)
top_5_countries = df_sorted.head


# In[13]:


grouped_df =df.groupby(['Country'])['Sales'].sum().reset_index()


# In[14]:


dff2=grouped_df.sort_values(by='Sales', ascending=False).head(10)


# In[15]:


sns.barplot(x='Country', y='Sales', data=dff2)
plt.title('Total Sales by Country')
plt.xticks(rotation=90, ha='center')
plt.show


# In[16]:


df_sorted = df.sort_values(by='Sales', ascending=False)
grouped_df1 = df_sorted.groupby(['Region'])['Sales'].sum().reset_index()


# In[17]:


grouped_df1.sort_values(by='Sales', ascending=False)


# In[18]:


sns.barplot(x='Region', y='Sales', data=grouped_df1)
plt.title('Total Sales by Region')
plt.xticks(rotation=90, ha='center')


# In[19]:


df_aggregated = df.groupby('Segment')['Sales'].sum().reset_index()
sns.barplot(x='Segment', y='Sales', data=df_aggregated, palette='viridis')
plt.title('Total Sales by Customer Segment')
plt.xlabel('Customer Segment')
plt.ylabel('Total Sales')
plt.show()


# In[20]:


plt.figure(figsize=(8, 6))
sns.boxplot(x=df['Sales'])
plt.title('Box Plot of Sales')
plt.show()


# In[21]:


plt.figure(figsize=(8, 6))
sns.histplot(df['Sales'], kde=True)
plt.title('Histogram of Sales')
plt.xlabel('Sales')
plt.ylabel('Frequency')
plt.show()


# In[22]:


print(df['Ship Mode'].unique())


# In[23]:


print(df['Market'].unique())


# In[24]:


print(df['Region'].unique())


# In[25]:


print(df['Order Priority'].unique())


# In[26]:


duplicate_customers = df[df.duplicated(subset='Row ID', keep=False)]


# In[27]:


duplicate_customers


# In[28]:


missing_values = df[['Sales', 'Quantity', 'Profit']].isnull().sum()
print(missing_values)


# In[29]:


missing_values = df[['Category', 'Sub-Category', 'Ship Mode']].isnull().sum()
print(missing_values)


# In[30]:


print(df[['Order Date', 'Ship Date']].dtypes)


# In[31]:


df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
df['Ship Date'] = pd.to_datetime(df['Ship Date'], errors='coerce')


# In[32]:


df['Order Year'] = df['Order Date'].dt.year


# In[33]:


df['Order Year']


# In[34]:


sns.histplot(df['Order Date'], bins=30, kde=True)
plt.xticks(rotation=90, ha='center')


# In[35]:


df


# In[36]:


shipping_and_order = df[['Shipping Cost', 'Ship Mode', 'Order Priority']]


# In[37]:


correlation_matrix = shipping_and_order.corr()


# In[38]:


df_aggregated = df.groupby('Category')['Sales'].sum().reset_index()
df_aggregated['Sales'] = df_aggregated['Sales'] / 1000000
sns.barplot(x='Category', y='Sales', data=df_aggregated)
plt.title('Total Sales by category')
plt.xlabel('Category')
plt.ylabel('Total Sales')
plt.show()


# In[39]:


df['Profit'] = pd.to_numeric(df['Profit'].replace('[\$,]', '', regex=True)) 


# In[40]:


df_aggregate = df.groupby('Category')['Profit'].sum().reset_index()
sns.barplot(x='Category', y='Profit', data=df_aggregate, palette='viridis')
plt.title('profit by category')
plt.xlabel('Category')
plt.ylabel('Total Sales')
plt.show()


# In[41]:


df_aggregate


# In[42]:


df_aggregated1 = df.groupby('Category')['Quantity'].sum().reset_index()
sns.barplot(x='Category', y='Quantity', data=df_aggregated1)
plt.title('Quantity  by category')
plt.xlabel('Category')
plt.ylabel('total item sold')
plt.show()


# In[43]:


df_sorted = df.sort_values(by='Sales', ascending=False)
top_5_countries = df_sorted.head(20)
grouped_df = df.groupby(['Sub-Category'])['Sales'].sum().reset_index()


# In[44]:


grouped_df3 = df.groupby(['Sub-Category'])['Sales'].sum().reset_index()
grouped_df3['Sales'] = grouped_df3['Sales'] / 1000000
sns.barplot(x='Sub-Category', y='Sales', data=grouped_df3)
plt.title('Sales by Sub-Category ')
plt.xlabel('Sub-Category')
plt.xticks(rotation=90, ha='center')
plt.show()


# In[45]:


grouped_df3


# In[46]:


dff=df.sort_values(by='Sales', ascending=False).head(10)
sns.barplot(x='Product Name', y='Sales', data=dff)
plt.title('top 10 products ')
plt.xlabel('products')
plt.xticks(rotation=90, ha='center')
plt.show()


# In[47]:


correlation_matrix = df[['Profit', 'Discount']].corr()


# In[48]:


correlation_matrix


# In[49]:


sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix')
plt.show()


# In[50]:


df3 = df.groupby(['Order Priority'])['Sales'].sum().reset_index()
sns.barplot(x='Order Priority', y='Sales', data=df3)
plt.title('Sales by order periority')
plt.show()


# In[51]:


sns.scatterplot(x='Shipping Cost', y='Sales', data=df, hue='Order Priority')
plt.show


# In[52]:


df


# In[53]:


corr_sales=df[['Sales','Profit', 'Quantity']].corr()


# In[54]:


corr_sales


# In[55]:


sns.heatmap(corr_sales, annot=True, cmap='coolwarm', fmt=".2f")


# In[56]:


sns.scatterplot(x='Discount', y='Profit', data=df)
plt.title('Scatter Plot of Profit vs Discount')
plt.xlabel('Discount')
plt.ylabel('Profit')
plt.show()


# In[57]:


segmented_data = df.groupby('Segment')['Sales'].sum().reset_index()


# In[58]:


segmented_data


# In[59]:


sns.barplot(x='Segment', y='Sales', data=segmented_data)
plt.title('Sales by Customer Segment')
plt.xlabel('Customer Segment')
plt.ylabel('Mean Sales')
plt.show()


# In[60]:


category_performance = df.groupby(['Category', 'Order Date'])['Sales'].sum().reset_index()


# In[61]:


category_performance_pivot = category_performance.pivot(index='Order Date', columns='Category', values='Sales').fillna(0)


# In[62]:


category_performance_pivot


# In[63]:


df['Order Year'] = df['Order Date'].dt.year


# In[64]:


df['Order Year'].unique()


# In[65]:


category_performance = df.groupby(['Category', 'Order Year'])['Sales'].sum().reset_index()


# In[66]:


category_performance


# In[67]:


sns.lineplot(x='Order Year', y='Sales', hue='Category', data=category_performance)
plt.legend(title='Category', loc='upper left', bbox_to_anchor=(1, 1))
plt.show()


# In[68]:


sns.barplot(x='Order Year', y='Sales', hue='Category', data=category_performance)
plt.show


# In[ ]:





# In[ ]:





# In[ ]:





# In[69]:


file_path = 'C:\projects\power bi projects\HR Attrition/clean_data.csv'
df.to_csv(file_path, index=False)
print(f'Data has been saved to CSV: {file_path}')


# In[70]:


df


# In[ ]:




