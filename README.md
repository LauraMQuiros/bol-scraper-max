
Instead of giving me the promised monetary compensation, I have been given a bol.com voucher. 
I want to make the best use of my money, so I will be buying as many items as possible. 
Since I am university student, obviously I am talking about instant noodle packages.

I modified [this scraper](https://github.com/xgino/bol-product-scraper).
Following additions
- Took out rating limitations
- Introduced price limitations
- Extracted grams and units from the title

To run the program:
```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python src/main.py
```
and then introduce your search term. It might take a bit for the program to go through the files, 
but you should see the progress being printed. 