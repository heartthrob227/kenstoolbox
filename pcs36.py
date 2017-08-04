### Version 0.5.0 (Python 3.6)
### Version Notes: Added Google Drive Upload Functionality
### Last Edit 4/19/2017
### Last Editor Dennis

import io
import csv
import pymysql as p
from zipfile import *
# import smtplib
# import mimetypes
# from email.mime.multipart import MIMEMultipart
# from email import encoders
# from email.message import Message
# from email.mime.base import MIMEBase
# from email.mime.text import MIMEText
# from pydrive.auth import GoogleAuth
# from pydrive.drive import GoogleDrive
# from pydrive.files import *

print ('===========================')
print ('Welcome to the Pixel Generator')
print ('Note: Custom Params must be built outside of this tool')

#Get Server Number
servernumber = input('What Server is this pixel being built for (Currenly does not support servers that are in the 1000s)? ')
profilenumber = input('What profile numbers are we building for? (Comma delimited, no spaces) ')
var1 = profilenumber.split(',')
inputprofilenum = []
for x in var1:
    quotes = "'"+x+"'"
    inputprofilenum.append(quotes)
sqlprofilenumber = ",".join(inputprofilenum)
#Get HTML or JS to build
htmlorjs = input('JS (J) or HTML (H) version (case sensitive)? ')
# Get your Conv Types
# inputconvtypelist = #####
convtypes = []
# var2 = convtypelist.split(',')
# for x in var2:
#     quotes1 = "'"+x+"'"
#     convtypes.append(quotes1)
convtypecount = 1
while True:
    convtypename = input('Conv Type ' + str(convtypecount) + ' (enter "Done" after last Conv Type):')
    convtypecount = convtypecount + 1
    if convtypename == 'Done':
        break
    else:
        convtypes.append(convtypename)
#toaddrs = input('What email address should we mail this to? ')
#connect to DB
host = 'eclidb%s.kenshooprd.local' % (servernumber)
conn = p.connect(host=host, user='query', password='query', db='kazaam')
#Set the cursor
a = conn.cursor()
#SQL Query
sql = "SELECT token, site_name FROM customer_profiles WHERE profile_id in (%s);" % (sqlprofilenumber)
countrow = a.execute(sql)
print ('# of Profiles: ',countrow)
#Fetch all data
data = a.fetchall()

zipfilename = servernumber + '_pixels_kenshoo.zip'
zip_archive = ZipFile(zipfilename, 'w')
# Unpack tuples to a,b
for a,b in data:
    profiletoken = a
    profilename = b
    #Write JS code
    if htmlorjs == 'J':
        for convtype in convtypes:
            pixel = '''
<script type=text/javascript src="https://services.xg4ken.com/js/kenshoo.js?cid=%s" ></script>
<script type=text/javascript>
kenshoo.trackConversion('%s','%s',{
   /*OPTIONAL PARAMETERS. FILL VALUES OR REMOVE UNNEEDED PARAMETERS*/
   conversionType: '%s', /*specific conversion type. example: type:'AppInstall' default is 'conv'*/
   revenue: 0.0, /*numeric conversion value. example convValue: 12.34*/
   currency:'USD', /*example currency:'USD'*/
   orderId:'',/*example orderId: 'abc'*/
   promoCode:'',
   customParam1:'', /*any custom parameter. example: Airport: 'JFK'*/
   customParam2:'' })
</script>

<noscript>
   <img src="https://%s.xg4ken.com/pixel/v1?track=1&token=%s&conversionType=%s&revenue=0.0&currency=USD&orderId=&promoCode=&customParam1=&customParam2=" width="1" height="1" />
</noscript>
                ''' % (profiletoken, servernumber, profiletoken, convtype, servernumber, profiletoken, convtype)

            #print(pixel)
            #print (type(filecontent))
            filename = profilename + '_' + 'ks' + servernumber + '_' + convtype +'.txt'
            pixelfile = open(filename, 'w')
            pixelfile.write(pixel)
            pixelfile.close()
            zip_archive.write(filename)


    #Write HTML code
    elif htmlorjs == 'H':
        for convtype in convtypes:
            pixel = '''
<img src="https://%s.xg4ken.com/pixel/v1?track=1&token=%s&conversionType=%s&revenue=0.0&currency=USD&orderId=&promoCode=&customParam1=&customParam2=" width="1" height="1" />
                ''' % (servernumber, profiletoken, convtype)
            #print(pixel)
            filename = profilename + '_' + 'ks' + servernumber + '_' + convtype +'.txt'
            pixelfile = open(filename, 'w')
            pixelfile.write(pixel)
            pixelfile.close()
            zip_archive.write(filename)
    else:
        print('this is not possible')

zip_archive.close()
# connect to Google Drive
# gauth = GoogleAuth()
# gauth.LocalWebserverAuth()
# drive = GoogleDrive(gauth)
# #Upload Zip
# fileupload = drive.CreateFile()
# fileupload.SetContentFile(zipfilename)
# fileupload.Upload()
# #Set permissions
# permission = fileupload.InsertPermission({'role':'writer','type':'anyone','withLink':'True'})
# print(fileupload['alternateLink'])
# downloadlink = fileupload['alternateLink']
#
# #Connect to Mail Server
# server = smtplib.SMTP('smtp.gmail.com:587')
# server.starttls()
# #Note: we need to get a neutral email address
# server.login('dennis.yu@kenshoo.com','odfddvbyeojuzmra')
#
# #Email details
# sender = 'dennis.yu@kenshoo.com'
# recipient = toaddrs
# msg = MIMEMultipart()
# msg['Subject'] = 'KS'+ servernumber+' | Your Pixels Have Arrived!'
# msg['To'] = toaddrs
# msg['From'] = 'dennis.yu@kenshoo.com'
# text = 'Download at this link:\n%s\n\nThis is an Automated Email.' % (downloadlink)
# body = MIMEText(text,'plain')
# msg.attach(body)
# msg = msg.as_string()
#
# server.sendmail(sender, recipient, msg)
print('Construction Complete.')
#server.quit()
