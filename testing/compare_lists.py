import numpy as np
import pandas as pd

def import_lists():
    try:
        listname1 = input("Please select Veteran file to read: ")
        list1 = pd.read_csv(listname1+".csv")
        listname2 = input("Please select second file to read: ")
        list2 = pd.read_csv(listname2+".csv")
    except:
        print("That doesn't seem to be a valid file. Pleae try again.")

    return list1, list2

def compare_names(df, df2):
    compared_names = pd.DataFrame(columns = ["Last Name", "First Name","First vets", "War", "Year Joined", "Year Left"])
    for i in df.index:
        lastname1 = df.loc[i,'Last Name'].title()
        firstname1 = str(df.loc[i,'First Name']).title()
        warserved = df.loc[i,'War']
        for x in df2.index:
            lastname2 = df2.loc[x,'Last Name'].title()
            firstname2 = df2.loc[x,'First Name'].title()
            yearjoined = df2.loc[x,'From']
            yearleft = df2.loc[x,'To']
            if lastname2 == lastname1:
                if firstname2[0] == firstname1[0]:
                    temp_series = pd.Series(data = [lastname2, firstname2, firstname1, warserved, yearjoined, yearleft], index = ['Last Name', 'First Name', 'First vets', 'War', 'Year Joined', 'Year Left'])
                    compared_names = compared_names.append(temp_series, ignore_index=True)
                    print("{} {} matches {} {}".format(firstname2, lastname2, firstname1[0], lastname1))

    return compared_names

def compare_dates(df):
    compared_dates = pd.DataFrame(columns = ["Last Name", "First Name","First vets", "War", "Year Joined", "Year Left"])
    wardates = {'War': ['WW1', 'WW2', 'Korea', 'Vietnam', 'Persian Gulf', 'OEF/OIF'],
             'Start Date': [1917, 1940, 1950, 1965, 1990, 2001], 'End Date': [1918, 1945, 1953, 1975, 1991, 2020]}
    war_dates = pd.DataFrame(wardates, columns = ['War', 'Start Date', 'End Date'])

    main_list = pd.DataFrame(df, columns = ['Last Name', 'First Name', 'First Name(vet)' 'War', 'Year Joined', 'Year Left'])
    print(main_list)

    for i in df.index:
        fullrow = df.loc[i]
        warserved = df.loc[i,'War']
        yearjoined = df.loc[i,'Year Joined']
        yearleft = df.loc[i,'Year Left']
        fullname = df.loc[i,'First Name'] + " " + df.loc[i,'Last Name']
        war = df.loc[i, 'War']
        warstart = war_dates.loc[war_dates['War'] == war , 'Start Date'].iloc[0]
        warend = war_dates.loc[war_dates['War'] == war , 'End Date'].iloc[0]
        start = df.loc[i, 'Year Joined']
        print("{} Joined in {}".format(fullname, start))
        if start <= warstart:
            if yearleft >= warend:
                print("{} was a member during {}".format(fullname, war))
                temp_series = pd.Series(fullrow)
                compared_dates = compared_dates.append(temp_series, ignore_index=True)
        elif start > warstart and start <= warend:
            if yearleft >= warend:
                print("{} was a member during {}".format(fullname, war))
                temp_series = pd.Series(fullrow)
                compared_dates = compared_dates.append(temp_series, ignore_index=True)
                print("{} may have been a member during {}".format(fullname, war))
                temp_series = pd.Series(fullrow)
                compared_dates = compared_dates.append(temp_series, ignore_index=True)
        else:
            print("{} was not a member during war".format(fullname))
    return compared_dates

def main():
    list1, list2 = import_lists()
    datelist = compare_names(list1, list2)
    final_list = pd.DataFrame(compare_dates(datelist))
    final_list.to_excel("final_list.xlsx")

if __name__ == "__main__":
    main()
