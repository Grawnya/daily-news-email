import pandas as pd
import re

class WebsiteInformation:

    def __init__(self, website_name, html, tag, identifying_class, heading_attribute, secondary_tag, link_tag):
        self.website_name = website_name
        self.html = html
        self.tag = tag
        self.identifying_class = identifying_class
        self.heading_attribute = heading_attribute
        self.secondary_tag = secondary_tag
        self.link_tag = link_tag

    def scraped_values(self):
        '''docstring'''
        website_content = self.html.find_all(self.tag, attrs=self.identifying_class)
        return website_content
    
    def clean_title_values(self, value_text):
        value_text_cleaned = value_text.replace('\n', '')
        value_text_cleaned = value_text_cleaned.replace('"', '')
        value_text_cleaned = value_text_cleaned.strip(' ')
        return value_text_cleaned

    def headings(self):
        '''docstring'''
        headings = []
        for each in self.scraped_values():
            heading_text = each.find(**self.heading_attribute).get_text()
            heading_text = self.clean_title_values(heading_text)
            headings.append(heading_text)
        return headings
    
    def secondary_info(self):
        '''docstring'''
        secondary = []
        for each in self.scraped_values():
            try:
                secondary_text = each.find(**self.secondary_tag).get_text()
            except:
                secondary_text = 'No supporting text supplied, access the link for more info'
            secondary_text = self.clean_title_values(secondary_text)
            secondary.append(secondary_text)
        return secondary

    def links(self):
        '''docstring'''
        links = []
        for each in self.scraped_values():
            link = each.find_next(self.link_tag).get('href')
            link = self.clean_title_values(link)
            if 'https' not in link:
                # alter website so it uses correct link 
                link = self.website_name[:-5] + link[1:]
            links.append(link)
        return links
    
    def news_dataframe(self):
        '''docstring'''
        df = pd.DataFrame({'Headings':self.headings(),'Secondary Info':self.secondary_info(), 'Links':self.links()})
        return df

class BBC(WebsiteInformation):
    '''docstring'''
    def __init__(self, website_name, html):
        super().__init__(website_name, html, tag='div', identifying_class={'class':'media__content'}, heading_attribute={'name':'h3'}, secondary_tag={'name':'p'}, link_tag='a')

class BBCSport(WebsiteInformation):
    '''docstring'''
    def __init__(self, website_name, html):
        super().__init__(website_name, html, tag='div', identifying_class={'spacing':'2'}, heading_attribute={"role":'text'}, secondary_tag={'class':'ssrcss-1q0x1qg-Paragraph eq5iqo00'}, link_tag='a')