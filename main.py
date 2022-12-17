import requests
from bs4 import BeautifulSoup


def change_ip():
    # Use requests to send a GET request to the web page
    r = requests.get('https://checkip.dyndns.org')

    # Use BeautifulSoup to parse the HTML of the web page
    soup = BeautifulSoup(r.text, 'html.parser')

    # Find the element containing the IP address
    ip_element = soup.find('body').text

    # Extract the IP address from the element
    current_ip = ip_element.split(': ')[1].split('<')[0]
    print(f'Current IP: {current_ip}')

    # Use requests to send a POST request to the proxy website
    r = requests.post('https://www.proxy-list.download/api/v1/get', data={'type': 'http'})

    # Extract the IP address and port from the response
    new_ip = r.json()['Lists'][0]['ip']
    new_port = r.json()['Lists'][0]['port']
    print(f'New IP: {new_ip}:{new_port}')


change_ip()
