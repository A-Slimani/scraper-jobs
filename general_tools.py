from selenium import webdriver
from typing import List
import csv

def create_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless=new')
    driver = webdriver.Chrome(options=options)
    return driver

def write_to_csv(job_list, file_name: str):
    with open(file_name, 'w', encoding='utf-8', newline='') as f:
        dict_writer = csv.DictWriter(f, job_list[0].keys())
        dict_writer.writeheader()
        dict_writer.writerows(job_list)

