from matplotlib.pyplot import clf
import pandas as pd
from sklearn.metrics import classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib

from sklearn.pipeline import Pipeline


# load data
data = {}
data["train"] = pd.read_csv("data/dataset_dev_intent.csv")
data["test"] = pd.read_csv("data/dataset_test_intent.csv")

# mdel
model = LogisticRegression(
    C=1,
    penalty='l2'
)
# encoder
encoder = TfidfVectorizer(
    ngram_range=[1, 1], lowercase=False, norm=None)

pipe = Pipeline([('encoder', encoder), ('logistic', model)])

# training
x = data["train"]["sentence"]
y = data["train"]["label_intent"]

pipe.fit(x, y.astype('int'))

# test
x = data["test"]['sentence']
y_pred = pipe.predict(x)
y_true = data["test"]["label_intent"]

clf_report = classification_report(y_pred, y_true,
                                   output_dict=True)

print(clf_report)

joblib.dump(pipe, 'model_intent.joblib')
