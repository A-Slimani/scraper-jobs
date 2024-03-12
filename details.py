from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def get_details(driver, card):

    job = {}

    try:
        card_details = driver.find_element(By.CLASS_NAME, 'SearchOpportunityContentstyle__OpportunityDetailsWrapper-sc-k2tet-30.caEsCG')
    except NoSuchElementException as e:
        print("No card detail element")
        card_details = None

    try:
        job['role'] = driver.find_element(
            By.CLASS_NAME, 
            'sc-eCssSg.kgSmcY.heading.SearchOpportunityContentstyle__OpportunityTitle-sc-k2tet-12.htCSOp'
            ).text.replace(',', ' ')
    except NoSuchElementException as e:
        print('No role element')
        job['role'] = 'N/A'
    
    try:
        job['company'] = driver.find_element(
            By.CLASS_NAME, 
            'SearchOpportunityContentstyle__StyledLink-sc-k2tet-15.iSykQe'
            ).text.replace(',', ' ')
    except NoSuchElementException as e:
        print('No company element')
        job['company'] = 'N/A'
    
    try:
        job['location'] = driver.find_elements(
            By.CLASS_NAME, 
            'SearchOpportunityContentstyle__OpportunityLabel-sc-k2tet-20.bprSzs'
            )[1].text.replace(',', ' ')
    except (NoSuchElementException, IndexError) as e:
        print('No location element')
        job['location'] = 'N/A'

    try:
        salary = driver.find_element(
            By.CLASS_NAME, 
            'SearchOpportunityContentstyle__SalaryDetail-sc-k2tet-40.ejxyuQ'
            ).text
        salary = salary.split(' ')[1: -2] 
        for i in range(len(salary)):
            salary[i] = salary[i].replace(',', '')
        job['salary'] = ' '.join(salary)
    except NoSuchElementException as e:
        job['salary'] = 'N/A'

    try:
        if card_details is None:
            raise NoSuchElementException
        detail_list = card_details.find_elements(By.CLASS_NAME, 'sc-cbDGPM.eTEuVf.field-item')
        detail_titles = card_details.find_elements(By.CLASS_NAME, 'sc-jNMdTA.fzbNbD.sc-httYMd.eunqYU')

        for i in range(len(detail_titles)):
            # details.append({detail_titles[i].text : detail_list[i].text})
            job[detail_titles[i].text] = detail_list[i].text

        # start_date = detail_list[0].text
        # open_date = detail_list[1].text
        # close_date = detail_list[2].text
        # vacancies = detail_list[3].text
    except (NoSuchElementException, IndexError) as e:
        print('No details element')


    try:
        card.click()
    except NoSuchElementException as e:
        print('end??')

    return job