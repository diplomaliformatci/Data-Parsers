import sys
import string
import json
from collections import Counter
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords
import matplotlib as plt

def process(text, tokenizer=TweetTokenizer(), stopwords=[]):

    text = text.lower()
    tokens = tokenizer.tokenize(text)
   
    # tokens = normalize_contractions(tokens)
    return [tok for tok in tokens if tok not in stopwords and not tok.isdigit()]

def normalize_contractions(tokens):
  
    token_map = {
        "i'm": "i am",
        "you're": "you are",
        "it's": "it is",
        "we're": "we are",
        "we'll": "we will",
    }
    for tok in tokens:
        if tok in token_map.keys():
            for item in token_map[tok].split():
                yield item
        else:
            yield tok

if __name__ == '__main__':
    tweet_tokenizer = TweetTokenizer()
    punct = list(string.punctuation)
    stopword_list = stopwords.words('english') + punct + ['rt', 'via']

    fname = sys.argv[1]
    tf = Counter()
    with open(fname, 'r') as f:
        for line in f:
            tweet = json.loads(line)
            tokens = process(text=tweet.get('text', ''),
                             tokenizer=tweet_tokenizer,
                             stopwords=stopword_list)
            tf.update(tokens)
        for tag, count in tf.most_common(50):
            print("{}: {}".format(tag, count))

        y = [count for tag , count in tf.most_common(30)]
        x = range(1,len(y)+1)

        plt.bar(x,y)
        plt.title("Term Frequencies")
        plt.ylabel("Frequency")
        plt.savefig('term_distribution.png')
