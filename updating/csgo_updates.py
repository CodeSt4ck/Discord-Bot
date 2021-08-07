import time
import requests
import os
import json
from bs4 import BeautifulSoup

os.chdir(r'/Users/jangi/Desktop/Discord Bot')

def search_updates():
    print('Running')
    updates_url = requests.get('https://blog.counter-strike.net/index.php/category/updates/').text
    #print(updates_url)
    soup = BeautifulSoup(updates_url, 'lxml')

    post_link = soup.find('h2').a['href']

    info_url = requests.get(str(post_link)).text

    info_soup = BeautifulSoup(info_url, 'lxml')

    release_note = info_soup.find('h2').text

    post_date = info_soup.find('p', class_='post_date').text.replace('-', '')
    post_date = 'Date : ' + post_date

    update_info = info_soup.find_all('p', class_=None)[0:-1]
    patches = ''
    for info in update_info:
        patches = patches + info.get_text()

    with open('data/updates.json', 'r') as f:
        updates = json.load(f)
        if post_link not in updates:
            updates[str(post_link)] = {}
            updates[str(post_link)]['ReleaseNotes'] = release_note
            updates[str(post_link)]['Date'] = post_date
            updates[str(post_link)]['PatchNotes'] = patches
    with open('data/updates.json', 'w') as f:
        json.dump(updates, f)

if __name__ == '__main__':
    while True:
        search_updates()
        hour = 12
        min = 60
        print(f'Reloading after {hour} hours.')
        time.sleep(hour * min * 60)