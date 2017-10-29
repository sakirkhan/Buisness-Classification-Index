# Buisness-Classification-Index
<code> Project Setup Guide </code>

Python : sudo apt-get install python

Installing PIP : sudo apt-get install python-pip

Install the following Libraries

Pandas : pip install pandas
xlrd: pip install xlrd
requests : pip install requests
BeautifulSoup : pip install BeautifulSoup

<code>Running The script</code>

1. Open the terminal and go to the project directory.
2. Enter pwd and copy the path of proect directory and replace this with the path variable in line no 33 in main.py file.
   <code>For Example : #chhange path here <br>
   path="/home/sakir/Desktop/blue/result/"+company_name; <br>
   change this to <br>
   #chhange path here <br>
   path="YOUR PATH HERE/result/"+company_name; <br></code>
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

<code>NOTE :</code>
if the following error occurs :
  /usr/local/lib/python2.7/dist-packages/bs4/__init__.py:181: UserWarning: No parser was explicitly specified, so I'm using the best available HTML parser for this system ("lxml"). This usually isn't a problem, but if you run this code on another system, or in a different virtual environment, it may use a different parser and behave differently.


then change the following statments in line no 51 and 81 from
<code> soup = BeautifulSoup(html) </code> to <code> soup = BeautifulSoup(html,"lxml") </code>

