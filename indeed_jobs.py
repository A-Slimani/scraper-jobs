from selenium.webdriver.common.by import By
from general_tools import create_driver, write_to_csv, write_to_db, connect_to_db

def indeed_job_list():
    driver = create_driver(False)

    # db_connection = connect_to_db()

    driver.get(f"https://au.indeed.com/jobs?q=data+engineer&l=Sydney+NSW&from=searchOnHP&vjk=ab43ce3ed3718539")

    job_cards = driver.find_elements(By.CLASS_NAME, 'css-5lfssm.eu4oa1w0')

    job_list = []

    for job in job_cards:
        details = {}
        details['title'] = job.find_element(By.CLASS_NAME, 'jcs-JobTitle.css-jspxzf.eu4oa1w0').text
        details['company'] = job.find_element(By.CLASS_NAME, 'css-92r8pb.eu4oa1w0').text
        details['location'] = job.find_element(By.CLASS_NAME, 'css-92r8pb.eu4oa1w0').text
        details['url'] = job.find_element(By.CLASS_NAME, 'jcs-JobTitle.css-jspxzf.eu4oa1w0').get_attribute('href')
        job_list.append(details)
      
    write_to_csv(job_list, 'indeed.csv')  

    driver.quit()

    # write_to_csv(job_list, 'seek.csv')