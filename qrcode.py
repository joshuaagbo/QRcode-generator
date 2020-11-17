import pyqrcode as pqr
import png;

from pyqrcode import QRCode

# a string to store generated QRCode
url_string = input("Enter the url to generate QRCode: ")

# name for the qrcode image file
qrcode_name = input("Enter name to save your file: ")

def concate_secure(url_str):#add https|http to url string if not included
    if  "https://" in url_string:
        if url_string.endswith(".com"):
            return url_string
        return url_string+".com"
    elif "http://" in url_string:
        if url_string.endswith(".com"):
            return url_string
        return url_string+".com"
    return (f"https://{url_string}.com")
    
    # format urls string
format_url= concate_secure(url_string)

# generate QRcode with  link 
code = pqr.create(format_url)


code.png(qrcode_name+".png",scale=6)

print("Completed!")



