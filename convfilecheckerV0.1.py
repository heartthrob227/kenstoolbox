import csv, re, pandas
from collections import defualtdict
print('=================================')
print('Welcome to the Conversion File Checker')

#Ask for file to parse
rawfile = input('What file do you want to test (without extension; must be csv)? ')
firstfile = rawfile + '.csv'
#Open file
fout=open(outputname,"w+", newline='')

def dateformat():
    datecolumn = input('What is the name of the date column? ')
    #Draw value for one key from one row
    dateformat = #drawn value from key
def idcheckandcount():
    # Determine profile/affcode or KClickID
    idtype = input('Is this a Click ID (C) or Profile|Affcode (P) based file (case sensitive)? ')
    if idtype == 'C':
        #insert regex Check
        #valid rows
        validrows = #count of rows that meet criteria
        #not valid rows (return an error file with row that had error)
        invalidrows = #count of rows that do not meet criteria
    elif idtype == 'P':
        #insert regex Check
        #valid rows
        #not valid rows (return an error file with row that had error)
    else:
        print ('Not a valid Type')

def singleormulti():
# Determine if single column for conv type or multiple columns
    singleormulti = input('Is this file based on single (S) or multiple (M) columns for conversions (case sensitive)? ')
    if singleormulti == 'S'
    # If single run this
    ## of conversions by Type
    # $ by Type
    elif singleormulti == 'M'
    #if multiple run this
    ## of conversions by Type
    # $ by Type
    else:
        print ('That is not a valid response')

dateformat()
idcheckandcount()
singleormulti()

def createreport():
    print ('======================================')
    print ('Date format is ' + dateformat)
    print ('The number of valid rows is ' + validrows)
    print ('The number of valid rows is ' + invalidrows)
    print ('') #figure out a way to get the consolidated list of conv types and their aggregation
    print ('') #same as above but with Rev
