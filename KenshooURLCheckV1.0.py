import urllib.request, urllib.error, csv, re
from collections import defaultdict
print ('================================================')
print ('Welcome to the URL Checker!')
rawfile = input("what file do we want to process? ")
firstfile = rawfile + '.csv'
outputname = rawfile + '_testresults.csv'
fout=open(outputname,"w+", newline='')
columns = defaultdict(list)
option = input('Which option would you like to choose? \n1. Tracking Template Check \n2. URL Check \n3. Derp\nWhat is your option? ')


# def readlines():
#     with open(firstfile) as file:
#         reader = csv.DictReader(file, delimiter =',')
#         columnname = input('What is the exact column name we are looking for (case sensitive)? ')
#         for row in reader:
#             # print (row)
#             for (k,y) in row.items():
#                 # print ('==')
#                 # print (k)
#                 # print (y)
#                 # print ('==')
#                 if k == columnname:
#                     print (y)
#                 else:
#                     print ('That Column does not Exist')
#
#                 # print ('Printing Test Column Value')
#                 # subdict = dict((k,reader[columnname]))
#                 # print (subdict)


def trackingtemplatecheck():
    with open(firstfile) as file:
        tt_column = csv.DictReader(file, delimiter =',')
        header = tt_column.fieldnames

        # for line in tt_column:
        #     header = line
        #     break
        columnname = input('What is the exact column name we are looking for (case sensitive)? ')
        if columnname in header:
            print ('YAS')
        else:
            print ('BOO YOU')
        writer = csv.DictWriter(fout, fieldnames = header2)
        writer.writeheader()
        pattern = re.compile('.*\{lpurl\}.*|.*\{unescapedlpurl\}.*')
        rowcount = 0
        for row in tt_column:
            for (k,y) in row.items():

                if k == columnname:
                    print ('testing ' + y)
                    if pattern.match(y):
                        print('Good')
                    else:
                        print('TT not good. Writing full row to log file')
                        # affcode = re.findall('affcode\=(cr\d+|kw\d+|pg\d+)',tt)
                        writer.writerow(row)
                else:
                    print ('Processing...')
            rowcount += 1
    fout.close()
    print('Complete! ' + str(rowcount) + ' row(s) processed.')

def responsecode():
    with open(firstfile) as file:
        url_column = csv.DictReader(file, delimiter = ',')
        header = url_column.fieldnames
        columnname = input('What is the exact column name we are looking for (case sensitive)? ')
        if columnname in header:
            print ('YAS')
        else:
            print ('BOO YOU')
        writer = csv.DictWriter(fout, fieldnames = ['URL','Error Message'])
        writer.writeheader()
        for row in url_column:
            for (k,y) in row.items():
                if k == columnname:
                    print ('testing ' + y)
                    try:
                        conn = urllib.request.urlopen(y)
                    except urllib.error.HTTPError as e:
                        # Return code error (e.g. 404, 501, ...)
                        # ...
                        print(e.code)
                        # writer.writerow({"URL": url, "Error Message": str(e)})
                        writer.writerow(row, {'URL':y ,"Error Message": str(e)})
                    except urllib.error.URLError as e:
                        # Not an HTTP-specific error (e.g. connection refused)
                        # ...
                        print (e)
                        print('URLError - not a HTTP error')
                        print(e.args)
                        writer.writerow(row, {'URL':y ,"Error Message": str(e)})
                    else:
                        # 200
                        # ...
                        print(conn.getcode())
                        print('Good')
                else:
                    print ('Processing...')
    fout.close()
    print('Complete')

if option == '1':
    trackingtemplatecheck()
elif option == '2':
    responsecode()
elif option == '3':
    print('Derp')
    # readlines()
else:
    print('That is not a valid option. You should color inside the lines.')
