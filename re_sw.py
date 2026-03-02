#nltk.download('stopwords')

from nltk.corpus import stopwords
import pandas

data = pandas.read_csv("words.csv")

stop_words = set(stopwords.words("german"))
data_clean = data[~data["word_single"].isin(stop_words)]
data_clean.to_csv("word_datasets/words_clean.csv", index=False)



