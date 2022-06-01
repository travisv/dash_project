import pandas as pd
from pathlib import Path

financial_data_file_path = input('Enter path to financial data file: ')
#Path('/home/travis/Downloads/us_financials_jgnh7gj')
print(f'Getting data from {financial_data_file_path}')

def get_data(data_file_path):
    company_dict = {}
    for file in data_file_path.glob('*tickers.xlsx'):
        my_dict = pd.read_excel(file, header=2, index_col='Report Date',
                            sheet_name=None)
        company_dict.update(my_dict)
    df = pd.concat([df.T for df in company_dict.values()],
                   keys=[ticker for ticker in company_dict.keys()])
    return df

data = get_data(financial_data_file_path)
data.reset_index().to_csv('financial_data_script_file.csv')
print(data.head())



