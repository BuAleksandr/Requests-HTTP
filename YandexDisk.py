import requests

with open('yandex_disk_token.txt', 'r') as file:
    token = file.read().strip()

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        params = {
            'path': name_file
        }
        headers = {
            'content-type': 'application/json',
            'accept': 'application/json', 'authorization': f'OAuth {uploader.token}'
        }
        req = requests.get(API_BASE_URL + "/v1/disk/resources/upload", params=params, headers=headers)
        upload_url = req.json()["href"]
        requests.put(upload_url, headers=headers, files={'file': path_to_file})


if __name__ == '__main__':
    token = 'Тут токен'
    API_BASE_URL = "https://cloud-api.yandex.net:443"
    name_file = '№33.jpg'
    path_to_file = "C://Users/BuniN/Desktop/№33.jpg"
    uploader = YaUploader(token)
    uploader.upload(path_to_file)
