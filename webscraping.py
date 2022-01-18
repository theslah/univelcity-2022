# num = 10
# word = "new"

# try:
#     output = num + word
#     print(output)
# except:
#     new_output = str(10)
#     print(new_output)

import requests
from bs4 import BeautifulSoup as BS             

url = "https://jumia.com.ng/smartphones/"
headers = requests.utils.default_headers() #a dictionary method
headers.update({
    "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Sari/537.36" 
})

my_response = requests.get(url, headers)
# print(my_response.status_code)
first_soup = BS(my_response.content, features = "lxml")
#print(first_soup)
second_soup = first_soup.find("div", attrs = {"class" : "-paxs row _no-g _4cl-3cm-shs"})
#print(second_soup)
list_of_soups = second_soup.find_all("article", attrs = {"class" : "prd _fb col c-prd"})

for soup in list_of_soups:
    #print(soup.prettify())
    phone_details = soup.find("a")
    ####for phone brand
    # try:
    #     phone_brand = phone_details.get("data-brand")
    #     print(phone_brand)
    # except:
    #     phone_brand = none
    ### for phone specification
    try:
        phone_specification = phone_details.get("data-name")
        #print(phone_specification)
    except:
        phone_specification = none
    ##for phone old price
    try:
        old_div = soup.find("div", attrs = {"class" : "old"})
        phone_old_price = int((old_div.text).lstrip("₦ ").replace(",", ""))
        #print(phone_old_price)
    except:
        phone_old_price =None
    ### for new price
    try:
        new_div = soup.find("div", attrs = {"class" : "prc"})
        phone_new_price = int((new_div.text).lstrip("₦ ").replace(",", ""))
        #print(phone_new_price)
    except:
        phone_new_price = None
    ## for percentage
    try:
        discount = soup.find("div", attrs = {"class" : "tag _dsct _sm"})
        phone_discount = discount.text
        #print(phone_discount)
    except:
        phone_discount = None
    ### for rating
    try:
        rating = soup.find("div", attrs = {"class" : "stars _s"}) 
        phone_rating = (rating.text).strip(" out of 5")
        float_phone_rating = float(phone_rating)
        print(float_phone_rating)
    except:
        phone_rating = None



    



    break


