import pandas as pd
import string
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer


def preprocess(input):
    data = pd.read_csv(input)

    # Drop NaN values from 'text' column
    data['text'] = data['text'].dropna()

    # Create stopwords set
    stopwords_set = set(stopwords.words('english'))

    # Initialize stemmer
    stemmer = PorterStemmer()

    # Process text
    corpus = []
    for text in data['text'].str.lower():
        text = text.translate(str.maketrans('', '', string.punctuation)).split()
        text = [stemmer.stem(word) for word in text if word not in stopwords_set]
        text = ' '.join(text)
        corpus.append(text)

    # Split data
    x_train, x_test, y_train, y_test = train_test_split(corpus, data['label_num'], test_size=0.5, random_state=3)

    # Initialize and fit TfidfVectorizer
    feature_extraction = TfidfVectorizer(min_df=1, stop_words='english', lowercase=True)
    x_train_features = feature_extraction.fit_transform(x_train)
    x_test_features = feature_extraction.transform(x_test)

    # Convert labels to integers if needed
    if not isinstance(y_train.iloc[0], int):
        y_train = y_train.astype(int)
        y_test = y_test.astype(int)

    return x_train_features, x_test_features, y_train, y_test, feature_extraction
