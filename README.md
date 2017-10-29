# web-scrapping-and-crawling

<code> Project Setup Guide </code>

Python : sudo apt-get install python

Installing PIP : sudo apt-get install python-pip

Install the following Libraries

Pandas : pip install pandas
xlrd: pip install xlrd
requests : pip install requests
BeautifulSoup : pip install beautifulsoup

<code>Running The script</code>

1. Open the terminal and go to the project directory.
2. Enter pwd and copy the path of proect directory and replace this with the path variable in line no 33 in main.py file.
   For Example : #chhange path here <br>
   path="/home/sakir/Desktop/blue/result/"+company_name; <br>
   change this to <br>
   #chhange path here <br>
   path="YOUR PATH HERE/result/"+company_name; <br>
3. Now to run the script using the following command.
   <code>
    python main.py PermID HierarchicalId
   </code>
   NOTE : replace PermId and HierarchicalID with the id you want to search.
   Example(for searching uranium) <code> python main.py 4294952775 50301010.
4. The output will be stored in the <code>result</code> directory. The Output will be as follows:
   Directory with the same of company.
   In Each Directory there will be a file called company_ranking.csv which will store the company ranking data.
   And other files with the name_of_company.csv which will store the employee data.

 
