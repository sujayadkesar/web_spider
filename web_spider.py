#!/usr/bin/python3
import os
import re
import random
import requests
import bs4
from tqdm import tqdm
import time
import json
import socket
from random import randint

def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)


# Display Banner
def banner():
    print("\n\n")
    print("""\033[1;32;40m
              ▓▓             ▒          ▒              ▓▓
              ▓             ▒            ▒              ▓  
              ▓             ▒  ▒      ▒  ▒              ▓
              ▓            ▓  ▒        ▒  ▓             ▓
              ▓            ▒▓  ▓      ▓  ▓▒             ▓
              ▓             ▒▓▓▒▓▓▓▓▓▓▒▓▓▒              ▓
              ▓             ▒▒▒▓██████▓▒▒▒              ▓
              ▓           ▓▓ ▒▒▓▓████▓▓▒  ▓▓            ▓
              ▓          ▒  ▓▓▒ ▓████▓ ▒▓▓  ▒           ▓
              ▓          ▒ ▒▓    ▒██▒    ▓  ▒           ▓
              ▓            ▒              ▒             ▓
              ▓             ▒            ▒              ▓
              ▓              ▒          ▒               ▓
              ▓      ╦ ╦┌─┐┌┐   ╔═╗┌─┐┬┌┬┐┌─┐┬─┐        ▓
              ▓      ║║║├┤ ├┴┐  ╚═╗├─┘│ ││├┤ ├┬┘        ▓
              ▓      ╚╩╝└─┘└─┘  ╚═╝┴  ┴─┴┘└─┘┴└─        ▓
              ▓▓                                       ▓▓  


    *════════════════════════════════════════════════════════════════*
      ╔════════════════════════════════════════════════════════════╗
      ║     By        : SUJAY ADKESAR                              ║
      ║     Portfolio : https://sujayadkesar.github.io/portfolio   ║                                                                          
      ║     Github    : https://github.com/sujayadkesar            ║
      ║     Licence   : MIT                                        ║
      ║     Code      : Python                                     ║ 
      ╚════════════════════════════════════════════════════════════╝
    *════════════════════════════════════════════════════════════════*

    """)
    print("\n")


# Get inputs from user
def get_user_inputs():
    global target_domain
    global website_name
    website_name = input("\033[1;36;40m [*] Enter the target website name! :-  ")
    target_domain = f"https://{website_name}"
    # dir_name = input("\n\n [*] Enter the name of new directory to store scan results :- ")
    # os.system('cd ~/Desktop')
    # path = os.getcwd()
    # os.system(f'mkdir {path}/{dir_name}')
    # os.system(f'cd {dir_name}')



# Finding Domai ip_address
def domain_ip():
    print("\n\n======================={   IP Details   }===========================\n\n")

    global website
    website = website_name
    try:
        print(f"\n\033[0;35m\033[1m\tHost name: \033[1m\033[0;32m \t{target_domain} \n")
        host_ip = socket.gethostbyname(website)
        print(f"\n\033[0;35m\033[1m\tDomain IP: \033[1m\033[0;32m \t{host_ip} \n")
        # print(host_ip)
    except:
        print("Unable to get Hostname and IP")





    response = requests.get(f'https://ipapi.co/{host_ip}/json/').json()

    print("\n\n\033[0;35m\033[1m\tDouble IP verification using IPinfo.io")
    print("\n\033[0;35m\033[1m\tResults:\033[0m\033[0;32m")

    response = requests.get(f'https://ipinfo.io/{host_ip}/json')
    data = json.loads(response.text)

    ip = data['ip']
    organization = data['org']
    city = data['city']
    region = data['region']
    country = data['country']
    location = data['loc']
    postal = data['postal']
    timezone = data['timezone']

    print("\tip            :", ip)
    print("\torganization  :", organization)
    print("\tcity          :", city)
    print("\tregion        :", region),
    print("\tcountry       :", country)
    print("\tpostal        :", postal)
    print("\tlocation      :", location)
    print("\ttimezone      :", timezone)






def Process_request():
    print("\n\n*════════════════════════════════════════════════════════════════*")
    print("\n\t [*] Getting Html content from the webpage . . . .")
    raw_response = requests.get(f'https://securityheaders.com/?q={target_domain}')
    html_content_ = raw_response.content
    global soup
    soup = bs4.BeautifulSoup(html_content_, 'html.parser')


    response = requests.get(target_domain)
    server = response.headers.get("server")

    session = requests.Session()
    response = session.get(target_domain)


    print(f"\n\t [*] Scanning {target_domain}  . . . .\n")
    time.sleep(3)
    print("\t [*] Scanning for injection vulnerabilities  . . . .\n")

    print("\t [*] Saving the results . . . . \n\n")

    global file_name
    file_name = input(f"\n[*] Enter the file name to store security headers details\n[!] Note: Must end with '.txt' :- ")
    store_result = open(f'{file_name}', 'w')

    for tr in soup.findAll("table", attrs={"class": "reportTable"}):
        store_result.write(tr.text)



    store_result.write(f" \n[*] Web-server :- {server} \n\n")
    store_result.write(f" [*] Set-cookie :- {session.cookies.get_dict()} ")
    # store_result.close()

    for i in tqdm(range(100)):
        time.sleep(0.06)

    print("\n\n")



    print("\n\n*═════════════════════ Manual Testing ═══════════════════════════*")
    target = f"{target_domain}"
    response = requests.get(target)
    header = response.headers


    # create_file = open(f'{file_name}' , 'a')
    # store_result.write("\n\n*═════════════════════{ SECURITY HEADER DETAILS }═══════════════════════════*")


    print("\n \t[*] Checking for HTTP Security Headers . . . .")
    time.sleep(3)
    print("\n \t[*] Checking X-XSS-Protection . . . .\n\n")
    time.sleep(3)
    print("\n \t[*] Verifying Content-Security-Policy { CSP } . . . .\n\n")

    for i in tqdm(range(100)):
        time.sleep(0.06)


    if 'Strict Transport Security' in header:
        pass
    else:
        store_result.write(" [*] Cookie hijacking and man in the middle attack is possible \n")
        store_result.write(" [*] Strict Transport Security header is not implemented in this website\n\n")

    if 'X-XSS-Protection' in header:
        pass
    else:
        store_result.write(" [*] Cross site scripting possibilities detected!\n")
        store_result.write(" [*] Additional XSS protection header is not implemented in this website\n\n")


    if 'X-Frame-Options' in header:
        pass
    else:
        store_result.write(" [*] Clickjacking possibility detected!\n")
        store_result.write(" [*] X-Frame-Options header is not implemented on this domain.\n\n")

    if 'X-Content-Type-Options' in header:
        pass
    else:
        store_result.write(" [*] MIME-sniffing vulnerability and User provided file acceptance is detected!\n")
        store_result.write(" [*] X-Content-Type-Option header is not implemented in this site\n\n")

    if 'Content-Security-Policy' in header:
        pass
    else:
        store_result.write(" [*] Cross-Site Scripting (XSS), ClickJacking, and HTML injection attacks. possibilities detected!\n")
        store_result.write(" [*] Content-Security-Policy header is not implemented in this site.\n\n")
    print("\n\n")
    print("\n\n\033[1;31;40M=========================={   NOTE   }================================\n\n")
    print(f"\033[1;31;40m\n\n \t[*] All hyperlinks on the web page are stored in all_links.txt ")
    print(f"\033[1;31;40m\n \t[*] The scan results are stored in {file_name}.txt")
    print("\n\n")
    print("\033[1;31;40M======================================================================")







def find_all_links():
    base_url = target_domain

    # get the html
    get_con = requests.get(base_url)
    html_content = get_con.content

    # parse the html content
    soup = bs4.BeautifulSoup(html_content, 'html.parser')

    # web page title
    title = soup.title
    print(title.text)

    # links
    all_links = set()
    searching_links = soup.findAll('a')



    def random_(n):
        range_start = 10 ** (n - 1)
        range_end = (10 ** n) - 1
        return randint(range_start, range_end)
    no = random_(2)
    all_link_File = f"all_links{no}.txt"
    link_file = open(f'{all_link_File}' , 'w')

    count_no = 0
    for link in searching_links:
        count_no += 1
        link_text = (link.get('href'))
        if re.findall('http*' , link_text):
            all_links.add(link_text)
        else:
            link_text = base_url + link_text
            all_links.add(link_text)

        link_file.write(f"{count_no} {link_text}\n")

# # crawl each and every link again at your own risk
#     for link in all_links:
#         linkText = (link.get('href'))
#         if re.findall('http*', linkText):
#             all_links.add(linkText)
#         else:
#             linkText = base_url + linkText
#             all_links.add(linkText)
#
#         link_file.write(f"{count_no) {linkText}\n")





def main():
    banner()
    get_user_inputs()
    domain_ip()
    Process_request()
    find_all_links()


main()







