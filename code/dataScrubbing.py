import pandas as pd
from time import sleep
import boto3
from datetime import datetime
startTime = datetime.now()
# Create a Data Frame 
# dataframe = pd.read_csv("./1k.csv", sep='\t')
dataframe = pd.read_csv("./full_num.txt", sep='\t')

# Remove unnecessary columns (for details on what each column means: https://www.sec.gov/files/aqfs.pdf)
necessary_columns = ['edgar_accession_number', 'account_name', 'date', 'value']
unnecessary_columns = ['footnote', 'coreg', 'version', 'uom', 'qtrs']

for column in unnecessary_columns:
  del dataframe[column]

# Rename columns for clarity
dataframe.columns = necessary_columns

# print(dataframe.shape)

dictionary_of_securities_and_accounts = {}
# list_of_financial_accounts = dataframe[0:50].values
list_of_financial_accounts = dataframe.values
print(len(dataframe)) # 3m line items.
for account_details in list_of_financial_accounts:
  accession_number = account_details[0]
  account_name = account_details[1]
  date = account_details[2]
  value = account_details[3]
  
  new_item = {
    'account_name': account_name,
    'date': date,
    'value': value
  }

  # check if the company exists
  if accession_number in dictionary_of_securities_and_accounts:
    dictionary_of_securities_and_accounts[accession_number].append(new_item)
  else:
    dictionary_of_securities_and_accounts[accession_number] = [new_item]

# print(dictionary_of_securities_and_accounts)
documents = []
for security in dictionary_of_securities_and_accounts.items():
  # print('security: ', security)
  new_doc = {}
  new_doc['edgar_accession_number'] = security[0]
  new_doc['stock_symbol'] = 'COF'
  new_doc['former_symbols'] = []
  new_doc['financial_data'] = {}

  for account in security[1]:
    # print('acc: ', account)
    account_date = str(account['date'])
    account_name = str(account['account_name'])
    value = str(account['value'])

    if account_date in new_doc['financial_data']:
      if account_name in new_doc['financial_data'][account_date]:
        # Todo: question for SEC. Should there be duplicates?
        # print("new_doc['financial_data'] ", new_doc['financial_data'])
        # print('duplicate account in the same year?: ', account)
        dupe = account_name + 'dupe'
        new_doc['financial_data'][account_date][dupe] = []
        new_doc['financial_data'][account_date][dupe].append(value)
      else:
        new_doc['financial_data'][account_date][account_name] = value
    else:
      new_doc['financial_data'][account_date] = { account_name: value }
  documents.append(new_doc)

formatting_data = datetime.now() - startTime
print('formatting data: ', formatting_data)

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('securities')
# Update table to have 20 RW capoacity within 25 free tier
# client = boto3.client('dynamodb')
# client.update_table(
#   TableName='securities',
#   ProvisionedThroughput={
#     'ReadCapacityUnits': 20,
#     'WriteCapacityUnits': 20
#   }
# )
print(len(documents))
try:
  num = 0
  with table.batch_writer() as batch:
    for item in documents:
      sleep(1) # Todo: This is obviously, not cool.
      print(num)
      num += 1
      batch.put_item(Item=item)
except Exception as e:
  print('error: ', e)
dynamo_time = datetime.now() - formatting_data
print('dynamo: ', dynamo_time)



# Create the DynamoDB table. Todo: This should be put into a config/setup directory
# dynamodb.create_table(
#   TableName='securities',
#   KeySchema=[
#     {
#       'AttributeName': 'edgar_accession_number',
#       'KeyType': 'HASH'
#     }
#   ],
#   AttributeDefinitions=[
#     {
#       'AttributeName': 'edgar_accession_number',
#       'AttributeType': 'N'
#     },
#   ],
#   ProvisionedThroughput={
#     'ReadCapacityUnits': 25,
#     'WriteCapacityUnits': 25
#   }
# )

# table = dynamodb.Table('security')
# print(table)
# Wait until the table exists.


# Execute the puppeteer code
# Create reference of accession numbers with company names


# Cross reference new adsh ids with new companies
# dataframe1.to_csv('14k.csv', index = None)


'''
Situation: I want to start this from scratch
1. Create a dynamoDB table for all securities
Each security will have at least the following:
  edgar_accession_number: int
  financial_data: [
    {
      year: 1
      account1: 10,
      account2: 20
    },
    {
      year: 2
      account1: 10,
      account2: 20
    },
  ],
  current_cik: string,
  former_ciks: [string, string, string],


Situation: I have new data to update
2. Iterate over the .txt data and for each item, add the account data to the new_data_dictionary
3. Once done, iterate over each item in the dictionary, find the document in dynamodb with a matching accession_number


- Go through the listing of Accession numbers and get a list of unique ids
- For each unique id, check if a document exists in dynamodb
  - if so: 
    - add the new data 
  - else: 
    pipe it into a file which anthoiny needs to manually revisit.
    create a new document object with the first year's data

Tables:
DynamoDB | 'securities' | each item has all historical data broken down by account for each accession_number to cross reference to SEC data
PostgreSQL | 'securities' | each row is precalculated financial ratios for each company

'''



'''

{
  id: 1234,
  financial_data: {
    2011: {
      cash: 123,
      liability: 123
    }
  }
}

security
  -> financial_data
    -> years
      -> financial_ratios (calc'd later)
      -> financial_accounts
        -> value / financial statement

get me the working capital ratio for appl in 2012
appl.financial_data.2012.financial_accounts
'''