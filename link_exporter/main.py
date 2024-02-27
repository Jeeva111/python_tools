import requests
from bs4 import BeautifulSoup
# import webbrowser
import click

def get_text_by_class(url, class_name):
    # Send an HTTP GET request to the URL
    response = requests.get(url)
    
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all elements with the given class name
    elements = soup.find_all(class_=class_name)
    
    # Extract the text from each element
    text_list = [element.get_text().replace("\n", "") for element in elements]
    
    return text_list

def check_url_status(url):
    proxy = 'http://198.199.86.11:3128/'
    proxies = {
        'http': proxy,
        'https': proxy
    }
    try:
        response = requests.head("http://"+url, proxies=proxies)
        status_code = response.status_code
        return status_code
    except requests.exceptions.RequestException:
        return None

def get_url_with_proxy(url):
    proxy = "50.223.129.106:3128"
    proxies = {
        'http': proxy,
        'https': proxy
    }
    response = requests.get(url, proxies=proxies)
    return response.text

# Example usage
url = 'https://xranks.com/alternative/isaidub.com'  # Replace with your desired URL
class_name = 'font-weight-500 font-16'  # Replace with the desired class name
text_list = get_text_by_class(url, class_name)
for text in text_list:
    text = text.replace(" ", "")
    if(text != ""):
        # print(text)
        print(click.echo(click.style("http://"+text.lower(), fg='blue', underline=True), err=True))
        #webbrowser.open_new_tab("http://"+text)
        #click.echo(click.style("http://"+text, fg='blue', underline=True), err=True)
