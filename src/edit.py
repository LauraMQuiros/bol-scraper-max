from datetime import datetime
import pandas as pd

date = datetime.today().strftime('%d%m-%y')

def clear_garbage(search_name: str) -> str:
        
    df = pd.read_csv('data/scraped_product.csv')

    df.drop_duplicates(subset=['title'], keep='first', inplace=True)

    # If rated lower that 7 delete row
    #df['rated'] = df['rated'].fillna(0)
    #df.drop(df[df.rated < 5].index, inplace=True)
    #df['rated'] = pd.to_numeric(df['rated'], downcast="integer")

    #if rating lower 3.5 drop row
    #df['rating'] = df['rating'].fillna(0)
    #df.drop(df[df.rated < 3.2].index, inplace=True)

    # Del - in scraped price
    df['price'] = df['price'].str.replace('-','')

    budget = input('Enter your budget: ')
    budget = float(budget)
    # make sure to make the price column a float
    df['price'] = df['price'].str.replace('€', '').str.replace(',', '.').astype(float)
    # drop all rows with a price higher than the budget
    df.drop(df[df.price > budget].index, inplace=True)

    # Add the grams column
    df = get_grams(df)

    # Save file, no index
    df.to_csv(f'data/{search_name}-{date}.csv', index=False,)
    return f'{search_name}-{date}'


def extract_brackets (item: str) -> list:
    # when we find an item with parenthesis in it, we take the string out
    # some items (other words) -> ['some items', 'other words']
    return [item.replace(')', '') for item in item.split("(")]

def get_grams(df: pd.DataFrame) -> pd.DataFrame:

    # separate title into a list of all things split by -
    df['title'] = df['title'].str.split('-')
    
    for row in range(len(df['title'])):
        # if any row has a list with a str with a parenthesis in it
        # we extract the brackets and append to the list
        for item in df.iloc[row]['title']:
            if '(' in item:
                # remove item from df['title'][row]
                df.iloc[row]['title'].remove(item)
                # append the extracted brackets
                df.iloc[row]['title'].extend(extract_brackets(item))

    # create a new column called grams, where we store the string in the title list that contains a number followed by 'g' or 'G'
    df['grams'] = df['title'].apply(lambda x: [item for item in x if any(char.isdigit() for char in item) and ('g' in item or 'G' in item)])

    # if the grams column is empty, we fill it with '0g'
    df['grams'] = df['grams'].apply(lambda x: x if x else ['0g'])

    return df