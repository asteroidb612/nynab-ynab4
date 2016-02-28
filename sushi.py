import pdb
import pandas as pd
import sys

columns = ["Account","Date","Payee","Category","Memo","Outflow","Inflow","Cleared"]
reindex_columns = ["Account","Date","Payee","Category","Memo","Inflow","Outflow","Cleared"]
output_columns = ["Date", "Payee", "Category", "Memo", "Inflow", "Outflow"]

data = pd.read_csv("My Budget as of 2016-02-26 0928 PM - Register.csv", 
                            names=columns, 
                            skiprows = 1,
                            na_values=['$0.00'])

for col in ('Outflow', 'Inflow'):
    data[col] = data[col].str[1:].astype(float)

#Whatever your accounts were
accounts = ['Cash', 'Credit Card', 'Checking Account', 'Venmo']

for each in accounts:
    account = data[data['Account'] == each]
    account.reindex(reindex_columns)

    #You will have one csv for each account
    with open('./' + each + 'sliced.csv', 'w') as sliced:
        account.to_csv(path_or_buf=sliced, index=False, columns=output_columns)
