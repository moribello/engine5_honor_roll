import numpy as np
import pandas as pd
import sys

def remove_space(df, listname):
    for i in df.index:
        remove_space1 = df.loc[i,'Last Name']
        df.loc[i,'Last Name'] = remove_space1.lstrip()
        remove_space2 = str(df.loc[i,'First Name'])
        df.loc[i,'First Name'] = remove_space2.lstrip()

    new_filename = listname[:-4]
    df.to_csv(new_filename+"_corrected.csv", index=False)
    print("Spaces removed. Changes written to file {}_corrected.csv.".format(new_filename))

def import_list():
    while True:
        try:
            listname1 = sys.argv[1]
            list1 = pd.read_csv(listname1)
            break
        except:
            print(listname1)
            print("That doesn't appear to be a valid file. Please try again.")
            break

    return list1, listname1

def main():
        list1, listname1 = import_list()
        remove_space(list1, listname1)

if __name__ == "__main__":
    main()
