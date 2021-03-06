import json
import requests
import secrets
import time

startTime = time.time()

#call secrets for authentication
baseURL = secrets.baseURL
user = secrets.user
password = secrets.password

#authenticate session
auth = requests.post(baseURL + '/users/'+user+'/login?password='+password).json()
session = auth["session"]
headers = {'X-ArchivesSpace-Session':session, 'Content_Type':'application/json'}
print 'authenticated'

repo = raw_input("Enter repo ID; 2=RBML, 3=Avery, 4=Starr, 5= Burke:")
resource = raw_input("Enter resource ID:")

#define the API call to get EAD
endpoint = '/repositories/' + repo + '/resource_descriptions/' + resource + '.xml'

#optional parameters can be appended to the end of the above url - e.g. ?include_unpublished=true&include_daos=true&numbered_cs=true&print_pdf=true&ead3=true

#call the API
output = requests.get(baseURL + endpoint, headers=headers).text
print output

elapsedTime = time.time() - startTime
m, s = divmod(elapsedTime, 60)
h, m = divmod(m, 60)
print 'Total script run time: ', '%d:%02d:%02d' % (h, m, s)

