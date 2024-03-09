from selenium import webdriver 
from selenium.webdriver.common.by import By
from details import get_details
from math import ceil


def create_driver():
    remote_url = 'http://10.0.0.146:4444/wd/hub'
    local_url = 'http://localhost:4444/wd/hub'
    options = webdriver.ChromeOptions()
    options.add_argument('--headless=new')
    # driver = webdriver.Chrome(options=options)
    driver = webdriver.Remote(command_executor=local_url, options=options)
    return driver


def main():
    driver = create_driver()

    driver.get("https://au.prosple.com/search-jobs?study_fields=502&locations=9692&defaults_applied=1&sort=popularity%7Cdesc&start=0&keywords=Graduate&opportunity_types=1")
    total_job_count = driver.find_element(By.CLASS_NAME, 'SearchResultCount__ResultsCount-sc-17kyq0v-0.bEIzsi').text.split(' ')[2]
    # pages = ceil(int(total_job_count) / 20)
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

    #with open('jobs.csv', 'w') as f:
    #    f.write(','.join(job_list[0].keys()) + '\n')
    #    for job in job_list:
    #        f.write(','.join([job['company'], job['role'], job['location'], job['start_date'], job['open_date'], job['close_date'], job['vacancies'], job['salary']]) + '\n')

    for job in job_list:
        print(job)

if __name__ == '__main__':
    main()