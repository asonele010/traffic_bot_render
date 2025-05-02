import requests
import time
from fake_useragent import UserAgent

def visit_site():
    ua = UserAgent()
    headers = {'User-Agent': ua.random}
    url = "https://trendingbuzz.netlify.app"  # Replace with your site URL

    try:
        res = requests.get(url, headers=headers)
        if res.status_code == 200:
            print(f"[+] Visit successful: {headers['User-Agent']}")
        else:
            print(f"[!] Failed: Status Code {res.status_code}")
    except Exception as e:
        print(f"[!] Error: {e}")

while True:
    visit_site()
    time.sleep(15)
