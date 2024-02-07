class Univariate():
    def quanQual(ds):
        quan=[]
        qual=[]
        for columnname in ds.columns:
                #print(columnname)
            if(ds[columnname].dtype=='O'):
                #print("qual")
                qual.append(columnname)
            else:
               # print("quan")
                quan.append(columnname)
        return quan,qual
        
    def freqTable(columnName,ds):
        freqTable=pd.DataFrame(columns=["Unique_Values","Frequency","Relative Frequency","CumSum"])
        freqTable["Unique_Values"]=ds[columnName].value_counts().index
        freqTable["Frequency"]=ds[columnName].value_counts().values
        freqTable["Relative Frequency"]=(freqTable["Frequency"]/103)
        freqTable["CumSum"]=freqTable["Relative Frequency"].cumsum()
        return freqTable
        
    def Univariate(ds,quan):
        descriptive=pd.DataFrame(index=["Mean","Median","Mode","Q1:25%","Q2:50%","Q3:75%","Q4:100%","IQR","1.5rule","Lesser","Greater","Min","Max"],columns=quan)
        for columnName in quan:
            descriptive[columnName]["Mean"]=ds[columnName].mean()
            descriptive[columnName]["Median"]=ds[columnName].median()
            descriptive[columnName]["Mode"]=ds[columnName].mode()[0]
            descriptive[columnName]["Q1:25%"]=ds.describe()[columnName]["25%"]
            descriptive[columnName]["Q2:50%"]=ds.describe()[columnName]["50%"]
            descriptive[columnName]["Q3:75%"]=ds.describe()[columnName]["75%"]
            descriptive[columnName]["Q4:100%"]=ds.describe()[columnName]["max"]
            descriptive[columnName]["IQR"]=descriptive[columnName]["Q3:75%"]-descriptive[columnName]["Q1:25%"]
            descriptive[columnName]["1.5rule"]=1.5*descriptive[columnName]["IQR"]
            descriptive[columnName]["Lesser"]=descriptive[columnName]["Q1:25%"]-descriptive[columnName]["1.5rule"]
            descriptive[columnName]["Greater"]=descriptive[columnName]["Q3:75%"]+descriptive[columnName]["1.5rule"]
            descriptive[columnName]["Min"]=ds[columnName].min()
            descriptive[columnName]["Max"]=ds[columnName].max()
        return descriptive
            