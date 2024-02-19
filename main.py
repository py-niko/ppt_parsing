import requests
from bs4 import BeautifulSoup

storage_num = 1
link = f'https://magicdiagram.com/page/'
ppt_number = 0

for storage in range(35): # цикл по страницам
    response = requests.get(f'{link}{storage_num}').text
    soup = BeautifulSoup(response, 'lxml')
    block = soup.find('div', class_ = 'main-container')
    all_ppt = block.find_all('div', class_ = 'video-thumb')

    for ppt in all_ppt:
        ppt_link = ppt.find('a').get('href')
        download_storage = requests.get(f'{ppt_link}').text
        download_soup = BeautifulSoup(download_storage, 'lxml')
        download_block = download_soup.find('div', class_ = 'entry-content').find('div', class_ = 'attachment')
        result_link = download_block.find('a').get('href')

        # скачивание презентаций
        ppt_bytes = requests.get(f'{result_link}').content

        with open(f'/Users/k_nikolaev/Desktop/ppt_folder/{ppt_number}.ppt', 'wb') as file:
            file.write(ppt_bytes)

        ppt_number += 1
        print(f'Изображение {ppt_number}.ppt успешно загружено!')

    storage_num += 1
