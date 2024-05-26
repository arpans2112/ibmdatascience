'''
Webscraping is the reading data from the web site.  

soup.title                 -- gives title of the html page. </br> 
soup.h3                    -- gives the first h3 element from the top.  </br> 
soup.h3.b                  -- gives the child tag of the first h3 tag.  </br> 
soup.h3.b.parent           -- gives the parent of the tag b. i.e soup.h3 </br> 
soup.h3.next_sibling       -- Gives the sibling tag of the tag h3 </br> 
soup.h3.attrs              --  returns the dictionary of all the attributes as key and value pair </br> 
soup.h3.string             -- returns the text(content) of the h3 tag. </br> 
soup.find_all(name='tag')  -- returns list of all the objects with given tag name. </br> 



# sample code
from bs4 import BeautifulSoup
page_html = request.get(url).text
soup = BeautifulSoup(page_html,'html.parser')
artists_links. = soup.find_all('a')

'''

first_element = 'arpan'

