import re
from bs4 import BeautifulSoup
import requests
class Searcher:
    def __init__(self):
        self.link_draft = re.compile('some-ref-link-here')
    def search_twitter(self, links_list):
        
        """ 
        Warning! You should pass links like mobile.twitter.com/name_of_account to the function for proper work
        Function that search new posts that meet criterias in twitter through web scraping and if something found call the function write_sqlite to add new records
         """
        for x in links_list:
            html = requests.get(x).text # TODO
            soup = BeautifulSoup(html, 'lxml')
            tweet_text_soup = soup('div', class_='dir-ltr') # soup with text of all tweets
            tweet_inf_soup = soup('td', class_='timestamp') # soup with date and link of all tweets
            dates = [x.a.string for x in               tweet_inf_soup]
            tweet_links = [x.a['href'] for x in tweet_inf_soup]
            for i in range(len(tweet_text_soup)):
                """   Trying to find ref links in every post. If list is empty - we don't have any links, that meeting our criteria in the post. If not - print all information about tweet """
                ref_links_list = re.findall(self.link_draft, str(tweet_text_soup[i]))
                if ref_links_list != []:
                    print(dates[i], tweet_links[i], ref_link_list[0])
               
