print ('===========================')
print ('Welcome to the Pixel Generator')
print ('Note: Custom Params must be built outside of this tool')
servernumber = input('What Server is this pixel being built for? ')
profiletoken = input('What is the profile token (full string from profile)? ')
convtypecount = 1
convtypes = []
while True:
    convtypename = input('Conv Type ' + str(convtypecount) + ' (enter "Done" after last Conv Type):')
    convtypecount = convtypecount + 1
    if convtypename == 'Done':
        break
    else:
        convtypes.append(convtypename)

for convtype in convtypes:
    pixel = '''
<script type=text/javascript src="https://services.xg4ken.com/js/kenshoo.js?cid="'%s'></script>
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
    print(pixel)
    filename = 'ks' + servernumber + '_' + convtype +'.txt'
    pixelfile = open(filename, 'w')
    pixelfile.write(pixel)
