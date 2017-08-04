#Pattifilebreaker V1.0
#last Update 8/4/17

import csv
from collections import defaultdict


filename = input('What file will we be looking at (CSV format required; no extension)? ')
filenamewithtext = filename + '.csv'
fout = open(filename + '_filtered.csv', 'a+', newline = '')

with open(filenamewithtext) as file:
    # REMEMBER: DELIMITERS NEED TO BE SET PER FILE
    dictfile = csv.DictReader(file, delimiter=',')
    header = dictfile.fieldnames
    print (header)
    writer = csv.DictWriter(fout, fieldnames = header)
    writer.writeheader()
    column = input('What column are we filtering? ')
    filtervalue = input('What is the filtering criteria (comma separated)? ')
    filterlist = filtervalue.split(',')
    print(filterlist, type(filterlist))
    check = input('')
    for value in filterlist:
        print (value)
        rowcount = 1
        passcount = 0
        matchcount = 0
        for row in dictfile:
            #print (row)
            print('Processing Row #' + str(rowcount))
            for (k,y) in row.items():
                if k == column:
                    if y == value:
                        print (value)
                        print (y)
                        #check = input('')
                        # print (row)
                        writer.writerow(row)
                        matchcount = matchcount + 1
                    else:
                        pass
                        passcount = passcount + 1
            rowcount = rowcount + 1
        file.seek(0)
processpercent = matchcount/rowcount * 100
print ('Complete! # of rows processed: ' + str(rowcount))
print ('# of rows with filter match: ' + str(matchcount))
print ('# of rows passed: ' + str(passcount))
print ('Percent Processed: ' + str(processpercent))
