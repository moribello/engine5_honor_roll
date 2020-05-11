Honor Roll Compilation Tools
===================================
This suite of tools was originally developed to assist in comparing lists of veterans who served from a particular town with a list of members in a particular engine company. Depending on your list you may or may not need every tool in the suite. The suite includes the following python scripts:
    split_names.py
    remove_spaces.py
    searchby_name.py
    compare_lists.py

Pre-requisites
--------------
- Python 3
- Numbpy
- Pandas

Usage and description for individual packages:
----------------------------------------------

split_names.py

Purpose: To split a list of full names into a .csv file with "Last Name" and "First Name" columns.

Usage: run "split_names.py <filename>" where <filename> is the file you wish to split names from

Description: This script takes a .csv list with a single column called "Full Name" and splits it into two columns: "Last Name" and "Full Name". It then removes the "Full Name" column and finally writes the new split list into a new .csv list with "split" appended to the filename.

remove_spaces.py

Purpose: To remove extraneous leading white spaces in "First Name" and "Last Name" columns.

Usage: run "remove_spaces.py <filename>" where <filename> is the name of the file you wish to remove white spaces from

Description: When comparing names an extraneous space in front of either the first or last name can cause a false negative; this script uses python's lsplit() function to remove any leading white spaces and then write the new value into a new .csv list with "corrected" appended to the filename

searchby_name.py

Purpose: To search a file by last names

Usage: run "searchby_name.py". The script will prompt for a file to read from and then a last name to search by.

Description: This script allows a user to search for a particular last name in either a list of members or a list of veterans. If matching last names are found they'll be returned; if not, nothing will be returned.

compare_lists.py

Purpose: To compare two lists, one of veterans and the war they served in, and a second list of members' names and years they were active within the company.

Usage: run "compare_lists.py". The script will prompt for the files to read and export a new excel file called "final_list.xlsx"

Description: This script compares two lists - a "Veterans" list and a "Members" list. Note that this script requires specific formatting of each list:
    The "Veterans" list must contain the following columns:
        "Last Name"
        "First Name"
        "War" (war the veteran fought in; possible values are "WW1", "WW2", "Korea", "Vietnam", "Persian Gulf", or "OEF/OIF")
    The "Members" list must contain the following columns:
        "Last Name"
        "First Name"
        "From" (year the member joined the company)
        "To" (year the member left the company; if still a member use the current year)
    The scripts above should assist in preparing your two comparison lists.

    Once run, the script will iterate through both lists and check for matching last names. If it finds a matching last name it will examine the first letters of the first name; this is done to avoid false negatives for variations in names (i.e., "Edward" vs. "Ed"). For final comparison both the "First Name" value from the "Members" list and the "First Name" value from the "Veterans" list (column name: "First (vets)") is included in the final list.

    If a match is found the script will then look at the war this individual served in and compare it to the "From" and "To" dates for the matching member. If the individual was a member during the years their "War" value indicates the individual is added to the final list. Once complete, the script will create an excel file called "final_list.xlsx" containing the list of members and the war they served in. The "First (vets)" column can be used to confirm the correct individual was selected from both lists.
