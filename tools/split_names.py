# Python script to split full names into "Last Name", "First Name" format
#Note: this script will take a .csv file from the argument and create a new one with "_split" appended to the filename. The original file should have a single column labled "Full Name"
import pandas as pd
import sys

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

def split_fullnames(df, listname):
    # new data frame with split value columns
    new = df["Full Name"].str.split(" ", n = 1, expand = True)
    # making separate first and last name columns from new data frame
    df["First Name"]= new[1]
    df["Last Name"]= new[0]
    df = df.drop(columns=['Full Name'])

    new_filename = listname[:-4]
    df.to_csv(new_filename+"_split.csv", index=False)
    print("Spaces removed. Changes written to file {}_split.csv.".format(new_filename))


def main():
        list1, listname1 = import_list()
        split_fullnames(list1, listname1)

if __name__ == "__main__":
    main()
