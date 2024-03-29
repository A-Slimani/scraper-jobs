from general_tools import create_driver, write_to_csv, write_to_db, connect_to_db
from selenium.webdriver.common.by import By
import datetime as dt
import re

def calculate_closing_date(str):
    match = re.search(r'\d+', str)
    if match:
        return (dt.datetime.today() + dt.timedelta(days=int(match.group()))).strftime('%d/%m/%Y')
    else:
        return 'N/A'

def grad_connect_job_list():
    driver = create_driver()

    db_connection = connect_to_db()

    # job_list = []
    for p in range(1, 16):
        driver.get(f"https://au.gradconnection.com/graduate-jobs/computer-science/?page={p}")

        job_cards = driver.find_elements(By.CLASS_NAME, 'full-row')

        for job in job_cards:
            if job.find_element(By.CLASS_NAME, 'ellipsis-text-paragraph').text == 'Graduate Jobs':
                details = {}
                details['title'] = job.find_element(By.TAG_NAME, 'h3').text
                details['company'] = job.find_element(By.CLASS_NAME, 'box-header-para').text
                try:
                    close_date = job.find_element(By.CLASS_NAME, 'box-closing-interval').text
                except:
                    close_date = '' 
                details['close_date'] = calculate_closing_date(close_date)
                details['location'] = job.find_element(By.CLASS_NAME, 'ellipsis-text-paragraph.location-name').text
                details['link'] = job.find_element(By.CLASS_NAME, 'box-header-title').get_attribute('href')
                details['salary'] = None
                details['website'] = 'gradconnect'
                # job_list.append(details)
                write_to_db(details, db_connection[0], db_connection[1])

    driver.quit()

    # write_to_csv(job_list, 'gradconnect.csv')
