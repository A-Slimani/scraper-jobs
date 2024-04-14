from selenium import webdriver
from dotenv import load_dotenv
import psycopg2
import csv
import os

load_dotenv()

def create_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless=new')
    driver = webdriver.Chrome(options=options)
    return driver

def write_to_csv(job, file_name: str):
    with open(file_name, 'a', encoding='utf-8', newline='') as f:
        dict_writer = csv.DictWriter(f, job.keys())
        if os.path.exists(file_name) and os.stat(file_name).st_size == 0:
            dict_writer.writeheader()
        dict_writer.writerow(job)

def connect_to_db():
    connection = psycopg2.connect(
        host=os.environ.get('hostname'), 
        database=os.environ.get('database'), 
        user=os.environ.get('username'), 
        password=os.environ.get('password')
    )

    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS jobs (
            id SERIAL PRIMARY KEY,
            title TEXT,
            company TEXT,
            salary TEXT,
            location TEXT,
            link TEXT,
            close_date DATE,
            website TEXT,
            scraped_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        ''')
    
    return connection, cursor


def write_to_db(job, connection, cursor):
    cursor.execute("SELECT * FROM jobs WHERE title=%s AND company=%s", (job['title'], job['company'],))
    result = cursor.fetchone()

    if not result:
        try:
            cursor.execute("""
                INSERT INTO jobs (title, company, close_date, salary, location, link, website) 
                VALUES (%s, %s, 
                    CASE
                        WHEN %s ~ '^\d{2}/\d{2}/\d{4}$' THEN TO_DATE(%s, 'DD/MM/YYYY')
                        ELSE NULL
                    END,
                    %s, %s, %s, %s)
                """
                ,(
                    job['title'],
                    job['company'],
                    job['close_date'],
                    job['close_date'],
                    job['salary'],
                    job['location'],
                    job['link'],
                    job['website']
                ))
            connection.commit()
        except Exception as e:
            connection.rollback()
            print(e)
    

