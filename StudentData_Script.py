import urllib.request
from bs4 import BeautifulSoup


"""
Currently for Y16 only ...
"""
for roll in range(160002,160832):
	url = "http://oa.cc.iitk.ac.in/Oa/Jsp/"+ "OAServices/IITk_SrchRes1.jsp?"+ "typ=stud&numtxt="+ str(roll) + "&sbm=Y"
	page = urllib.request.urlopen(url)

	list_array = []
"""
data extraction

"""
	soup = BeautifulSoup(page, "lxml")
	data = soup.find('tr', attrs={'class' : 'tablecontent'}).find_all("p")
	
"""
Username skipped-> difficulty in stripping white space bacause usename contained in anchor tag 
"""
	for i in range(0,4):
		list_array.append(data[i].contents[2].strip())

	for j in range(5,7):
		list_array.append(data[j].contents[2].strip())	
	

'''	
Function writefiles made to wrtie all the file with name of roll.txt having all the values corresponding to a field
'''
	def writeFiles: 
		file = open(str(roll)+".txt" , 'a')
		for item in list_array:
			file.write("%s\n" % item)
		file.close()

	writeFiles()			
		