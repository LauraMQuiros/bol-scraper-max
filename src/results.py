import pandas as pd

def give_results(search_name: str): 
    df = pd.read_csv(f'data/{search_name}.csv')
    
    # sort by price
    df.sort_values(by='price', inplace=True)

give_results('noodles-0103-21')