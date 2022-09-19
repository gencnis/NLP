# from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from lib2to3.pgen2.tokenize import tokenize
import nltk
import os

# This function counts the words and returns the counted words dictionary
def word_count(words):
    counts = dict()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

# This function sorts the words and returns the sorted dictionary
def sort_dict_by_value(words, reverse = False):
      return dict(sorted(words.items(), key = lambda x: x[1], reverse = reverse))

'''
This is the cool word cloud I wanted to do, but could not debug. SO here for the future work.

def word_cloud(words):
    # Create the wordcloud object
    wordcloud = WordCloud(width=480, height=480, margin=0).generate(words)

    # Display the generated image:
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.margins(x=0, y=0)
    plt.show()
'''

def main():
    # gets the input
    file_name = input("Enter the path of your file: ")
    
    # checks if the file path exists
    assert os.path.exists(file_name), "I did not find the file at, "+str(file_name)
    
    # opens the file
    with open(file_name,'r+') as f:
        lines = f.read() # reads
        lines = lines.lower() # lowers all the capitalized letters

        # initializing punctuations string
        punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        
        # Removing punctuations in string
        # Using loop + punctuation string
        for ele in lines:
            if ele in punc:
                lines = lines.replace(ele, "")

        tokenized = nltk.word_tokenize(lines) # tokenizes the words
        wordcount_dic = word_count(tokenized) # creates a dictionary to keep the word count
        sorted_words = sort_dict_by_value(wordcount_dic, True) # sorts the words
            
        N = 20 # initializes limit for the first 20 words

        # gets first 20 items in our dictionary 
        top_twenty = dict(list(sorted_words.items())[0: N]) 

        print("This is the sorted top twenty words for the entered file:\n ",top_twenty)

        # creates two different lists to hold the keys and the values of the top 20 words      
        words = list(top_twenty.keys())
        values = list(top_twenty.values())
    
        y_pos = np.arange(len(top_twenty))
        
        # creates horizontal bars
        plt.barh(y_pos, values)
        
        # creates names on the x-axis
        plt.yticks(y_pos, words)
        
        # show graphic
        plt.show()

        # attempt for a cool word cloud, had errors
        # word_cloud(words)
        

if __name__ == "__main__":
    main()
