import urllib2
import time

def get_price():
    page = urllib2.urlopen( "http://beans-r-us.biz/prices.html")
    text = page.read().decode("utf8")

    price_index = text.find(">$")

    start_of_price = price_index + 2
    end_of_price = price_index + 6

    price = float(text[start_of_price:end_of_price])

    return price


price_status = raw_input("Do you need the coffee price immediately? Y/N :  ")
print price_status

if price_status == "Y":
    price = get_price()
    print price
else:
    price = 99.99
    while price >6.0:
        price = get_price()
        print price
        time.sleep(9)
    print "Buy!"

    
        
        
    
