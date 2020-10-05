from collections import Counter
import pandas as pd
import os
from functools import reduce

icmldf = pd.read_csv(os.getcwd()+"/paper_data/icml2019.csv",encoding = "ISO-8859-1").apply(lambda x: x.astype(str).str.upper())
iclrdf = pd.read_csv(os.getcwd()+"/paper_data/iclr2020.csv").apply(lambda x: x.astype(str).str.upper())
nipsdf = pd.read_csv(os.getcwd()+"/paper_data/neurips2019.csv").apply(lambda x: x.astype(str).str.upper())
totaldf = pd.read_csv(os.getcwd()+"/paper_data/total.csv").apply(lambda x: x.astype(str).str.upper())

#cols_to_check=["Title","Authors"]
#icmldf[cols_to_check].replace({'(':''}, regex=True).replace({')':''}, regex=True)
#iclrdf[cols_to_check].replace({'(':''}, regex=True).replace({')':''}, regex=True)
#nipsdf[cols_to_check].replace({'(':''}, regex=True).replace({')':''}, regex=True)
#totaldf[cols_to_check].replace({'(':''}, regex=True).replace({')':''}, regex=True)

stop = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now", "UNIVERSITY", "UNIVERSITY)", "(UNIVERSITY" , "UNIVERSITY);"]

stop = [s.upper() for s in stop]

icmldf["Title_clean"]=icmldf["Title"].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop)]))
iclrdf["Title_clean"]=iclrdf["Title"].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop)]))
nipsdf["Title_clean"]=nipsdf["Title"].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop)]))
totaldf["Title_clean"]=totaldf["Title"].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop)]))

num = 50
icml_count = Counter(" ".join(icmldf["Title_clean"]).split()).most_common(num)
iclr_count = Counter(" ".join(iclrdf["Title_clean"]).split()).most_common(num)
neurips_count = Counter(" ".join(nipsdf["Title_clean"]).split()).most_common(num)
full_count= Counter(" ".join(totaldf["Title_clean"]).split()).most_common(num)
#print(icml_count)
#print(iclr_count)
#print(neurips_count)
print("----- TITLES -----")
print(' '.join([f[0] for f in full_count]))

icmldf["Authors_clean"]=icmldf["Authors"].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop)]))
iclrdf["Authors_clean"]=iclrdf["Authors"].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop)]))
nipsdf["Authors_clean"]=nipsdf["Authors"].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop)]))
totaldf["Authors_clean"]=totaldf["Authors"].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop)]))

num = 50
icml_count = Counter(" ".join(icmldf["Authors_clean"]).split()).most_common(num)
iclr_count = Counter(" ".join(iclrdf["Authors_clean"]).split()).most_common(num)
neurips_count = Counter(" ".join(nipsdf["Authors_clean"]).split()).most_common(num)
full_count= Counter(" ".join(totaldf["Authors_clean"]).split()).most_common(num)
#print(icml_count)
#print(iclr_count)
#print(neurips_count)

print('----- Authors -----')
print(' '.join([f[0] for f in full_count]))

