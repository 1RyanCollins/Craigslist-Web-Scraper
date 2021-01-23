import requests
import urllib.request
import time
from bs4 import BeautifulSoup


from requests import get
user_input = input("Enter url of a Craiglist page > " )
print("Completed...Running Scrape of " + str(user_input))
print("Here are the most relevant results:   ")
print(" ")

urls = [user_input] 

for url in urls:
    response = requests.get(url)



from bs4 import BeautifulSoup
html_soup = BeautifulSoup(response.content, 'html.parser')
type(html_soup)

x = html_soup.find_all('a', class_="result-title hdrlnk")


with open('Indy_gigs.txt', 'w', encoding = "utf-8") as f:
    for names in x:
        f.write('%s\n' % names.string)
        print('%s\n' % names.string)
        


f.close()

   


#print ( "count of food service  gigs is" + " " + str(len(food_service)))

#ratio = len(food_service) / len(mylines) 
        
#f.close()
#print(ratio)


        


