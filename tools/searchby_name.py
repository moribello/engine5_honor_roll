import pandas as pd

def import_lists():
    try:
        listname1 = input("Please select file to read: ")
        list1 = pd.read_csv(listname1+".csv")
    except:
        print("That doesn't seem to be a valid file. Pleae try again.")

    return list1

#full_list['Full Name'] = full_list['First Name'].str.title() + " " +full_list['Last Name'].str.title()

def search_for_name(full_list):
    search_name = input("What last name would you like to search by? ").upper()
    print(full_list.loc[full_list['Last Name'] == search_name])

def main():
    full_list = import_lists()
    search_for_name(full_list)

if __name__ == "__main__":
    main()
