import pandas as pd

#to print
print(pd.__version__)

dist = {
    'head' : {
        'name':'Paban Bhandari',
        'adress':'Changathali',
        'number':9848436507
    },
    'staff1':{
        'name':'Prakash Yari',
        'adress':'Ratnapark',
        'number':9800000000
    }
}
#to convert dictionary to data frame we can use pd.dataFrame
df = pd.DataFrame(dist)
print(df)
print(df.head())
print(df.index)