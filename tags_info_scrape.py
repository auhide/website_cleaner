
import re
import csv
import numpy as np

import requests
from bs4 import BeautifulSoup


CSV_PATH = 'data/tags_percent.csv'


def download_data(url):
    resp = requests.get(url)

    src = resp.text

    soup = BeautifulSoup(src, 'lxml')

    overview = soup.find('section')

    overview = str(overview)

    re_tag_percent = r'<div class="bar__label">&lt;([^&]+)&gt;<\/div>\s*<\/div>\s*<div class="col-md-8">\s*<div class="bar__value" style="width: [^;]+;">\s*<div class="bar__pct">\s*([^%]+)%\s*<\/div>'

    match = re.findall(re_tag_percent, overview)

    return match



def write_data(data):
    with open('tags_percent.csv', mode='w') as f:
        writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        writer.writerow(["Tag", "Percent"])

        for tag_perc in data:
            writer.writerow([tag_perc[0], tag_perc[1]])



# data = download_data('https://www.advancedwebranking.com/html/')
# write_data(data)

# Reading the CSV File

import pandas as pd

df = pd.read_csv(CSV_PATH)


df = df[df['Percent'] > 50.0].sort_values(by=["Percent"], ascending=False)

np.asarray(df)

df = np.transpose(df["Tag"])
print(list(df))