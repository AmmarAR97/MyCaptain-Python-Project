import string
import requests
from bs4 import BeautifulSoup
import pandas
import argparse
import connect123

parser=argparse.ArgumentParser()
parser.add_argument("--page_num_max",help="Enter the number of pages to parse",type=int)
parser.add_argument("--dbname",help="Enter the db name", type=str)
args=parser.parse_args()

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
oyo_url="https://www.oyorooms.com/hotels-in-bangalore/?page="

page_num_MAX=args.page_num_max
scrapped_hotel_list=[]
connect123.connection(args.dbname)

for page_num in range(1,page_num_MAX):
    url=oyo_url+str(page_num_MAX)
    print("GET requested for "+url)
    req=requests.get(url,headers=headers)
    content = req.content

    soup=BeautifulSoup(content,"html.parser")

    all_hotels=soup.find_all("div",{"class":"listingHotelDescription"})

    for hotel in all_hotels:
        hotel_dict={}
        hotel_dict["Name"]= hotel.find("h3", {"class":"listingHotelDescription__hotelName"}).text
        hotel_dict["Address"]=hotel.find("span",{"itemprop":"streetAddress"}).text
        hotel_dict["Price"]=hotel.find("span" ,{"class":"listingPrice__finalPrice"}).text
        #try----except
        try:
            hotel_dict["Ratings"]=hotel.find("span" ,{"class":"hotelRating__ratingSummary"}).text
        except AttributeError:
            hotel_dict["Ratings"]=None
        parent_amenities_element=hotel.find("div",{"class":"amenityWrapper"})
        amenities_list=[]
        for amenities in parent_amenities_element.find_all("div",{"class":"amenityWrapper__amenity"}):
            amenities_list.append(amenities.find("span",{"class":"d-body-sm"}).text.strip())
        hotel_dict["amenities"]=", ".join(amenities_list[:-1])

        scrapped_hotel_list.append(hotel_dict)

        connect123.insert_into_table(args.dbname,tuple(hotel_dict.values()))

DataFrame= pandas.DataFrame(scrapped_hotel_list)
print("Creating csv file......")
DataFrame.to_csv("OYO.csv")
connect123.get_hotel_info(args.dbname)
