'''
Made by Wotwarrior
https://github.com/Wotwarrior
                    _       _     _ 
               /\  | |     | |   | |
  ___ _ __    /  \ | |_ ___| |__ | |
 / __| '_ \  / /\ \| __/ __| '_ \| |
 \__ \ | | |/ ____ \ || (__| | | |_|
 |___/_| |_/_/    \_\__\___|_| |_(_)

'''
# Requires beautifulsoup and requests for HTML scraping
import time
import requests
from bs4 import BeautifulSoup
# Simple loop to keep it going
print ("""
Made by Wotwarrior
https://github.com/Wotwarrior
                    _       _     _ 
               /\  | |     | |   | |
  ___ _ __    /  \ | |_ ___| |__ | |
 / __| '_ \  / /\ \| __/ __| '_ \| |
 \__ \ | | |/ ____ \ || (__| | | |_|
 |___/_| |_/_/    \_\__\___|_| |_(_) Proxy Scanner
 """)    
while True:
        # Requesting page
        page = requests.get("https://www.free-proxy-list.net")
        # Verifying successful page download. A returned value of 200 is wanted.
        success = page.status_code
        if success == 200:
                print ("Page successfully downloaded!")
        else:
                retry = str(input("Page not found. Retry? (Y/n)   "))
                retry = retry.lower()
                if retry == "y":
                        print ("Restarting...")
                        continue
                else:
                        print ("Stopping...")
                        break
        # HTML Parsing (Splitting code) & finding the proxies section
        split = BeautifulSoup(page.content, 'html.parser')
        split = split.body
        proxies = split.find("section", id="list")
        proxies = proxies.find("tbody")
        count = -1
        file = open("proxies.txt", "a")
        # Copying the proxies & checking if they're HTTPS compatible as per the website's standards
        for i in range(300):
                count = count + 1
                proxy = proxies.find_all("tr")[count]
                https = proxy.find_all()[6]
                https = https.text
                level = proxy.find_all()[4]
                level = level.text
                if https == ("yes"):
                        if level == ("elite proxy"):
                                ip = proxy.find_all()[0]
                                port = proxy.find_all()[1]
                                ip = ip.text
                                port = port.text
                                # Writing the proxies to the proxy file
                                string = (ip + ", " + port + "\n")
                                file.write(string)
                        else:
                                continue
                else:
                        continue
        file = file.close()        
        print ("""
----------------------------------
           COMPLETED
----------------------------------
Scanner will scan again in 10 mins
----------------------------------
            """)
        # Waiting 10 minuites, because that's the website's reloading time
        time.sleep(600)
