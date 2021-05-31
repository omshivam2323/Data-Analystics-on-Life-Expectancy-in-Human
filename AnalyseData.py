import pandas as pd


class Analyse:

    def __init__(self, path):
        self.df = pd.read_csv(path)
        # self.cleanData()

    def cleanData(self):
        self.df.drop(columns=[self.df.columns[0]], inplace=True)

    def getDataframe(self):
        return self.df

    def getRegionLifeExpectancyData(self):
        return self.df.groupby('Location')['First Tooltip'].mean().sort_values()

    def getHealthvsLife(self):
        life = self.df.groupby(['Location'])['Life expectany'].mean()
        health = self.df.groupby(['Location'])['Hale Expectency'].mean()
        return (life, health)

    def getGender(self):
        return self.df.groupby('Dim1')['First Tooltip'].mean()

    def getGender(self):
          return self.df.groupby('Dim1')['First Tooltip'].mean()

    def getData(Africa):
          return Africa.df.groupby('Dim1')['First Tooltip'].mean()   

    def getData(Americas):
          return Americas.df.groupby('Dim1')['First Tooltip'].mean() 

    def getData(Europe):
          return Europe.df.groupby('Dim1')['First Tooltip'].mean()  

    def getData(Eastern):
          return Eastern .df.groupby('Dim1')['First Tooltip'].mean()    

    def getData(Asia):
          return Asia .df.groupby('Dim1')['First Tooltip'].mean()                        
              

      
        
        
       
    
