### Insert Data Columns in DataFrame

### Python pandas: remove everything after a delimiter in a string
df['text_new'] = df['text'].str.split('::').str[0]

df['text_new1'] = [x.split('::')[0] for x in df['text']]

### Subset Time Series By Dates Python Using Pandas

  #### Subset Pandas Dataframe Using Range of Dates
  df=df.set_index('date')
  df["begin_index_date" : "end_index_date]
  
  #### Subset Pandas Dataframe By Day of Month
  df.index.month == value
  
  #### Select data for 1st of month - view first rows
  boulder_precip_2003_2013[boulder_precip_2003_2013.index.day == 1]
  
  #### Subset Pandas Dataframe By Month
  df.index.month == value

  #### Select all December data - view first few rows
  boulder_precip_2003_2013[boulder_precip_2003_2013.index.month == 12].head()
 
  #### Subset Pandas Dataframe By Year
  df["index_date"]
  
  #### Select 2013 data - view first few records
  boulder_precip_2003_2013['2013'].head()
