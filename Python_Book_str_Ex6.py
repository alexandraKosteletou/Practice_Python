#the script takes a word as input 
#we give a sample text
#point out the words in the sample text in which we can find the input word


input_word= input('Type a word:')
text_sample = '''The IRS website says that as of Dec. 23, 2021, it still had
 6 million unprocessed individual returns, and as of the start of this month it still
 had more than 2 million unprocessed amended tax returns, a separate category.'''

def find_word(word, text):
    i=0
    for w in text.split():
        if word in w:
            i+=1
            print(i, ':', w)

find_word(input_word,text_sample)

