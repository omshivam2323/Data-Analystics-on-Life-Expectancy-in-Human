import pandas as pd

class Analyse:

    def __init__(self, path = 'datasets/apps.csv'):
        self.df = pd.read_csv(path)
        self.cleanData()

    def cleanData(self):
        self.df.drop(columns=[self.df.columns[0]], inplace=True)

    def getDataframe(self):
        return self.df

    def getCategories(self):
        return self.df.groupby('Category').count().sort_values('App')['App'][::-1]

    