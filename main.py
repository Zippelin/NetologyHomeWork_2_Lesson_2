import json
from urllib import parse
import requests
import hashlib

DB_FILE = 'db.json'
OUTPUT_FILE = 'out.txt'


# Задание 1
class WikiComposer:
    BASE_WIKI_URL = 'https://ru.wikipedia.org/wiki/'

    def __init__(self, file_path):
        self.file_path = file_path
        self.result_pairs = []
        with open(DB_FILE) as f:
            self.file_data = json.load(f)
        self.__inx = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.__inx += 1
        if self.__inx == len(self.file_data) - 1:
            raise StopIteration
        return self.file_data[self.__inx]

    def generate_urls(self):
        with open(OUTPUT_FILE, 'wt') as f:
            for record in self:
                url = str(parse.urljoin(self.BASE_WIKI_URL, record["translations"]["rus"]["official"]))
                # Закоментил, т.к. долго запросы делаются, да и не обязательно по задаче.
                # result = requests.get(url)
                # if result.status_code != 200:
                #     url = 'нет ссылки'
                f.write(f'({record["translations"]["rus"]["official"]}, {url}),\n')


# Задание 2
def file_crypt(file_ath):
    with open(file_ath, 'r') as f:
        yield hashlib.md5(f.readline().encode('utf-8')).hexdigest()
        next(f)


if __name__ == '__main__':
    # Задача 1
    pairs_saver = WikiComposer(DB_FILE)
    pairs_saver.generate_urls()

    # Задача 2
    for line in file_crypt('1.txt'):
        print(line)