import pandas as pd
df = pd.read_csv('interface.csv')

for raw,column in df.iterrows():
    with open("output.txt",'a') as f1:
        f1.write(f"interface {column[0]}\n")
        f1.write(f"description {column[1]}\n")
        f1.write(f"switch-port mode access\n")
        f1.write(f"switch-port access vlan {column[2]}\n\n")



