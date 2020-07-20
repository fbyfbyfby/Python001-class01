import pandas as pd

# 1
data = pd.DataFrame()
# 2
data.iloc[:10, :]
# 3
data['id']
# 4
data['id'].count()
# 5
data[(data['id'] < 1000) & (data['age'] > 30)]
#6
data.groupby('id').agg({'order_id':'count'})
#7
pd.merge(table1, table2, on='id', how='inner')
#8
table1.append(table2)
#9
table1.drop(10)
#10
table1.drop('column_name',axis=1)