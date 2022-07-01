import argparse
import os
import time

import requests
from tqdm import tqdm


def scrape(args: argparse.Namespace):
    count = 2500
    url = 'https://vaxxeddoggos.com/assets/doggos/'
    if not os.path.exists(args.savedir):
        os.makedirs(args.savedir)
    for i in tqdm(range(count)):
        fn = f'{args.savedir}/{i}.png'
        if os.path.exists(fn):
            continue
        resp = requests.get(f'{url}/{i}.png')
        with open(fn, 'wb') as f:
            f.write(resp.content)
        time.sleep(2)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Vaxxed Doggos Scraper')
    parser.add_argument('--savedir', type=str,
                        default='data/', help='save directory')
    args = parser.parse_args()
    scrape(args)
