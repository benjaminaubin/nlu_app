import pandas as pd
from sklearn_crfsuite import CRF
from sklearn_crfsuite.metrics import flat_classification_report
from sklearn.base import RegressorMixin
import joblib

from sklearn.pipeline import Pipeline


class Manual_Features(object):
    def __init__(self, n=1):
        self.n = n

    def transform(self, df):
        sentences = [s for s in df.groupby(
            'slot').apply(self.aggregate_words)]
        x = [self.sentence_to_features(s) for s in sentences]
        y = [self.sentence_to_labels(s) for s in sentences]
        return x, y, df["slot"].iloc[-1]

    def aggregate_words(self, s):
        return [word_tag for word_tag in zip(
            s['word'].values.tolist(),
            s['tag'].values.tolist(),
            s['slot'].values.tolist(),
            s['sentence'].values.tolist(),
        )]

    def sentence_to_features(self, sequence):
        return [self.word_to_features(sequence, i) for i in range(len(sequence))]

    def sentence_to_labels(self, sequence):
        return [tag for word, tag, slot, sentence in sequence]

    def word_to_features(self, sequence, i):
        word = sequence[i][0]
        slot = sequence[i][2]
        sentence = sequence[i][3]
        words = sentence.split()
        length = len(words)

        # get position of the word
        try:
            pos = words.index(word)
        except:
            pos = 0

        features = {
            'word.lower()': word.lower(),  # lower
            'word[-3:]': word[-3:],  # suffix
            'word[-2:]': word[-2:],  # suffix
            'word.isupper()': word.isupper(),  # upper
            'word.isdigit()': word.isdigit(),
            'position': pos
        }

        ## closest neighbour ##
        for neighbour in range(1, self.n + 1):
            if pos > neighbour - 1:
                word_left = words[pos - neighbour]
                features.update({
                    f'-{neighbour}:word.lower()': word_left.lower(),
                    f'-{neighbour}:word.isupper()': word_left.isupper(),
                    f'-{neighbour}:word.isdigit()': word_left.isdigit(),
                    f'-{neighbour}:pos': pos - neighbour,
                })
            else:
                features[f'-{neighbour}:word.lower()'] = 'BOS'
            if pos < length - neighbour:
                word_right = words[pos + neighbour]
                features.update({
                    f'+{neighbour}:word.lower()': word_right.lower(),
                    f'+{neighbour}:word.isupper()': word_right.isupper(),
                    f'+{neighbour}:word.isdigit()': word_right.isdigit(),
                    f'+{neighbour}:pos': pos + neighbour,
                })
            else:
                features[f'+{neighbour}:word.lower()'] = 'EOS'

        return features


class CustomCRF(RegressorMixin):
    def __init__(self, model, encoder, max_iterations=100):
        self.model = model
        self.encoder = encoder
        self.model.max_iterations = max_iterations

    def fit(self, X=None, y=None):
        x, y, _ = self.encoder.transform(X)
        self.model.fit(x, y)

    def process_for_prediction(self, sentence):
        df = pd.DataFrame(columns=['sentence', 'slot', 'word', 'tag'])
        list_words = []
        for word in sentence.split():
            list_words.append(word)
            sentence = ' '.join(list_words)
            dic = dict(sentence=sentence, slot=sentence, word=word, tag="O")
            df = df.append(dic, ignore_index=True)
        return df

    def predict(self, X=None):
        X = self.process_for_prediction(X)
        x, y, sentences = self.encoder.transform(X)

        y_pred = self.model.predict(x)
        return y_pred, y


if __name__ == "__main__":
    # load data
    data = {}
    data["train"] = pd.read_csv("data/dataset_dev_tags.csv")
    data["test"] = pd.read_csv("data/dataset_test_tags.csv")

    # model
    model = CRF(
        algorithm='lbfgs',
        c1=0.1,
        c2=0.1,
        all_possible_transitions=True
    )
    encoder = Manual_Features()

    customModel = CustomCRF(model=model, encoder=encoder)

    # training
    customModel.fit(data["train"])

    # test
    # y_pred, y_true = customModel.predict(data["test"])
    # clf_report = flat_classification_report(y_true, y_pred,
    #                                         output_dict=True)

    # print(clf_report)

    joblib.dump(customModel, 'model_tag.joblib')
