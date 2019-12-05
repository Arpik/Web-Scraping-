# Get all software jobs from boston.craigslist.org in csv format.

from bs4 import BeautifulSoup
import requests
import pandas as pd 

url = "https://boston.craigslist.org/search/sof"

# Create a dictionary
npo_jobs = {}

job_no = 0

while True:

    response = requests.get(url)
    data = response.text
    soup = BeautifulSoup(data, 'html.parser')
    
    jobs = soup.find_all('p',{'class' : 'result-info'})
    for job in jobs:
        title = job.find('a', {'class' : 'result-title'}).text
        location_tag = job.find('span', {'class': 'result-hood'})
        
        # If a location tag is found extract the text otherwise just add the text N/A
        location = location_tag.text[2:-1] if location_tag else 'N/A' 
        
        # Extract the time tag
        date = job.find('time', {'class' : 'result-date'}).text

        # Extract job link
        link = job.find('a', {'class' : 'result-title'}).get('href')

        # Parse each job description tag
        job_response = requests.get(link)
        job_data = job_response.text
        job_soup = BeautifulSoup(job_data, 'html.parser')

        # Extract job description
        job_description = job_soup.find('section', {'id': 'postingbody'}).text
        
        job_attributes_tag = job_soup.find('p',{'class':'attrgroup'})
        job_attributes = job_attributes_tag.text if job_attributes_tag else "N/A"
        
        job_no += 1 
        npo_jobs[job_no] = [title, location, date, link, job_attributes, job_description]

        print('Job Title:' , title, '\nLocation', location, '\nDate', date, '\nLink', link, '\n---')
    
    # Get jobs from all pages.
    url_tag = soup.find('a', {'title' : 'next page'})
    if url_tag.get('href'):
        url = 'https://boston.craigslist.org' + url_tag.get('href')
        print(url)
    else:
        break

print("Total Jobs:", job_no)

# Convert the npo_job dictionary into a pandas Data Frame.
npo_jobs_df = pd.DataFrame.from_dict(npo_jobs, orient = 'index', columns = ['Job Title', 'Location', 'Date', 'Link', 'Job Attributes', 'Job Description'])

# Write data into csv file. 
npo_jobs_df.to_csv('npo_jobs.csv')