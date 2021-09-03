import pandas as pd

def generate_namelist(rowdata):
    namelist=pd.read_csv(rowdata, sep='\t')
    namelist=namelist.loc[:,["name"]]
    namelist=namelist.drop_duplicates(subset=['name'],keep='first')
    namelist.to_csv("namelist.txt", sep='\t',index=False, header=None)
    print("number of samples:")
    print(len(namelist))
def samplegenerator(rowdata,label):    
    train=pd.read_csv(rowdata, sep='\t')
    train=train.loc[:,["name","len","label"]]
    df=train[train['label']==label.strip()]

    with open("namelist.txt") as f:
        samplenames = f.readlines()
        for samplename in samplenames:
            onesample=df[df['name']==samplename.strip()]
            onesample.to_csv(samplename.strip()+"_"+label.strip()+".csv", sep=',',index=False)
            
generate_namelist("qwe.tsv")
samplegenerator("qwe.tsv","mother")
samplegenerator("qwe.tsv","child")