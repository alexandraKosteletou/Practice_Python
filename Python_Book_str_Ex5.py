# count the words of text
# text is part of washington post article 
# <https://www.washingtonpost.com/us-policy/2022/01/10/treasury-irs-filing-season/>


import re

#remove punctuation function
import re

def remove_punct(text):
    text = text.lower()
    text = re.sub(r'[.,!\d”“]', '', text)
    text = re.sub(r' +', ' ', text)            
    return text

data = '''Typically, IRS officials enter filing season with an unaddressed backlog of
 roughly 1 million returns. This year, however, the IRS will enter the filing season
 facing “several times” that, Treasury officials said, although they declined to give a
 more precise estimate. The IRS website says that as of Dec. 23, 2021, it still had
 6 million unprocessed individual returns, and as of the start of this month it still
 had more than 2 million unprocessed amended tax returns, a separate category.'''


data =remove_punct(data)
print(data)
data=data.split()

#print how many words are there in text after removing punctuation and digits
print(len(data))
