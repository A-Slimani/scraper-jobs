from general_tools import create_driver

def grad_connect_job_list():
    driver = create_driver()

    driver.get("https://au.gradconnection.com/graduate-jobs/computer-science/?ordering=earliest_closing_date")
    job_list = []


    driver.quit()
