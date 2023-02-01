import requests
import lxml
from bs4 import BeautifulSoup
import smtplib

amazon_url = "https://www.amazon.com/Roland-SP-404MKII-Creative-Polyphony-SP-404MK2/dp/B09J1TMSYV"

headers = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
}

response = requests.get(amazon_url, headers=headers)

soup = BeautifulSoup(response.content, "lxml")
# print(soup.prettify())

whole = soup.find(class_="a-price-whole").get_text()
fraction = soup.find(class_="a-price-fraction").get_text()

price = float(whole + fraction)
print(price)

item = amazon_url[23:40]
print(item)
# smtplib.SMTP("smtp.gmail.com", port=587)

host = "smtp.gmail.com"
sender = "robgordongarcia@gmail.com"
password = ""
receiver = "robgordongarcia@gmail.com"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=sender, password=password)
    connection.sendmail(from_addr=sender,
                        to_addrs=receiver,
                        msg=f"Subject:{item}\n\nA {item} is on sale on Amazon for only ${price}!\nOrder Now\n\n{amazon_url}")
