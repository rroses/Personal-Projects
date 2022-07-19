import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer

url_data = pd.read_csv("malicious_phish.csv")

url_data.head()

def makeTokens(f):
    tkns_BySlash = str(f.encode('utf-8')).split('/')
    total_Tokens = []

    for i in tkns_BySlash:
        tokens = str(i).split('-')
        tkns_ByDot = []

    for j in range(0, len(tokens)):
        temp_Tokens = str(tokens[j]).split('.')
        tkns_ByDot = tkns_ByDot + temp_Tokens
        total_Tokens = total_Tokens + tokens + tkns_ByDot
        total_Tokens = list(set(total_Tokens))

    return total_Tokens

url_list = url_data['url']
y = url_data['type']

vectorizer = TfidfVectorizer(tokenizer=makeTokens)

X = vectorizer.fit_transform(url_list)

X_train, X_test, y_train, y_test = train_test_split(X, y)

logit = LogisticRegression()

logit.fit(X_train, y_train)

print("Accuracy ", "{:.3%}".format(logit.score(X_test, y_test)))



