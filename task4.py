import types
import json
import urllib2
import socket

a = '--------------------------'
def registerUrl():
	try:
		url = 'http://github.com/inwk6312spring2019.html'
		data = urllib2.urlopen(url).read()
		return data
	except Exception,e:
		print(e)

def jsonFile(fileData):
	file = open('json.txt','w')
	file.write(fileData)
	file.close

def praserJsonFile(jsonData):
	value = json.loads(jsonData)
	rootlist = value.keys()
	print(rootlist)
	print(a)
	for rootkey in rootlist:
		print rootkey
	print(a)
	subvalue = value[rootkey]
	print(subvalue)
	print(a)
	for subkey in subvalue:
		print(subkey, subvalue[subkey])

if __name__ == '__main__':
	xinput = raw_input()
	x = 130
	xvalue = cmp(x, xinput)
	print(xvalue)
	print(x/100.0)
	data = registerUrl()
	jsonFile(data)
	praserJsonFile(data)

class Host():
	def gethostcount(self, hostId = ''):
		for host in response['result']:
			status = {'1':'OK', '0':'disabled'}
			available = {'0':'Unknown', '1':'available', '2':'Unavaiable'}
			host_dict['name']=host['name']
			host_dict['status']=status[host['status']]
			host_dict['available']=available[host['available']]
			return host_dict
