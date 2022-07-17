
#!/usr/bin/env python3
#Created By Aditya Singh ()
import subprocess
import sys
import os
import fileinput
import time
import pprint
import colorama
import re
from tabulate import tabulate
from colorama import Fore, Style
print(Style.BRIGHT + Fore.RED + r"""
            ;::::;
          ;::::; :;
        ;:::::'  :;
        ;:::::;    ;.
      ,:::::'      ;          OOO\
      ::::::;      ;          OOOOO\
      ;:::::;      ;        OOOOOOOO
      ,;::::::;    ;'        / OOOOOOO
    ;:::::::::`. ,,,;.        /  / DOOOOOO
  .';:::::::::::::::::;,    /  /    DOOOO
,::::::;::::::;;;;::::;,  /  /        DOOO
;`::::::`'::::::;;;::::: ,#/  /          DOOO
:`:::::::`;::::::;;::: ;::#  /            DOOO
::`:::::::`;:::::::: ;::::# /              DOO
`:`:::::::`;:::::: ;::::::#/              DOO
:::`:::::::`;; ;:::::::::##                OO
::::`:::::::`;::::::::;:::#                OO
`:::::`::::::::::::;'`:;::#                O
  `:::::`::::::::;' /  / `:#
  ::::::`:::::;'  /  /  `#
▓█████▄ ▓█████  ▄████▄  ▒█████  ███▄ ▄███▓ ██▓  █████▒▓██  ██▓
▒██▀ ██▌▓█  ▀ ▒██▀ ▀█  ▒██▒  ██▒▓██▒▀█▀ ██▒▓██▒▓██  ▒  ▒██  ██▒
░██  █▌▒███  ▒▓█    ▄ ▒██░  ██▒▓██    ▓██░▒██▒▒████ ░  ▒██ ██░
░▓█▄  ▌▒▓█  ▄ ▒▓▓▄ ▄██▒▒██  ██░▒██    ▒██ ░██░░▓█▒  ░  ░ ▐██▓░
░▒████▓ ░▒████▒▒ ▓███▀ ░░ ████▓▒░▒██▒  ░██▒░██░░▒█░      ░ ██▒▓░
▒▒▓  ▒ ░░ ▒░ ░░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒░  ░  ░░▓  ▒ ░      ██▒▒▒
░ ▒  ▒  ░ ░  ░  ░  ▒    ░ ▒ ▒░ ░  ░      ░ ▒ ░ ░      ▓██ ░▒░
░ ░  ░    ░  ░        ░ ░ ░ ▒  ░      ░    ▒ ░ ░ ░    ▒ ▒ ░░
  ░      ░  ░░ ░          ░ ░        ░    ░          ░ ░
░            ░                                        ░ ░
"""+ Style.RESET_ALL+"""
Created By: """+ Style.BRIGHT + Fore.GREEN +"""Aditya Singh"""+ Style.RESET_ALL +"""
Build: 1.0 (Users can now insert list of Hosts in console itslef)
""")

print("Attackbox Checks:"+ Style.BRIGHT + Fore.GREEN + " " + Style.RESET_ALL)

AccessibleIps=[]

HOST=[""]
Attackbox=[]

print(Style.BRIGHT + Fore.GREEN + '\nPlease select one of the following options:'+ Style.RESET_ALL)
val = input('Option 1 : Connectivity Scan \nOption 2 : Akamai Scan Check (Header Based)\nOption 3 : HTTP TRACE Method Check (Header Based)\n')

#Application Connectivity Scan

if val =='99':
url = input(Style.BRIGHT + Fore.GREEN + '\nInsert URL for Ping Scan'+ Style.RESET_ALL + '\nMultiple URLs can be added by adding a space\nExample: www.google.com facebook.com 192.168.0.1\n')
url = url.replace("http://","")
url = url.replace("https://","")
COMMAND="fping " + url

#print('\x1b[6;30;47m' + '\n' + '\x1b[0m')
print('\n')
print (Style.BRIGHT + Fore.GREEN + "[+] " + Style.RESET_ALL + 'Running Ping Scan on '+ Style.BRIGHT + Fore.GREEN+ "BDOC1"+ Style.RESET_ALL)
print ("Running command: " + COMMAND)  #Just for debugging
bdoc1Scan = subprocess.Popen([COMMAND],stdin =subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True,shell=True,bufsize=0)
bdoc1Scan.stdin.close()

for line in bdoc1Scan.stdout:
    fullstring = line.strip()
    substring = "alive"

    if substring in fullstring:
    print(Style.BRIGHT + Fore.RED + "[✯] " + line.strip() + Style.RESET_ALL)
    else:
    print(line.strip())
print(Style.BRIGHT + Fore.GREEN +"---------------------------------"+ Style.RESET_ALL)

for x in range(len(HOST)):
  print (Style.BRIGHT + Fore.GREEN + "[+] " + Style.RESET_ALL + 'Running Ping Scan on '+ Style.BRIGHT + Fore.GREEN+ Attackbox[x]+ Style.RESET_ALL)
  print ("Running command: " + COMMAND)  #Just for debugging
  ssh = subprocess.Popen(["ssh", HOST[x]],stdin =subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True,bufsize=0)

# Send ssh commands to stdin
  ssh.stdin.write(COMMAND+"\n")
  ssh.stdin.close()

# Fetch output
  for line in ssh.stdout:
    fullstring = line.strip()
    substring = "alive"

    if substring in fullstring:
    print(Style.BRIGHT + Fore.RED+ "[✯] " + line.strip() + Style.RESET_ALL)
    else:
    print(line.strip())
  print(Style.BRIGHT + Fore.GREEN +"---------------------------------"+ Style.RESET_ALL)


#----------------------------------------------------------------------------------------------------------------------------

#Network Decommission Scan

elif val =='1':
ScanIP=""
print(Style.BRIGHT + Fore.GREEN +'\nInsert Hosts: (To use a File list, insert a File name with .txt extension)'+ Style.RESET_ALL)
user_writing = []
while True:
  line = input()
  filename=line
  substring = ".txt"
  if substring in line:
  for line in fileinput.input(files =filename):
    ScanIP=ScanIP +" "+ line
  break
  else:
  if not line: # If line is blank
    break
  else:
    user_writing.append(line)
    ScanIP = ' '.join(user_writing)

ScanIP = ScanIP.replace("http://","")
ScanIP = ScanIP.replace("https://","")

ScanIP = ScanIP.strip()
iplist=[]
iplist = ScanIP.split()
iplist = list(set(iplist)) # Remove Duplicates
ScanIP=ScanIP.replace('\n', '')

option = input(Style.BRIGHT + Fore.GREEN +'\nPlease select one of the options below:'+ Style.RESET_ALL +'\nOption 1 : Scan APT Common ports(80/8080/443/9443/8443)\nOption 2 : Scan Top 1000 ports \nOption 3 : Scan specific port \n')
if option == "1":
  COMMAND="nmap " + ScanIP + " -sT -Pn -T5 -n --min-parallelism 100 -p 80,8080,443,9443,8443"+ """| awk '/^Nmap scan report/{cHost=$5;}
/open/ { split($1,a,"/"); result[cHost][a[1]]=""}
      END {
      for (i in result) {
        printf i;
        for (j in result[i])
          printf ",%s", j ;
        print ""} }' |
  sed -e 's/,/\t/'"""

elif option == "2":
  COMMAND="nmap " + ScanIP + " -sT -Pn -n -T5 --min-parallelism 100" """ | awk '/^Nmap scan report/{cHost=$5;}
/open/ { split($1,a,"/"); result[cHost][a[1]]=""}
      END {
      for (i in result) {
        printf i;
        for (j in result[i])
          printf ",%s", j ;
        print ""} }' |
  sed -e 's/,/\t/' """

elif option == "3":
  port = input(Style.BRIGHT + Fore.GREEN +'\nPlease input the specific ports to scan\n'+ Style.RESET_ALL +'Example: 80,443,445 \n')

  COMMAND="nmap " + ScanIP + " -sT -Pn -n -T5 --min-parallelism 100 -p "+port+ """ | awk '/^Nmap scan report/{cHost=$5;}
/open/ { split($1,a,"/"); result[cHost][a[1]]=""}
      END {
      for (i in result) {
        printf i;
        for (j in result[i])
          printf ",%s", j ;
        print ""} }' |
  sed -e 's/,/\t/' """

elif not option == "1" or val == "2" or val == "3" :
  sys.exit("Please choose Option 1 or 2 or 3")

print('\n')
print (Style.BRIGHT + Fore.GREEN + "[+] " + Style.RESET_ALL + 'Running Nmap Scan on '+ Style.BRIGHT + Fore.GREEN+ "BDOC1"+ Style.RESET_ALL)
# print ("Running command: " + COMMAND)  #Just for debugging

bdoc1Scan = subprocess.Popen([COMMAND],stdin =subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True,shell=True,bufsize=0)
bdoc1Scan.stdin.close()

printonlyonce=1;
for line in bdoc1Scan.stdout:
  AccessibleIps.append(line.strip() + " " + "BDOC1")
  ip=line.split()[0]
  ports=line.split()[1]
  if printonlyonce ==1:
  print(Style.BRIGHT + Fore.GREEN +"    Accessible Hosts/Ports"+Style.BRIGHT+ Style.RESET_ALL)
  print("    "+Style.BRIGHT + Fore.RED + ip+" "+ports + Style.RESET_ALL)
  printonlyonce=2
  else:
  print("    "+Style.BRIGHT + Fore.RED + ip+" "+ports + Style.RESET_ALL)
printonlyonce=1

# print(Style.BRIGHT + Fore.GREEN +" "+ Style.RESET_ALL)

for x in range(len(HOST)):
  print (Style.BRIGHT + Fore.GREEN + "[+] " + Style.RESET_ALL + 'Running Nmap Scan on '+ Style.BRIGHT + Fore.GREEN+ Attackbox[x]+ Style.RESET_ALL)
#  print ("Running command: " + COMMAND)  #Just for debugging
  ssh = subprocess.Popen(["ssh", HOST[x]],stdin =subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True,bufsize=0)

# Send ssh commands to stdin
  ssh.stdin.write(COMMAND+"\n")
  ssh.stdin.close()



# Fetch output
  printonlyonce=1;
  for line in ssh.stdout:
  AccessibleIps.append(line.strip() + " " + Attackbox[x])
  ip=line.split()[0]
  ports=line.split()[1]
  if printonlyonce ==1:
    print(Style.BRIGHT + Fore.GREEN +"    Accessible Hosts/Ports"+Style.BRIGHT+ Style.RESET_ALL)
    print("    "+Style.BRIGHT + Fore.RED + ip+" \t"+ports + Style.RESET_ALL)
    printonlyonce=2
  else:
    print("    "+Style.BRIGHT + Fore.RED + ip+" "+ports + Style.RESET_ALL)
printonlyonce=1
#  print(Style.BRIGHT + Fore.GREEN +" "+ Style.RESET_ALL)


AccessibleOnlyIps=[i.split()[0] for i in AccessibleIps]
AccessibleOnlyIps = list(set(AccessibleOnlyIps)) #Remove Duplicates

DecommissionedIps = list(set(AccessibleOnlyIps).symmetric_difference(set(iplist))) # Finding Decommissioned Hosts

iplist=sorted(iplist)
AccessibleOnlyIps=sorted(AccessibleOnlyIps)
DecommissionedIps=sorted(DecommissionedIps)

str1 = "\n".join(iplist)
str2 = "\n".join(AccessibleOnlyIps)
str3 = "\n".join(DecommissionedIps)

print ("\n"+Style.BRIGHT + Fore.GREEN +"[+] Results Of Decomify Scan:\n"+ Style.RESET_ALL)

print(tabulate([[str1,str2,str3]], headers=[Style.BRIGHT + Fore.GREEN +'Hosts Scanned', 'Accessible Hosts', 'Unreachable Hosts'+ Style.RESET_ALL], tablefmt='grid'))


#print (Style.BRIGHT + Fore.GREEN +"\n[+] Hosts Scanned:\n" + Style.RESET_ALL)
#print(*iplist, sep="\n")
print (Style.BRIGHT + Fore.GREEN +"\n[+] More Info On Accessible Hosts: (IP/Port/Attackbox)"+ Style.RESET_ALL)

AccessibleIps=sorted(AccessibleIps)
print (Style.BRIGHT + Fore.RED)
print(*AccessibleIps, sep="\n")
print (Style.RESET_ALL)

#print (Style.BRIGHT + Fore.GREEN +"\n[+] Decommissioned Hosts:\n"+ Style.RESET_ALL)
#print(*DecommissionedIps, sep="\n")
print ("\nResults have been saved to " + Style.BRIGHT + Fore.GREEN + "ScanResults.txt" + Style.RESET_ALL)

sys.stdout = open("ScanResults.txt", "w") #Save To File
print (Style.BRIGHT + Fore.GREEN +"\n[+] Hosts Scanned:\n" + Style.RESET_ALL)
print(*iplist, sep="\n")
print (Style.BRIGHT + Fore.GREEN +"\n[+] Accessible Hosts:"+ Style.RESET_ALL)
print (Style.BRIGHT + Fore.RED)
print(*AccessibleIps, sep="\n")
print (Style.RESET_ALL)
print (Style.BRIGHT + Fore.GREEN +"\n[+] Decommissioned Hosts:\n"+ Style.RESET_ALL)
print(*DecommissionedIps, sep="\n")
sys.stdout.close()

# Akamai Check Option

elif val =='2':
url = input(Style.BRIGHT + Fore.GREEN + '\nInsert URL for Akamai Scan'+ Style.RESET_ALL + '\nMultiple URLs can be added by adding a space\nExample: www.google.com facebook.com 192.168.133.7\n')
url = url.replace("http://","")
url = url.replace("https://","")
COMMAND="fping " + url

print('\n')
print (Style.BRIGHT + Fore.GREEN + "[+] " + Style.RESET_ALL + 'Running Ping Scan on '+ Style.BRIGHT + Fore.GREEN+ "BDOC1"+ Style.RESET_ALL)
print ("Running command: " + COMMAND)  #Just for debugging
bdoc1Scan = subprocess.Popen([COMMAND],stdin =subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True,shell=True,bufsize=0)
bdoc1Scan.stdin.close()

for line in bdoc1Scan.stdout:
    fullstring = line.strip()
    substring = "alive"
    if substring in fullstring:
    print("[✯] " + line.strip())
    result = re.search('(.*)is alive', fullstring)
    url=result.group(1)

    #Akamai Checks
    COMMAND="curl -I -H \"Host: akamaicheck\" " +"https://"+ url + "\n" #400 Error Detection
    #print(Style.BRIGHT + Fore.GREEN +"\nSearching for Akamai Headers"+ Style.RESET_ALL)
    ssh = subprocess.Popen([COMMAND],stdin =subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True,shell=True,bufsize=0)
    ssh.stdin.close()

    # Send ssh commands to stdin
    #print ("Running command: " + "curl -I -H \"Host: akamaicheck\" " +"https://"+ url + "\n")

    for line in ssh.stdout:
      fullstring = line.strip()
      substring = "akamai"

      if any(re.findall(substring, fullstring, re.IGNORECASE)):
      #print(Style.BRIGHT + Fore.RED+ "[✯] " + line.strip() + Style.RESET_ALL)
      print(Style.BRIGHT + Fore.RED+ "[✯] Akamai Detected on: " + url+"\n"+ Style.RESET_ALL)
      #else:
      #print(line.strip())
print(Style.BRIGHT + Fore.GREEN +"-------------------------------------------------------------"+ Style.RESET_ALL)





for x in range(len(HOST)):
  print (Style.BRIGHT + Fore.GREEN + "[+] " + Style.RESET_ALL + 'Running Ping Scan on '+ Style.BRIGHT + Fore.GREEN+ Attackbox[x]+ Style.RESET_ALL)
  print ("Running command: " + COMMAND)  #Just for debugging
  ssh = subprocess.Popen(["ssh", HOST[x]],stdin =subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True,bufsize=0)

# Send ssh commands to stdin
  ssh.stdin.write(COMMAND+"\n")
  ssh.stdin.close()

# Fetch output
  for line in ssh.stdout:
    fullstring = line.strip()
    substring = "alive"

    if substring in fullstring:
    print("[✯] " + line.strip())
    result = re.search('(.*)is alive', fullstring)
    url=result.group(1)

    #Akamai Checks
    #print(Style.BRIGHT + Fore.GREEN +"\nSearching for Akamai Headers"+ Style.RESET_ALL)
    ssh = subprocess.Popen(["ssh", HOST[x]],stdin =subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True,bufsize=0)

    # Send ssh commands to stdin
    #print ("Running command: " + "curl -I -H \"Host: akamaicheck\" " +"https://"+ url + "\n")
    ssh.stdin.write("curl -I -H \"Host: akamaicheck\" " +"https://"+ url + "\n") #400 Error Check
    ssh.stdin.close()


    for line in ssh.stdout:
      fullstring = line.strip()
      substring = "akamai"

      if any(re.findall(substring, fullstring, re.IGNORECASE)):
      print(Style.BRIGHT + Fore.RED+ "[✯] Akamai Detected on: " + url+"\n"+ Style.RESET_ALL)

      #else:
      #print(line.strip())
  print(Style.BRIGHT + Fore.GREEN +"-------------------------------------------------------------"+ Style.RESET_ALL)

# HTTP TRACE Method Enabled Option
elif val =='3':
ScanIP=""
print(Style.BRIGHT + Fore.GREEN +'\nInsert Hosts: (To use a File list, insert a File name with .txt extension)'+ Style.RESET_ALL)
user_writing = []
while True:
  line = input()
  filename=line
  substring = ".txt"
  if substring in line:
  for line in fileinput.input(files =filename):
    ScanIP=ScanIP +" "+ line
  break
  else:
  if not line: # If line is blank
    break
  else:
    user_writing.append(line)
    ScanIP = ' '.join(user_writing)

ScanIP = ScanIP.replace("http://","")
ScanIP = ScanIP.replace("https://","")

ScanIP = ScanIP.strip()
ScanIP=ScanIP.replace('\n', '')

COMMAND="curl --insecure -I -X TRACE "+ ScanIP + "

print('\n')
print (Style.BRIGHT + Fore.GREEN + "[+] " + Style.RESET_ALL + 'Running Ping Scan on '+ Style.BRIGHT + Fore.GREEN+ "BDOC1"+ Style.RESET_ALL)
print ("Running command: " + COMMAND)  #Just for debugging
bdoc1Scan = subprocess.Popen([COMMAND],stdin =subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True,shell=True,bufsize=0)
bdoc1Scan.stdin.close()

for line in bdoc1Scan.stdout:
    fullstring = line.strip()
    substring = "alive"
    if substring in fullstring:
    print("[✯] " + line.strip())
    result = re.search('(.*)is alive', fullstring)
    url=result.group(1)

    #HTTP TRACE Method Checks
    COMMAND="curl --insecure -I -X TRACE "+ url + "| awk 'NR==1' \n" #400 Error Detection
    #print(Style.BRIGHT + Fore.GREEN +"\nSearching for Akamai Headers"+ Style.RESET_ALL)
    ssh = subprocess.Popen([COMMAND],stdin =subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True,shell=True,bufsize=0)
    ssh.stdin.close()

    # Send ssh commands to stdin
    #print ("Running command: " + "curl -I -H \"Host: akamaicheck\" " +"https://"+ url + "\n")

    for line in ssh.stdout:
      print(line.strip())
print(Style.BRIGHT + Fore.GREEN +"-------------------------------------------------------------"+ Style.RESET_ALL)





for x in range(len(HOST)):
  print (Style.BRIGHT + Fore.GREEN + "[+] " + Style.RESET_ALL + 'Running Ping Scan on '+ Style.BRIGHT + Fore.GREEN+ Attackbox[x]+ Style.RESET_ALL)
  print ("Running command: " + COMMAND)  #Just for debugging
  ssh = subprocess.Popen(["ssh", HOST[x]],stdin =subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True,bufsize=0)

# Send ssh commands to stdin
  ssh.stdin.write(COMMAND+"\n")
  ssh.stdin.close()

# Fetch output
  for line in ssh.stdout:
    fullstring = line.strip()
    substring = "alive"

    if substring in fullstring:
    print("[✯] " + line.strip())
    result = re.search('(.*)is alive', fullstring)
    url=result.group(1)

    #Akamai Checks
    #print(Style.BRIGHT + Fore.GREEN +"\nSearching for Akamai Headers"+ Style.RESET_ALL)
    ssh = subprocess.Popen(["ssh", HOST[x]],stdin =subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True,bufsize=0)

    # Send ssh commands to stdin
    #print ("Running command: " + "curl -I -H \"Host: akamaicheck\" " +"https://"+ url + "\n")
    ssh.stdin.write("curl --insecure -I -X TRACE "+ url + "| awk 'NR==1' \n") #400 Error Check
    ssh.stdin.close()


    for line in ssh.stdout:
      print(line.strip())
  print(Style.BRIGHT + Fore.GREEN +"-------------------------------------------------------------"+ Style.RESET_ALL)


elif not val == "1" or val == "2" or val == "3" :
sys.exit("Please choose Option 1 or 2 or 3")
