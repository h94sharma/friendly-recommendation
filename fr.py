import requests
import xml.etree.ElementTree as ET

def authbaseInfo(root):
	'''
		This function give basic info about the author from the author search,
		api call.
	'''
	for author in root.iter('author'):
		aid = author.attrib['id']
		name = author.find('name').text
		print 'GR id is', aid,'and Name is',name
		print '<br>'
	return aid, name

def authInfo(root):
	'''
		This function gives more detalied info about the author, and some of his works 
		from the author api call.
	'''
	for author in root.iter('author'):
		if author.find('about') != None:
			about = (author.find('about').text).encode('utf-8')
			print '\n','About', name
			print '<br>'
			print about,'\n'
	print 'Here are some of', name+"'s most famous works:"
	for book in root.iter('book'):
		if book.find('title') != None:
			print 'Title: ', (book.find('title').text).encode('utf-8')
			print 'Goodreads Rating: ', (book.find('average_rating').text).encode('utf-8')
			print 'Link to Goodreads Page: ', (book.find('link').text).encode('utf-8')
			print 'Description: ', (book.find('description').text).encode('utf-8'),'\n'
		
#Insert a goodread dev api key
key = 'INSERT KEY HERE'
key = unicode(key)

#Getting author name to search
a = raw_input('Give me an author name: ')
a = unicode(a)
print '<p>'

#Making requests to goodread to find author id
r = requests.get('https://www.goodreads.com/api/author_url/%s?key=%s' % (a, key))
print 'Response: ', r.status_code
print '<br>'
root = ET.fromstring(r.text)
aid, name = authbaseInfo(root)

#Making request to goodread to find info about author
r= requests.get('https://www.goodreads.com/author/show/%s?format=xml&key=%s'%(aid, key))
root = ET.fromstring(r.content)
print 'Response: ', r.status_code
print '<br>'
authInfo(root)
