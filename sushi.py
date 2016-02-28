import pdb
import pandas as pd
import sys

#The order NYNAB exports in
columns = ["Account","Date","Payee","Category","Memo","Outflow","Inflow","Cleared"]
#The order we need for YNAB4
reindex_columns = ["Account","Date","Payee","Category","Memo","Inflow","Outflow","Cleared"]
#The subset that YNAB4 wants
output_columns = ["Date", "Payee", "Category", "Memo", "Inflow", "Outflow"]

data = pd.read_csv(sys.argv[1], 
                   names=columns, 
                   skiprows = 1,
                   na_values=['$0.00'])

#Get rid of the dollar signs and convert to float
for col in ('Outflow', 'Inflow'):
    data[col] = data[col].str[1:].astype(float)

#For each of your accounts
for account_name in data['Account'].unique():
    account = data[data['Account'] == account_name]
    account.reindex(reindex_columns)

    #You will have one csv for each account
    with open('~/Desktop' + each + '_ynab.csv', 'w') as sliced:
        account.to_csv(path_or_buf=sliced, index=False, columns=output_columns)
