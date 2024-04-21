# crd to https://github.com/0MeMo07
import requests
import time
import re
import random


class Colors:
    light_blue = '\033[94m'
    golden = '\033[93m'
    green = '\033[92m'
    red = '\033[91m'
    end = '\033[0m'


class Colorate:
    @staticmethod
    def Vertical(color, text):
        return f"{color}{text}{Colors.end}"
def extract_username(url):
    pattern = r"https://[^/]+/(\w+)"
    match = re.match(pattern, url)
    if match:
        return match.group(1)
    else:
        raise ValueError("Invalid URL format")


def print_banner():
    banner = '''

 .-. .-.  ,--,   ,-.         ,-. .-.,-.,-.    ,-.    ,---.  ,---.    
 |  \| |.' .'    | |         | |/ / |(|| |    | |    | .-'  | .-.\   
 |   | ||  |  __ | |____.___ | | /  (_)| |    | |    | `-.  | `-'/   
 | |\  |\  \ ( _)| |`----==='| | \  | || |    | |    | .-'  |   (    
 | | |)| \  `-) )| `--.      | |) \ | || `--. | `--. |  `--.| |\ \   
 /(  (_) )\____/ |( __.'     |((_)-'`-'|( __.'|( __.'/( __.'|_| \)\  
(__)    (__)     (_)         (_)       (_)    (_)   (__)        (__) 

    '''
    print(Colorate.Vertical(Colors.green, banner))




def generate_random_string(length):
    characters = 'abcdefghijklmnopqrstuvwxyz0123456789'
    return ''.join(random.choice(characters) for _ in range(length))

def generate_random_uuid():
    segments = [
        generate_random_string(8),
        generate_random_string(4),
        generate_random_string(4),
        generate_random_string(4),
        generate_random_string(12)
    ]
    return '-'.join(segments)



def print_author_info():
    author_info = '''
    ===========================================
                Author Information
    ===========================================
    [Author]:    Aether
    [GitHub]:    https://github.com/Aether-0
    [Telegram]:  https://t.me/a37h3r
    ===========================================
    '''
    print(Colorate.Vertical(Colors.golden, author_info))


try:
    print_banner()
    print_author_info()
    url = input(Colorate.Vertical(Colors.light_blue, "[🔗]Url: "))
    nglusername = extract_username(url)
    message = input(Colorate.Vertical(Colors.light_blue, "[💬]Message: "))
    count = int(input(Colorate.Vertical(Colors.light_blue, "[🚀]Count: ")))

    value = 0
    not_send = 0

    ug = [
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.94 Chrome/37.0.2062.94 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9'
    ]

    random_user_agent = random.choice(ug)
    random_uuid = generate_random_uuid()
    while value < count:
        headers = {
            'Host': 'ngl.link',
            'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A-Brand";v="24"',
            'accept': '*/*',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'x-requested-with': 'XMLHttpRequest',
            'sec-ch-ua-mobile': '?0',
            'user-agent': f'{random_user_agent}',
            'sec-ch-ua-platform': '"Windows"',
            'origin': 'https://ngl.link',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': f'https://ngl.link/{nglusername}',
            'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
        }

        data = {
            'username': nglusername,
            'question': message,
            'deviceId': f'{random_uuid}',
            'gameSlug': '',
            'referrer': '',
        }

        try:
            response = requests.post('https://ngl.link/api/submit', headers=headers, data=data, )
            response.raise_for_status()  # Raise an HTTPError for bad responses
            if response.status_code == 200:
                not_send = 0
                value += 1
                print(Colorate.Vertical(Colors.green, "[✔]"), f"{message} sent ➤ {value}")
        except requests.RequestException as e:
            not_send += 1
            print(Colorate.Vertical(Colors.red, "[X]"), f"{message} not sent")
            if not_send == 10:
                print(Colorate.Vertical(Colors.golden, "[(^_^)]"), "Waiting 5 Seconds...")
                time.sleep(5)
                not_send = 0

except ValueError as e:
    print(Colorate.Vertical(Colors.red, f"Error: {e}"))
except KeyboardInterrupt:
    print(Colorate.Vertical(Colors.red, "\nUser Interrupted"))
except Exception as e:
    print(Colorate.Vertical(Colors.red, f"An unexpected error occurred: {e}"))
    
