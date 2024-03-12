from selenium import webdriver 
from selenium.webdriver.common.by import By
from details import get_details
from math import ceil
import csv


def create_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless=new')
    driver = webdriver.Chrome(options=options)
    return driver


def main():
    driver = create_driver()

    driver.get("https://au.prosple.com/search-jobs?study_fields=502&locations=9692&defaults_applied=1&sort=popularity%7Cdesc&start=0&keywords=Graduate&opportunity_types=1")
    total_job_count = driver.find_element(By.CLASS_NAME, 'SearchResultCount__ResultsCount-sc-17kyq0v-0.bEIzsi').text.split(' ')[2]
    pages = int(total_job_count)
    current = 0

    job_list = []

    while current <= pages:
        print("current: ", current)
        driver.get(f"https://au.prosple.com/search-jobs?study_fields=502&locations=9692&defaults_applied=1&sort=popularity%7Cdesc&start={current}&keywords=Graduate&opportunity_types=1")

        job_cards = driver.find_elements(By.CLASS_NAME, 'sc-jifIRw.lhxhuD')

        for card in job_cards:
            job_list.append(get_details(driver, card))

        current += 20

    driver.quit()

    with open('jobs.csv', 'w', encoding='utf-8') as f:
        dict_writer = csv.DictWriter(f, job_list[0].keys())
        dict_writer.writeheader()
        dict_writer.writerows(job_list)


if __name__ == '__main__':
    main()