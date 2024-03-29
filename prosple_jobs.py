from selenium.webdriver.common.by import By
from general_tools import create_driver, write_to_csv, write_to_db, connect_to_db
from prosple_details import get_details
from math import ceil
import csv


def prosple_job_list():
    driver = create_driver()

    driver.get("https://au.prosple.com/search-jobs?study_fields=502&locations=9692&defaults_applied=1&sort=popularity%7Cdesc&start=0&keywords=Graduate&opportunity_types=1")
    total_job_count = driver.find_element(By.CLASS_NAME, 'SearchResultCount__ResultsCount-sc-17kyq0v-0.bEIzsi').text.split(' ')[2]
    pages = int(total_job_count)
    current = 0

    db_connection = connect_to_db()
    # job_list = []

    while current <= pages:
        print("current: ", current)
        driver.get(f"https://au.prosple.com/search-jobs?study_fields=502&locations=9692&defaults_applied=1&sort=popularity%7Cdesc&start={current}&keywords=Graduate&opportunity_types=1")

        job_cards = driver.find_elements(By.CLASS_NAME, 'sc-jifIRw.lhxhuD')

        for card in job_cards:
            job = get_details(driver, card)
            write_to_db(job, db_connection[0], db_connection[1])
            write_to_csv(job, 'prosple_jobs.csv')
            # job_list.append(get_details(driver, card))

        current += 20

    driver.quit()

    # write_to_csv(job_list, 'prosple_jobs.csv') 

