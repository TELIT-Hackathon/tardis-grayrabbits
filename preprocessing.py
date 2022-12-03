# Imports
import pandas as pd
from sklearn import preprocessing as prep


# Preprocessor component
class Preprocessor(object):
    def __init__(self, dataset):
        self.dataframe = dataset

    # Removes data that should not affect the results of learning
    # To keep: [everything but instance, platform, route, maybe app]
    def remove_columns(self, col_names):
        for name in col_names:
            self.dataframe.drop(name, axis=1)

    # Scales data so the values are close to each other (0.0 - 1.0).
    # Data is otherwise too far apart - do not affect learning equally
    def scale(self):
        scaler = prep.MaxAbsScaler()
        scaler.fit(self.dataframe)
        transformed = scaler.transform(self.dataframe)
        return transformed
