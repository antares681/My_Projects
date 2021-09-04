def page_nmbr(page_counter):
    if page_counter < 10:
        return ('*'* 96 + '\n' + '*' * 37 + ' PAGE  ' + str(page_counter) + ' ' + '*' * 50 + '\n' + '*' * 96)
    else:
        return ('*'* 96 + '\n' + '*' * 37 + ' PAGE ' + str(page_counter) + ' ' + '*' * 50 + '\n' + '*' * 96)

def relevant_sublink(link):
    if 'https' in link or 'http' in link:       #Identifies type of the link (internal/external) and returns it properly
        return (f'{topic_counter}. {item.text}\n  {len(str(topic_counter)) * " "}{str(link)}')
    else:
        return (f'{topic_counter}. {item.text}\n  {len(str(topic_counter)) * " "}{basic_url}{str(link)}')


from bs4 import BeautifulSoup
import requests
import time

#SETTING GLOBAL VARIABLES
page_counter = 0
topic_counter = 0
target_url = basic_url = 'https://news.ycombinator.com/'

#TAKE PARSING TOPIC INPUT (BY DEFAULT PARSES ALL TOPICS)
current_topic = input('Enter specific topic for parsing or press Enter: ') or ''

#PARSES THE PAGES UNTIL NONE AVAILABE
while True:
    page_counter += 1
    request = requests.get(target_url)                      #get tge target url
    soup = BeautifulSoup(request.text,'html.parser')        #turn requests.ResoponseObject into human readable code
    time.sleep(1.5)                                         #inserts delay between executioni requests and l
    topics = soup.find_all('td', class_='title')            #identify all topics of class 'title'

    #IDENTIFYING AND PRINTING SUITABLE TOPICS & RELEVANT URLs
    print(page_nmbr(page_counter))
    for item in topics:                                     #Iterates through the topics and selects those with class 'storylink'
        topic_counter += 1
        item = item.find('a', {'class':'storylink'})
        if item is not None and current_topic in str(item): #Filters None and optionally only specific topics //to search current_topic in it item shall be set to str!!!
            print(relevant_sublink(item.get('href')))       #Gets the link to the relevant story
            print('=' * 96)                                 #Prints the found topics divider '==== ... '


    #CHECKS IF THERE IS NEXT PAGE IF NOT EXITS THE PROGRAM
    next_page = soup.find("a", {'class' : "morelink"})      #trys to move to next page in not succesful exits
    try:
        next_page_sublink = next_page.get('href')
        target_url = basic_url + next_page_sublink
    except AttributeError:
        print('Parsing completed')
        break
