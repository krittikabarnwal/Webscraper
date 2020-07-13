import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

#link to website
my_url='https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphic%20cards'

uClient=uReq(my_url)

page_html=uClient.read()

uClient.close()

page_soup=soup(page_html,"html.parser")

containers=page_soup.findAll("div",{"class":"item-container"})

#Creating the csv file
filename="Products.csv"
f=open(filename,"w")

headers= "brand,product,shipping\n"
f.write(headers)

#looping through all the products
for container in containers:

	product_name=container.img["title"]

	brand_container=container.findAll("a",{"class":"item-brand"})

	brand_name=brand_container[0].img["title"]

	shipping_container=container.findAll("li",{"class":"price-ship"})

	shipping=shipping_container[0].text.strip()

	f.write(brand_name + ","+product_name.replace(",","|")+","+shipping+"\n")

f.close()