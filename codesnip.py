from copy import deepcopy
myCopy = deepcopy(myDict)

# if col2 is 'string' then set col1 to VALUE, otherwize set to OTHERVALUE
df['col1'] = np.where(df1['col2'] = 'string', 'VALUE', 'OTHERVALUE')

# create a dictionary with key value pairs from dataframe values
# you can then use the map to update values in another dataframe whe id matches
value_map = dict(zip(df1['id'], df1['name']))
df2['name'] = df2['id'].map(value_map)


df1[df1['col1'].str.contains('test', na=False)]

