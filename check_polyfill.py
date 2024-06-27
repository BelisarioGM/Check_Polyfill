import requests
from bs4 import BeautifulSoup
import argparse

def check_polyfill(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            scripts = soup.find_all('script')
            for script in scripts:
                if script.get('src') and 'polyfill.io' in script.get('src'):
                    print(f'[+] Found polyfill.io in {url}')
                    return True
        print(f'[-] polyfill.io not found in {url}')
        return False
    except requests.RequestException as e:
        print(f'[-] Error accessing {url}: {e}')
        return False

def main():
    parser = argparse.ArgumentParser(description='Check if a website uses polyfill.io')
    parser.add_argument('-u', '--url', type=str, required=True, help='URL of the website to check')
    args = parser.parse_args()

    url = args.url
    if not url.startswith('http'):
        url = 'http://' + url
    
    check_polyfill(url)

if __name__ == '__main__':
    main()

