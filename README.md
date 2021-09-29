<h1 align="center">
  <br>
  <a href="https://github.com/shellreaper/Simple-Shodan"><img src="https://avatars.githubusercontent.com/u/73386311?s=400&u=33f552cb4457424c7747e1342dea442be8d9481d&v=4" alt="simple shodan"></a>
  <br>
  Simple-Shodan
  <br>
</h1>

<h4 align="center">Suite designed for passive recon</h4>

**Usage**: 
python3 setup.py
python3 simple-shodan.py


**Mechanism**

### CMS detection
  Detect the CMS and its version used in the web application

### FUZZING
  Fuzz the basic vulnerable directory and find sensitive files like .git, wp-json, xmlrpc, crossdomain, etc.
  
### javascript fetching
  fetch all the javascript files used in the webpage and displays on terminal

### Shodan search
  Fetch the cloudservices used in domain, country, area, ISP also fetch the open ports via searching on Shodan
  
### archieved URL search
  fetch all the URL from wayback machine or which are archieved by administrator
  
### DNS records
 Fetch all dns records of web application 
 - txt records
 - host records
 - mx records
 
**warning**
    This tool will throw an error if you don't provide valid api key 
 
 
