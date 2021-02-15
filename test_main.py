from main import (
    CSV,
    Translation
)

import argparse
import math
import time
import datetime


def test_single_translation(idx):
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
    
    start = time.time()
    # execution START
    r = translation.do(text)
    t = translation.extract_text(r.json())
    print(t)
    # execution END
    end = time.time()
    # print('time:', round((end - start)*10**9, -1))
    ns_time = int((end - start)*10**9)
    print('time:', ns_time)
    return ns_time

def run_test(idx: int):
    iterations = 10
    results = [0]*10
    for i in range(iterations):
        results[i] = test_single_translation(idx)

    stats = int(sum(results) / len(results))
    print('result:', stats)
    

if __name__ == "__main__":
    # Configure command line option
    # parser = argparse.ArgumentParser()
    # parser.add_argument('-i', '--index', help='run test for the defined index')
    # args = parser.parse_args()

    # main 
    for i in range(2, 57):
        print('\n#:', i+1)
        run_test(i)
