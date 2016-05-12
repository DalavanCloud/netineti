import nltk
from collections import *

def length_distribution(positive_example_filename):
    lines = open(positive_example_filename).readlines()
    
    count_dis = defaultdict(int) #distribution of the word count of the names
    for line in lines:
        tokens = line.split('---')
        if len(tokens) > 0:
            name = tokens[0].encode('utf-8')
        word_count = len(nltk.word_tokenize(name))
        
        count_dis[word_count] = count_dis[word_count] + 1
    
    max_length = max(count_dis.keys())
    
    for i in range(1, max_length+1):
        print i, '\t',
    print
    
    for i in range(1, max_length+1):
        print count_dis[i], '\t',
    print
    

if __name__ == '__main__':
    length_distribution('data/names_in_context.txt')
    
    length_distribution('data/test_result_before_refactoring.txt')