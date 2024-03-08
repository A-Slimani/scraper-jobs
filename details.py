from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def get_details(driver, card):
    try:
        card_details = driver.find_element(By.CLASS_NAME, 'SearchOpportunityContentstyle__OpportunityDetailsWrapper-sc-k2tet-30.caEsCG')
    except NoSuchElementException as e:
        print(e)

    try:
        role = driver.find_element(
            By.CLASS_NAME, 
            'sc-eCssSg.kgSmcY.heading.SearchOpportunityContentstyle__OpportunityTitle-sc-k2tet-12.htCSOp'
            ).text
    except NoSuchElementException as e:
        print(e)
        role = ' '
    
    try:
        company = driver.find_element(
            By.CLASS_NAME, 
            'SearchOpportunityContentstyle__StyledLink-sc-k2tet-15.iSykQe'
            ).text
    except NoSuchElementException as e:
        print(e)
        company = ' '
    
    try:
        location = driver.find_element(
            By.CLASS_NAME, 
            'SearchOpportunityContentstyle__OpportunityLabel-sc-k2tet-20.bprSzs'
            ).text
    except NoSuchElementException as e:
        print(e)
        location = ' '

    try:
        salary = driver.find_element(
            By.CLASS_NAME, 
            'SearchOpportunityContentstyle__SalaryDetail-sc-k2tet-40.ejxyuQ'
            ).text
        salary = salary.split(' ')[1: -2] 
        for i in range(len(salary)):
            salary[i] = salary[i].replace(',', '')
        salary = ' '.join(salary)
    except NoSuchElementException as e:
        print(e)
        salary = ' '

    try:
        detail_list = card_details.find_elements(By.CLASS_NAME, 'sc-cbDGPM.eTEuVf.field-item')
        start_date = detail_list[0].text
        open_date = detail_list[1].text
        close_date = detail_list[2].text
        vacancies = detail_list[3].text
    except NoSuchElementException as e:
        print(e)
        detail_list = []

    try:
        card.click()
    except NoSuchElementException as e:
        print('end??')
        return None 

    return {
        "company": company,
        "role": role,
        "location": location,
        "start_date": start_date,
        "open_date": open_date,
        "close_date": close_date,
        "vacancies": vacancies,
        "salary": salary
    }
