import urllib2
import time


price = 99.99

while price > 4.74:
    
    page = urllib2.urlopen( "http://beans-r-us.biz/prices.html")
    text = page.read().decode("utf8")

    price_index = text.find(">$")

    start_of_price = price_index + 2
    end_of_price = price_index + 6

    price = float(text[start_of_price:end_of_price])

    print price

    time.sleep(90)

print "Buy!"


'''page2 = urllib2.urlopen( "http://beans-r-us.biz/prices-loyalty.html")
text2 = page2.read().decode("utf8")


print (text2)

price2 = text2[233:238]

print price2'''
