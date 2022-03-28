import os
import pysam
import pandas as pd

def readbam(name):
    bamdata = pysam.AlignmentFile(name, "rb")
    bamdataout = open(name + ".txt", "w")
    for read in bamdata:
        lenth = read.template_length - 25
        print(lenth, sep="\t", file=bamdataout)

def readtxt(txtname):
    with open(txtname.strip() + ".txt", "r") as f:
        lendata = f.readlines()
    lendata = pd.Series(lendata)
    lendata = pd.value_counts(lendata, sort=True)
    lendata = pd.DataFrame(lendata)
    lendata.columns = [txtname]
    lendata.to_excel(txtname + ".xlsx", encoding="utf-8")

def merge(excelnames):
    df = []
    for excelname in excelnames:
        sample = (pd.read_excel(excelname.strip() +".xlsx"))
        samplename = str.split(excelname,sep='.')[0]
        sample.columns = ['len', samplename.strip()]
        sample = sample.set_index("len")
        df.append(sample)
    dfs = pd.concat(df,axis=1,sort=True)
    dfs.to_excel('sam.xlsx')


val = os.system('ls *.bam > bamnames.txt')
print(val)
with open("bamnames.txt", "r") as g:
    bamnames = g.readlines()
    for bamname in bamnames:
        readbam(bamname.strip())
        readtxt(bamname.strip())
    merge(bamnames)
        
