from openpyxl import Workbook
import pandas as pd
import json


api_url="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/module%201/Accessing%20Data%20Using%20APIs/jobs.json"

def get_number_of_jobs_T(technology):
    number_of_jobs = 0
    response = requests.get(api_url)
    if response.ok:
        data = response.json()
    for job in data:
        skills = job.get('Key Skills', '')
        if technology in skills:
            number_of_jobs += 1
    return technology, number_of_jobs

 def get_number_of_jobs_L(location):
    number_of_jobs = 0
    response = requests.get(api_url)
    if response.ok:
        data = response.json()
    for job in data:
        locations = job.get('Location', '')
        if location in locations:
            number_of_jobs += 1
    return location,number_of_jobs

location_list = ['Los Angeles', 'New York', 'San Francisco','Washington DC' ,'Seattle' ,'Austin', 'Detroit']
job_posting = []

for loc in location_list:
    job_posting.append(get_number_of_jobs_L(loc))

wb = Workbook()
ws = wb.active
ws.append(['Location', 'Number of Job Postings'])
for job in job_posting:
    ws.append(job)
wb.save('job-posting.xlsx')

technology_list = ['C', 'C#', 'C++','Java' ,'JavaScript' ,'Python', 'Scala', 'Oracle', 'SQL Server', 'MySQL Server', 'PostgreSQL', 'MongoDB']
job_posting = []

for tech in technology_list:
    job_posting.append(get_number_of_jobs_T(tech))
    
wb2 = Workbook()
ws2 = wb2.active
ws.append(['Technology', 'Number of Job Postings'])
for job in job_posting:
    ws2.append(job)
wb2.save('job-posting-technology.xlsx')
