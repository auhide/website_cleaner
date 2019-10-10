import os
import sys
import re

import requests
import difflib
import math

from bs4 import BeautifulSoup
import pandas as pd
import numpy as np




PARSER = 'lxml'
CSV_PATH = 'data/tags_percent.csv'



class Cleaner:


    def __init__(self, url):
        self.url = url

        # Getting the HTML source
        resp = requests.get(self.url)
        self.src = resp.text

        # Creating the BeautifulSoup Object
        self.soup = BeautifulSoup(self.src, PARSER)

        self.__get_tags()
        print("TAGS:", self.tags)

        self.__csv_tags_stats()
        print("CSV_TAGS:", self.csv_tags)

        self.__common_tags()

        print(self.common_tags)
        


    def __get_tags(self):
        '''
        TODO: Add function description
        '''

        self.tags = []

        for tag in self.soup.find_all():
            if tag.name != 'body' and tag.name != 'html' and tag.name != 'head':
                self.tags.append(tag.name)

        # Filtering only unique tags
        self.tags = list(set(self.tags))



    def __get_tag_string(self):
        '''
        TODO: Add function description
        '''

        pass



    def __csv_tags_stats(self):
        '''
        TODO: Add function description
        '''

        # Filtering the tags by percentage
        # Ordering the tags from the CSV file in descending order
        df = pd.read_csv(CSV_PATH)
        df = df[df["Percent"] > 50.0].sort_values(by=["Percent"], ascending=False)

        # Making a list out of all remaining tags
        np.asarray(df)
        df = np.transpose(df["Tag"])
        
        self.csv_tags = list(df)



    def __clean_empty_tags(self):
        
        for tag in self.soup.find_all():
            curr_content = str(tag.get_text())            

            print("CONTENT:", curr_content, len(curr_content))

            if re.search(r"^\s*$", curr_content):
                try:
                    print(tag)
                except (AttributeError):
                    print("FAIL LOL LMAO")
                tag.decompose()




    def __common_tags(self):
        
        self.common_tags = []

        for tag in self.tags:

            if tag in self.csv_tags:
                self.common_tags.append(tag)


    def save_source(self, filename="source", ext="html"):

        with open(f"{filename}.{ext}", 'w', encoding="utf-8") as f:
            soup_str = str(self.soup)
            f.write(soup_str)



    def clean(self):
        '''
        TODO: Add function description
        '''

        for tag in self.tags:

            if tag not in self.common_tags:
                print(f"{tag} removed!")
                
                for curr_tag in self.soup.find_all(tag):
                    curr_tag.decompose()


        self.__clean_empty_tags()

        return self

    

    def minify(self):
        '''
        TODO: Add function description
        '''
        pass




    def clean_additional(self, tags):
        '''
        TODO: Add function description
        '''


        for tag in tags:

            for curr_tag in self.soup.find_all(tag):
                curr_tag.decompose()


        return self









class Differentiator:

    
    def compare(self, ):
        pass



if __name__ == "__main__":

    cleaner = Cleaner("https://www.dnes.bg/sofia/2019/10/10/lek-trus-na-50-km-ot-sofiia-sled-polunosht.425648")

    cleaner.clean().clean_additional(["a"])

    cleaner.save_source()
    