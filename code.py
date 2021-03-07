#importing all libraries
import pandas as pd
import io
import getpass
import requests
import datetime
from bs4 import BeautifulSoup
import smtplib

# Finding special index
def get_url():# A function for generating url for fetching data.
    current_time = datetime.datetime.now()
    s='https://www1.nseindia.com/content/indices/ind_close_all_'
    if current_time.day < 10:
        s=s+'0'+str(current_time.day)
    else:
        s=s+str(current_time.day-1)
    if current_time.month < 10:
        s=s+'0'+str(current_time.month)
    else:
        s=s+str(current_time.month)
    s=s+str(current_time.year)+'.csv'
    return s


email = ['1805037@kiit.ac.in','1805092@kiit.ac.in','1805109@kiit.ac.in','1805157@kiit.ac.in','1805142@kiit.ac.in','1805095@kiit.ac.in']
email.append('1805096@kiit.ac.in')
email.append('1805099@kiit.ac.in')
email.append('1805258@kiit.ac.in')
email.append('surajgupta6205@gmail.com')
email.append('ayushstar28@gmail.com')
email.append('yash6334@gmail.com')
email.append('singhrishita24@gmail.com')
email.append('ajay.anandfcs@kiit.ac.in')

#All mail id is stored in email named list.

url=get_url()# getting URL
s=requests.get(url).content  #getting content present in URL
df=pd.read_csv(io.StringIO(s.decode('utf-8')))   #converting content into dataframe

#Doing some operation on data

df1=df[df['Change(%)']>df['Change(%)'][0]]
df2=df[df['Change(%)']<df['Change(%)'][0]]

df1.sort_values(by=['Change(%)'], inplace=True, ascending=False)
df2.sort_values(by=['Change(%)'], inplace=True,ascending=False)

d1=list(df1.head()['Index Name'].values)#top gainers index
d2=list(df2.head()['Index Name'].values)#top loosers index


server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()  #Starting server
server.login("adarsh.nwd@gmail.com",getpass.getpass('Enter Password :'))    #Entering mail id and password for login
# getpass method will help in taking password masked text.


s1='TOP BULLISH INDEX:-\n'
count = 1
for i in d1:
    s1=s1+str(count)+". "+str(i)+'\n'
    count = count + 1
s1=s1+'\n\n\nTOP BEARISH INDEX:-\n'
count = 1
for i in d2:
    s1=s1+str(count)+". "+str(i)+'\n'
    count=count+1


subject = "NSE-INDEX MOVEMENT"  #subject of mail.
body="subject:{}\n\n{}".format(subject,s1) # Creating body for the mail
server.sendmail("adarsh.nwd@gmail.com",email,body)  # Mailing.


print("NSE-INDEX MOVEMENT DONE")
# ->    ->     ->     ->     ->     ->     ->     ->     ->     ->     ->     ->     ->

# Finding Stocks dragging Index up and down
URL = 'https://www.moneycontrol.com/indian-indices/nifty-50-9.html'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
result = soup.find(id='indi_contribute')
df = pd.read_html(str(result))# stocks dragging index(up and don both)
d1=df[0]# stocks dragging nifty up
d2=df[1]# stocks dragging nifty down

ite=list(d1.index)
count = 1
s1="STOCKS DRAGGING NIFTY UP:-\n"
for i in ite:
    s1=s1+str(count)+".\nCompany Name - "+str(d1['Stock Name'][i])+'\n'
    s1=s1+"CMP - "+str(d1['CMP'][i])+'\n'
    s1=s1+"Contribution = "+str(d1['Contribution'][i])+'\n\n'
    count = count + 1
    
s1 = s1+"\n\nSTOCKS DRAGGING NIFTY DOWN:-\n"
ite=list(d2.index)
count = 1
for i in ite:
    s1=s1+str(count)+".\nCompany Name - "+str(d2['Stock Name'][i])+'\n'
    s1=s1+"CMP - "+str(d2['CMP'][i])+'\n'
    s1=s1+"Contribution = "+str(d2['Contribution'][i])+'\n\n'
    count = count + 1

subject = "STOCKS DRAGGING NIFTY(NIFTY-50)"
body="subject:{}\n\n{}".format(subject,s1)
server.sendmail("adarsh.nwd@gmail.com",email,body)


print("STOCKS DRAGGING NIFTY DONE")

# ->    ->     ->     ->     ->     ->     ->     ->     ->     ->     ->     ->     ->

# Finding top & bottom 5 Stocks from NIFTY 200
url = 'https://www.moneycontrol.com/stocks/marketstats/indexcomp.php?optex=NSE&opttopic=indexcomp&index=49'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
result = soup.find(class_='tbldata14 bdrtpg')
df = pd.read_html(str(result))
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
result = soup.find(class_='tbldata14 bdrtpg')
df = pd.read_html(str(result))[0]
df.sort_values(by=['%Chg'], inplace=True, ascending=False)
gainers=df.head()# Contains top gainers from NIFTY 200
df.sort_values(by=['%Chg'], inplace=True, ascending=True)
loosers = df.head()# contains top loosers from NIFTY 200

ite=list(gainers.index)
count = 1
s1="GAINERS IN NIFTY 200:-\n"
for i in ite:
    s1=s1+str(count)+".\nCompany Name - "+str(gainers['Company Name'][i][:-34])+'\n'
    s1=s1+"Industry - "+str(gainers['Industry'][i])+'\n'
    s1=s1+"% change = "+str(gainers['%Chg'][i])+'\n\n'
    count = count + 1
    
s1 = s1+"\n\nLOOSERS IN NIFTY 200:-\n"
ite=list(loosers.index)
count = 1
for i in ite:
    s1=s1+str(count)+".\nCompany Name - "+str(loosers['Company Name'][i][:-34])+'\n'
    s1=s1+"Industry - "+str(loosers['Industry'][i])+'\n'
    s1=s1+"% change = "+str(loosers['%Chg'][i])+'\n\n'
    count = count + 1
    

subject = "GAINERS AND LOOSERS(NIFTY-200)"
body="subject:{}\n\n{}".format(subject,s1)
server.sendmail("adarsh.nwd@gmail.com",email,body)
    
print("GAINERS AND LOOSERS IN NIFTY 200 DONE")
server.quit()
