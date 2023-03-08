import subprocess
import importlib
import time
import os
import json
import datetime
import locale

# Dil dosyalarının bulunduğu klasör adı
LOCALE_DIR = "locale"
# Desteklenen dillerin listesi
SUPPORTED_LANGUAGES = ["en", "tr", "hi", "ml"]

# config.json dosyasını yükle
if os.path.exists("config.json"):
    # Config dosyasını yükleme
    with open("config.json", encoding="utf-8") as f:
        config_data = json.load(f)

# Kullanılacak dili belirleme
    if "lang" in config_data and config_data["lang"]:
        lang = config_data["lang"]
    else:
        # Sistem dilini belirle
        lang, encoding = locale.getdefaultlocale()
        if lang is None or lang.split("_")[0] not in SUPPORTED_LANGUAGES:
            lang = "en"
else:
    # Sistem dilini belirle
    lang, encoding = locale.getdefaultlocale()
    if lang is None or lang.split("_")[0] not in SUPPORTED_LANGUAGES:
        lang = "en"

# Dil dosyasını yükle
try:
    with open(os.path.join(LOCALE_DIR, f"{lang}.json"), "r", encoding="utf-8") as lang_file:
        lang_data = json.load(lang_file)
except (FileNotFoundError, json.JSONDecodeError):
    lang_data = {}

# Dil verilerindeki boşlukları doldurmak için varsayılan değerler
DEFAULT_LANG_DATA = {
    "warning_message": "Using this tool is at your own risk. We are not responsible for any account closures.",
    "github_link_message": "Github link: {link}",
    "license_message": "License: {license}",
    "developer_message": "Developer: {developer}",
    "description_message": "This software is developed for the friendship between Turkey and India.",
    "config_file_reconfigured_message": "Do you want to reconfigure the config file?",
    "select_language_message": "Select language. (e.g: {lang})",
    "enter_username_message": "Enter username.",
    "enter_password_message": "Enter password.",
    "enter_hashtags_message": "Enter hashtags. (e.g: turkey, india)",
    "enter_comments_message": "Enter comments. (e.g: i love turkey and india /n Turkey and India are friends /n turkey loves india)",
    "config_created_message": "config.json file created.",
    "config_loaded_message": "config.json file loaded.",
    "countdown_message": "Press any key to continue in {i} seconds...",
    "continue_message": "Continuing...",
    "login_success_message": "Successfully logged in.",
    "login_error_message": "Error occurred while logging in.",
    "video": "Video",
    "image": "Image",
    "tag_message": "Tag:",
    "count_message": "Count:",
    "media_url_message": "Media Url:",
    "media_time_message": "Media Time:",
    "media_id_message": "Media Id:",
    "user_id_message": "User İd:",
    "like_message": "Like made:",
    "comment_posted": "Comment posted:",
    "comment_liked": "Comment liked:",
    "error_message": "Error occurred, error code: {error}",
    "next_task_countdown": "Next task in {time} seconds."
}

# Dil dosyasındaki eksik verileri doldur
for key in DEFAULT_LANG_DATA.keys():
    lang_data.setdefault(key, DEFAULT_LANG_DATA[key])

# Kullanılan dil verilerinin yüklenmesi
LANG = lang_data


def install_module(module):
    subprocess.check_call(["pip", "install", module])
    importlib.import_module(module)


try:
    from bs4 import BeautifulSoup
except ImportError:
    install_module('beautifulsoup4')
    from bs4 import BeautifulSoup

try:
    import requests
except ImportError:
    install_module('requests')
    import requests

try:
    import msvcrt
except ImportError:
    if not os.name == 'nt':
        print("Sadece Windows'ta kullanılabilir!")
        exit()
    install_module('msvcrt')
    import msvcrt

try:
    import ctypes
except ImportError:
    if not os.name == 'nt':
        print("Sadece Windows'ta kullanılabilir!")
        exit()
    install_module('pywin32')
    import ctypes

try:
    import random
except ImportError:
    install_module('random2')
    import random

try:
    from colorama import init, Fore, Style
except ImportError:
    install_module('colorama')
    from colorama import init, Fore, Style


init(autoreset=True)


print(Fore.MAGENTA + """
  _           _ _                                 
 (_)         | (_)                                
  _ _ __   __| |_  __ _  __ _ _ __ __ _ _ __ ___  
 | | '_ \ / _` | |/ _` |/ _` | '__/ _` | '_ ` _ \ 
 | | | | | (_| | | (_| | (_| | | | (_| | | | | | |
 |_|_| |_|\__,_|_|\__,_|\__, |_|  \__,_|_| |_| |_|
                         __/ |                    
                        |___/                     
""" + Style.RESET_ALL)
print(Fore.BLUE + "[İ] " +
      LANG["description_message"] + Style.RESET_ALL)
print(Fore.BLUE + "[İ] " +
      LANG["developer_message"].format(developer="anonimbiri") + Style.RESET_ALL)
print(Fore.BLUE + "[İ] " + LANG["github_link_message"]
      .format(link="www.") + "\n", end="" + Style.RESET_ALL)
print(Fore.YELLOW + "[!] " +
      LANG["license_message"].format(license="MIT License") + Style.RESET_ALL)
print(Fore.RED + "[!] " + LANG["warning_message"] + "\n" + Style.RESET_ALL)


kernel32 = ctypes.windll.kernel32
hwnd = kernel32.GetConsoleWindow()
ctypes.windll.kernel32.SetConsoleTitleW("İndiagram")


def sor_ve_kaydet():
    # Kullanıcıdan soruları ve cevapları alır
    lang = input(
        "\n\n"+LANG["select_language_message"].format(lang=", ".join(SUPPORTED_LANGUAGES))+"\n")

    # Dil dosyasını yükle
    try:
        with open(os.path.join(LOCALE_DIR, f"{lang}.json"), "r", encoding="utf-8") as lang_file:
            lang_data = json.load(lang_file)
    except (FileNotFoundError, json.JSONDecodeError):
        lang_data = {}

    # Dil dosyasındaki eksik verileri doldur
    for key in DEFAULT_LANG_DATA.keys():
        lang_data.setdefault(key, DEFAULT_LANG_DATA[key])

    # Kullanılan dil verilerinin yüklenmesi
    LANG.update(lang_data)

    username = input("\n"+LANG["enter_username_message"]+"\n")
    password = input("\n"+LANG["enter_password_message"]+"\n")
    hashtag = input("\n"+LANG["enter_hashtags_message"]+"\n")
    hashtags = hashtag.split(",")
    comment = input(
        "\n"+LANG["enter_comments_message"]+"\n")
    comments = comment.split(" /n ")

    # Cevapları bir sözlük nesnesi olarak saklar
    cevaplar = {"lang": lang, "username": username,
                "password": password, "hashtags": hashtags, "comments": comments}

    # Cevapları "config.json" dosyasına kaydeder
    with open("config.json", "w") as f:
        json.dump(cevaplar, f)
        print("\n"+LANG["config_created_message"]+"\n")


if os.path.exists("config.json"):
    with open("config.json", "r") as f:
        config = json.load(f)
        config_copy = config.copy()
        if "password" in config_copy:
            config_copy["password"] = "*" * len(config["password"])
        print(Fore.YELLOW + json.dumps(config_copy, indent=4) + Style.RESET_ALL)
        print(LANG["config_loaded_message"]+"\n")
else:
    sor_ve_kaydet()
    with open("config.json", "r") as f:
        config = json.load(f)
        config_copy = config.copy()
        if "password" in config_copy:
            config_copy["password"] = "*" * len(config["password"])
        print(Fore.YELLOW + json.dumps(config_copy, indent=4) + Style.RESET_ALL)
        print(LANG["config_loaded_message"]+"\n")


print(LANG["config_file_reconfigured_message"])

for i in range(10, 0, -1):
    if msvcrt.kbhit():
        break
    print(f"\r"+LANG["countdown_message"].format(i=i), end="")
    time.sleep(1)

if msvcrt.kbhit():
    key = msvcrt.getch()
    sor_ve_kaydet()
else:
    print("\n"+LANG["continue_message"])

time.sleep(2)
def clear(): return os.system('cls||clear')


clear()

print(Fore.MAGENTA + """
  _           _ _                                 
 (_)         | (_)                                
  _ _ __   __| |_  __ _  __ _ _ __ __ _ _ __ ___  
 | | '_ \ / _` | |/ _` |/ _` | '__/ _` | '_ ` _ \ 
 | | | | | (_| | | (_| | (_| | | | (_| | | | | | |
 |_|_| |_|\__,_|_|\__,_|\__, |_|  \__,_|_| |_| |_|
                         __/ |                    
                        |___/                     
""" + Style.RESET_ALL)
print(Fore.BLUE + "[İ] " +
      LANG["description_message"] + Style.RESET_ALL)
print(Fore.BLUE + "[İ] " +
      LANG["developer_message"].format(developer="anonimbiri") + Style.RESET_ALL)
print(Fore.BLUE + "[İ] " + LANG["github_link_message"]
      .format(link="www.") + "\n", end="" + Style.RESET_ALL)
print(Fore.YELLOW + "[!] " +
      LANG["license_message"].format(license="MIT License") + Style.RESET_ALL)
print(Fore.RED + "[!] " + LANG["warning_message"] + "\n" + Style.RESET_ALL)

# Instagram kullanıcı adı ve şifresi
username = config['username']
password = config['password']

# Instagram ana sayfasına get isteği göndererek CSRF token'ı alınır
session = requests.Session()
session.headers.update({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Referer': 'https://www.instagram.com/'
})
session.get('https://www.instagram.com/')

session.cookies.update({
    'sessionid': '',
    'mid': '',
    'ig_pr': '1',
    'ig_vw': '1920',
    'csrftoken': '',
    's_network': '',
    'ds_user_id': ''
})


req = session.get("https://www.instagram.com/")
csrf_token = req.cookies['csrftoken']

# Instagram'a oturum açmak için post isteği gönderilir
login_data = {
    'username': username,
    'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{int(123456789)}:{password}',
    'queryParams': {},
    'optIntoOneTap': 'false'
}
login_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'X-CSRFToken': csrf_token,
    'X-Instagram-AJAX': '1',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': '*/*',
    'X-Requested-With': 'XMLHttpRequest',
    'Referer': 'https://www.instagram.com/',
    'Authority': 'www.instagram.com',
    'Origin': 'https://www.instagram.com',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
}
login = session.post('https://www.instagram.com/accounts/login/ajax/',
                     headers=login_headers, data=login_data)
login_json = login.json()

if login_json.get('authenticated'):
    print(LANG["login_success_message"])
else:
    print(LANG["login_error_message"])


next_task_time = time.time()
while True:
    remaining_time = next_task_time - time.time()
    if remaining_time > 0:
        print(
            f"\r"+LANG["next_task_countdown"].format(time=int(remaining_time)), end="\r")
        time.sleep(1)
    else:
        print(" " * 100, end="\r")
        # burada yapılacak işlemi yapabilirsiniz
        next_task_time = time.time() + 300  # bir sonraki 5 dakika için hesap yap
        tags = config['hashtags']
        tag = random.choice(tags)
        url = f'https://www.instagram.com/api/v1/tags/logged_out_web_info/?tag_name={tag}'

        info_headers = {
            'accept': '*/*',
            'accept-language': 'tr',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'viewport-width': '1536',
            'x-asbd-id': '198387',
            'x-csrftoken': csrf_token,
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': '0',
            'x-requested-with': 'XMLHttpRequest'
        }

        response = requests.get(url, headers=info_headers)
        data = response.json()

        count = data['count']
        media_id = data['data']['hashtag']['edge_hashtag_to_media']['edges'][0]['node']['id']
        media_code = data['data']['hashtag']['edge_hashtag_to_media']['edges'][0]['node']['shortcode']
        user_id = data['data']['hashtag']['edge_hashtag_to_media']['edges'][0]['node']['owner']['id']
        media_time = data['data']['hashtag']['edge_hashtag_to_media']['edges'][0]['node']['taken_at_timestamp']
        media_type = LANG["video"] if data['data']['hashtag']['edge_hashtag_to_media']['edges'][0]['node']['is_video'] else LANG["image"]

        dt_object = datetime.datetime.fromtimestamp(media_time)

        print(f'\n{Fore.YELLOW}[{media_type}]\n{Fore.GREEN}{LANG["tag_message"]} {Fore.YELLOW}{tag}\n{Fore.GREEN}{LANG["count_message"]} {Fore.YELLOW}{count}\n{Fore.GREEN}{LANG["media_url_message"]} {Fore.YELLOW}https://www.instagram.com/p/{media_code}/\n{Fore.GREEN}{LANG["media_time_message"]} {Fore.YELLOW}{dt_object}\n{Fore.GREEN}{LANG["media_id_message"]} {Fore.YELLOW}{media_id}\n{Fore.GREEN}{LANG["user_id_message"]} {Fore.YELLOW}{media_id}')

        kernel32 = ctypes.windll.kernel32
        hwnd = kernel32.GetConsoleWindow()
        ctypes.windll.kernel32.SetConsoleTitleW(
            f'[İndiagram] {LANG["tag_message"]} {tag} Like: {count}')

        # Beğeni yapmak için post isteği gönderilir
        like_url = f'https://www.instagram.com/api/v1/web/likes/{media_id}/like/'
        like_data = {
            'media_id': media_id,
            'csrf_token': csrf_token
        }
        like_headers = {
            'accept': '*/*',
            'accept-language': 'tr,tr-TR;q=0.9,en;q=0.8',
            'content-type': 'application/x-www-form-urlencoded',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'viewport-width': '1536',
            'x-asbd-id': '198387',
            'x-csrftoken': csrf_token,
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': '0',
            'x-requested-with': 'XMLHttpRequest'
        }

        like_request = session.post(
            like_url, data=like_data, headers=like_headers, cookies=req.cookies)

        # Beğeninin başarıyla gerçekleştirilip gerçekleştirilmediği kontrol edilir

        if like_request.status_code == 200:
            print(
                f'{Fore.MAGENTA}{LANG["like_message"]} {Fore.YELLOW}{media_id}')
        else:
            print(LANG["error_message"].format(
                error=like_request.status_code), end="")

        comments = config['comments']
        comment = random.choice(comments)

        comment_url = f'https://www.instagram.com/api/v1/web/comments/{media_id}/add/'
        comment_headers = {
            "accept": "*/*",
            "accept-language": "tr,tr-TR;q=0.9,en;q=0.8",
            "content-type": "application/x-www-form-urlencoded",
            "sec-ch-prefers-color-scheme": "dark",
            "sec-ch-ua": "\"Chromium\";v=\"110\", \"Not A(Brand\";v=\"24\", \"Google Chrome\";v=\"110\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "viewport-width": "1536",
            "x-asbd-id": "198387",
            "x-csrftoken": csrf_token,
            "x-ig-app-id": "936619743392459",
            "x-ig-www-claim": '0',
            "x-requested-with": "XMLHttpRequest"
        }
        comment_data = {"comment_text": comment}

        comment_request = session.post(
            comment_url, headers=comment_headers, data=comment_data, cookies=req.cookies)

        # cevap JSON veri yapısına dönüştürülüyor
        comment_request_json = comment_request.json()
        comment_id = comment_request_json["id"]

        if comment_request.status_code == 200:
            print(
                f'{Fore.MAGENTA}{LANG["comment_posted"]} {Fore.YELLOW}{media_id}')
        else:
            print(LANG["error_message"].format(
                error=comment_request.status_code), end="")

        comment_like_url = f'https://www.instagram.com/api/v1/web/comments/like/{comment_id}/'
        comment_like_headers = {
            "accept": "*/*",
            "accept-language": "tr,tr-TR;q=0.9,en;q=0.8",
            "content-type": "application/x-www-form-urlencoded",
            "sec-ch-prefers-color-scheme": "dark",
            "sec-ch-ua": "\"Chromium\";v=\"110\", \"Not A(Brand\";v=\"24\", \"Google Chrome\";v=\"110\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "viewport-width": "1536",
            "x-asbd-id": "198387",
            "x-csrftoken": csrf_token,
            "x-ig-app-id": "936619743392459",
            "x-ig-www-claim": '0',
            "x-requested-with": "XMLHttpRequest"
        }
        comment_like_data = {"comment_text": comment}

        comment_like_request = session.post(
            comment_like_url, headers=comment_like_headers, data=comment_like_data, cookies=req.cookies)

        if comment_like_request.status_code == 200:
            print(
                f'{Fore.MAGENTA}{LANG["comment_liked"]} {Fore.YELLOW}{comment_id}{Style.RESET_ALL}')
        else:
            print(LANG["error_message"].format(
                error=comment_like_request.status_code), end="")

        print("\n"+"-" * 100 + "\n")
