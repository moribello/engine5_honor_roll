import numpy as np
import pandas as pd

def remove_space(df, listname):
    for i in df.index:
        remove_space1 = df.loc[i,'Last Name']
        df.loc[i,'Last Name'] = remove_space1.lstrip()
        remove_space2 = str(df.loc[i,'First Name'])
        df.loc[i,'First Name'] = remove_space2.lstrip()

    df.to_csv(listname+"_corrected.csv", index=False)
    print("Spaces removed. Changes written to file {}_corrected.csv.".format(listname))

def import_list():
    while True:
        try:
            listname1 = input("Please select file to read: ")
            list1 = pd.read_csv("data/"+listname1+".csv")
            break
        except:
            print(listname1)
            print("That doesn't appear to be a valid file. Please try again.")

    return list1, listname1

def main():
        list1, listname1 = import_list()
        remove_space(list1, listname1)

if __name__ == "__main__":
    main()
