import configparser
import requests as req

from csv_handler import CSV
from requests_oauthlib import OAuth1


config = configparser.ConfigParser()
config.read('config.ini')

NAME = config['translation_api']['name']
KEY = config['translation_api']['key']
SECRET = config['translation_api']['secret']
URL = config['translation_api']['url']

class Translation:

    def __init__(self):
        pass

    def do(self, text):
        consumer = OAuth1(KEY , SECRET)

        params = {
            'key': KEY,
            'name': NAME,
            'type': 'json',
            'text': text,
            'split': 0
        }    # その他のパラメータについては、各APIのリクエストパラメータに従って設定してください。

        try:
            res = req.post(URL, data=params , auth=consumer)
            res.encoding = 'utf-8'
            # print("[res]")
            # print(res)
        except Exception as e:
            print('=== Error ===')
            print('type:' + str(type(e)))
            print('args:' + str(e.args))
            print('e:' + str(e))
            raise

        j = res.json()
        return res
    
    def extract_text(self, j: dict) -> str:
        status = j['resultset']['code']
        if status == 0:
            text = j['resultset']['result']['information']['text-t']
        else:
            text = 'Error'
        return text


def full_translation():
    c = CSV(
        in_filename="DeepL_news_dataset2.csv",
        out_filename="Everyone_news_output_dataset2.csv"
    )

    # get input data from csv
    res, err = c.scan()
    if err is not None:
        print(err)

    # run translation
    translation = Translation()
    bucket = []
    for i, item in enumerate(res):
        r = translation.do(item)
        j = r.json()
        print('j:', j)
        status = j['resultset']['code']
        if status == 0:
            text = j['resultset']['result']['information']['text-t']
        else:
            text = 'Error'
        bucket.append([text])


    print('bucket:', bucket)

    # export translated data into new csv file
    err = c.print(bucket)
    if err is not None:
        print(err)
    else:
        print('success')

def single_translation(idx):
    # preparation
    c = CSV(
        in_filename="DeepL_news_dataset3.csv"
    )
    res, err = c.scan()
    if err is not None:
        print(err)
    text = res[idx]
    print('text:', text)
    translation = Translation()
    
    # execution
    r = translation.do(text)
    t = translation.extract_text(r.json())
    print(t)


if __name__ == "__main__":
    single_translation(0)
