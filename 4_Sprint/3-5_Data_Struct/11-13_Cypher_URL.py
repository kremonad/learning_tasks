import hashlib


class MarsURLEncoder:

    def __init__(self):
        self.url_storage = {}

    def encode(self, long_url):
        long_url_enc = long_url.encode(encoding='UTF-8')
        """Кодирует длинную ссылку в короткую вида https://ma.rs/X7NYIol."""
        hash = hashlib.sha256(long_url_enc).hexdigest()
        self.url_storage[hash] = long_url
        return f'https://ma.rs/{hash}'

    def decode(self, short_url):
        short_url = short_url.split('/')[-1]
        """Декодирует короткую ссылку вида https://ma.rs/X7NYIol в исходную."""
        return self.url_storage[short_url]

long_url = "https://tsup.ru/mars/marsohod-1/01-09-2023/daily_job.html"
x = MarsURLEncoder()
dec = x.encode(long_url)
print(dec)
print(x.decode(dec))