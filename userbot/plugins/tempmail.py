""" Temp mail retriever by @scifidemon """
from bs4 import BeautifulSoup
from requests import get
import re
import os
address = input("Enter the email: ")
URL = f"https://techrimail.herokuapp.com/{address}@t.techrim.tech"
page_src = get(URL)
soup = BeautifulSoup(page_src.text,"html.parser")
emails = soup.find_all("blockquote",{"class":"email"})
for i,email in enumerate(emails):
    sender = email.find("h6").text
    subject = email.find("p").text
    sender = os.linesep.join([s for s in sender.splitlines() if s])
    subject = os.linesep.join([s for s in subject.splitlines() if s])
    print(f"{i+1}) Sender and Date:")
    print (re.sub(' +',' ',sender))
    print("Subject:")
    print (re.sub(' +',' ',subject))
    print('\n')
    if i==4:
        break