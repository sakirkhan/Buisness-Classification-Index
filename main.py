#Importing Libraries
import pandas #handeling Data using dataframes
import csv #creating and reading csv files
import os #creating Directories
import requests #downloading html content of the page
#from BeautifulSoup import BeautifulSoup #extracting data from Html page
from BeautifulSoup import BeautifulSoup
import sys #conversion of ASCII to UTF-8 and reading command line arguments
#Conversion o f ASCII TO UTF-8 reading format
reload(sys)
sys.setdefaultencoding('utf8')

#reading sample.xls File
df = pandas.read_excel('./sample.xls',columns=['company','PermID','HierarchicalID','IndustryID']);

#reading command line arguments
pId=int(sys.argv[1])
hId=int(sys.argv[2])

#searching for data item containing the PermID and HierarchicalID
data = df.loc[(df['PermID']==pId) & (df['HierarchicalID']==hId)]

c_name=list(data['company'])

print "Company found : "+c_name[0]

industry_code=list(data['IndustryID'])

#print industry_code[c_name[0]]

company_name=c_name[0]

#Creating Directory to store result. please change the path to your program directory.(use pwd command on linux and append /result to it)

#chhange path here
path="/home/sakir/Desktop/blue/result/"+company_name;
#print path
if not os.path.exists(path):
    os.makedirs(path)
    #print company_name+" Directory Created"

print "Fetching Company Rankings"

#scraping company Rankings
url='https://www.reuters.com/sectors/industries/rankings?industryCode='+str(int(industry_code[0]))+'&view=size&page=-1&sortby=mktcap&sortdir=DESC'
#print url
response = requests.get(url)
html=response.content


soup = BeautifulSoup(html)
table=soup.find('tbody',attrs={'class':'dataSmall'})

list_of_rows = []
for row in table.findAll('tr'):
    list_of_cells = []
    for cell in row.findAll('td'):
        text = cell.text.replace('&nbsp;', '')
        list_of_cells.append(text)
    list_of_rows.append(list_of_cells)

#storing the company ranking into .csv file
path1="./result/"+c_name[0]+"/companies_ranking.csv"
outfile = open(path1, "wb")
writer = csv.writer(outfile)
writer.writerows(list_of_rows)

print "company Ranking Fetched Sucessfully"
print "Fetching Employee Details..."

#Scraping the Employee data
i=0
for item in list_of_rows:
    if i>=2:
        #print item[0]
        new_url="https://www.reuters.com/finance/stocks/company-officers/"+item[0]
        c1=item[1]
        response = requests.get(new_url)
        html=response.content

        soup = BeautifulSoup(html)
        table=soup.find('div',attrs={'class':'section'})

        list_of_rows = []
        j=0
        for tbody in table.findAll('tbody'):
            if j==2:
                break
            j+=1
            for row in tbody.findAll('tr'):
                list_of_cells = []
                for cell in row.findAll('td'):
                    text = cell.text.replace('&nbsp;', '')
                    list_of_cells.append(text)
                list_of_rows.append(list_of_cells)

        filePathName="./result/"+company_name+"/"+c1+".csv"

        outfile = open(filePathName, "wb")
        writer = csv.writer(outfile)
        writer.writerows(list_of_rows)
    i+=1


print "Employee Details Fetched Sucessfully"
print "Result is stored at "+path
