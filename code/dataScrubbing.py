import pandas as pd
import json
import boto3

# Create a Data Frame 
dataframe = pd.read_csv("./1k.csv", sep='\t')

# Remove unnecessary columns (for details on what each column means: https://www.sec.gov/files/aqfs.pdf)
necessary_columns = ['edgar_accession_number', 'account_name', 'date', 'value']
unnecessary_columns = ['footnote', 'coreg', 'version', 'uom', 'qtrs']

for column in unnecessary_columns:
  del dataframe[column]

# Rename columns for clarity
dataframe.columns = necessary_columns

print(dataframe.shape)
dictionary_of_securities_and_accounts = {}
# list_of_financial_accounts = dataframe[0:50].values
list_of_financial_accounts = dataframe.values
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

print(dictionary_of_securities_and_accounts)

'''
Create list of new items which need to be searched, push into a queue and run the lambdas to scrape and update the dynamo table
For now, print to a .txt file
accession_number_dataframe = dataframe.copy(deep = True)[['edgar_accession_number']]
accession_numbers_dictionary = {}
for value_list in accession_number_dataframe.values.tolist():
  accession_numbers_dictionary[value_list[0]] = ''
jsonString = json.dumps(accession_numbers_dictionary)
jsonFile = open("data.json", "w")
jsonFile.write(jsonString)
jsonFile.close()
'''
# For Each, create an item and put in table
# for security in list_of_securities:
  # print(security.keys())
  # new_item = {
  #   'edgar_accession_number': 2,
  #   'financial_data': [
  #     {
  #       'year': 1,
  #       'account1': 10,
  #       'account2': 20
  #     },
  #     {
  #       'year': 2,
  #       'account1': 10,
  #       'account2': 20
  #     }
  #   ],
  #   'symbol': '1',
  #   'common_name': 'Capital One Financial',
  #   'legal_name': 'Capital One Financial, Inc.',
  #   'former_symbols': [],
  # }
# Pull in the existing accession #s from our dynamodb
dynamodb = boto3.resource('dynamodb')


# Update a Company Document in the DynamoDB Table you created.
# table = dynamodb.Table('securities')
# table.put_item(
#   Item={
#     'edgar_accession_number': 2,
#     'financial_data': [
#       {
#         'year': 1,
#         'account1': 10,
#         'account2': 20
#       },
#       {
#         'year': 2,
#         'account1': 10,
#         'account2': 20
#       }
#     ],
#     'symbol': '1',
#     'common_name': 'Capital One Financial',
#     'legal_name': 'Capital One Financial, Inc.',
#     'former_symbols': [],
#   }
# )
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
new_date_list = [
  {
    accession_number: number,
    new_data: {
      date: ddate,
      acc1: value,
      acc2:value
    }
  },
  {
    accession_number: number,
    new_data: {
      date: ddate,
      acc1: value,
      acc2:value
    }
  }
]
new_data_dictionary = {
  accession_number: {
    date: ddate,
    account1: value,
    account2: value
  },
  accession_number2: {}
}
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

security
  -> financial_data
    -> years
      -> financial_ratios (calc'd later)
      -> financial_accounts
        -> value / financial statement

get me the working capital ratio for appl in 2012
appl.financial_data.2012.financial_accounts
'''