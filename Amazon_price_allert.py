import requests
from bs4 import BeautifulSoup
import smtplib
Url="https://www.amazon.in/OnePlus-Onyx-Black-128GB-Storage/dp/B071Z97T2C/ref=sr_1_1?crid=1SYGEQQI522QK&dchild=1&keywords=one+pluse8&qid=1610167907&sprefix=one+plus%2Caps%2C373&sr=8-1"
headers={"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}
def sentEmail(content):
    to="atultyagi.at.612@gmail.com"
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('your email id ', 'email id password')
        server.sendmail('your email id', to, content)
        print("sent successfully")
        server.close()
    except Exception as e:
        print(e)
while True:
    try:
        page = requests.get(Url, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        title = soup.find(id="productTitle")
        Title=str(title)

        title2 = soup.find(id="priceblock_ourprice")
        price = str(title2)
    except Exception as e:
        pass


    if title2!=None:

        item=Title.split('>')[1].split('<')[0].strip()
        price=price.split('₹')[1].split('<')[0].strip().split(",")
        price=float(price[0]+price[1])

        print(f"Item:-  {item}")
        print(f"Price :- {price}")
        if price<624991.0:
            content=f"Amazon Price Alert \n{item}\n\nLink :- {Url}\n\n Price:- {price}"
            sentEmail(content)


        break






