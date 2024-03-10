from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def get_details(driver, card):
    try:
        card_details = driver.find_element(By.CLASS_NAME, 'SearchOpportunityContentstyle__OpportunityDetailsWrapper-sc-k2tet-30.caEsCG')
    except NoSuchElementException as e:
        print("No card detail element")
        card_details = None

    try:
        role = driver.find_element(
            By.CLASS_NAME, 
            'sc-eCssSg.kgSmcY.heading.SearchOpportunityContentstyle__OpportunityTitle-sc-k2tet-12.htCSOp'
            ).text.replace(',', ' ')
    except NoSuchElementException as e:
        print('No role element')
        role = 'N/A'
    
    try:
        company = driver.find_element(
            By.CLASS_NAME, 
            'SearchOpportunityContentstyle__StyledLink-sc-k2tet-15.iSykQe'
            ).text.replace(',', ' ')
    except NoSuchElementException as e:
        print('No company element')
        company = 'N/A'
    
    try:
        location = driver.find_element(
            By.CLASS_NAME, 
            'SearchOpportunityContentstyle__OpportunityLabel-sc-k2tet-20.bprSzs'
            ).text.replace(',', ' ')
    except NoSuchElementException as e:
        print('No location element')
        location = 'N/A'

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
        print('No salary element')
        salary = 'N/A'

    try:
        if card_details is None:
            raise NoSuchElementException
        detail_list = card_details.find_elements(By.CLASS_NAME, 'sc-cbDGPM.eTEuVf.field-item')
        # this is not good if one of them is missing
        # get a better solution for this
        start_date = detail_list[0].text
        open_date = detail_list[1].text
        close_date = detail_list[2].text
        vacancies = detail_list[3].text
    except (NoSuchElementException, IndexError) as e:
        start_date = 'N/A'
        open_date = 'N/A'
        close_date = 'N/A'
        vacancies = 'N/A'

    try:
        card.click()
    except NoSuchElementException as e:
        print('end??')

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
