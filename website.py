import pandas as pd

class WebsiteInformation:

    def __init__(self, website_name, html, tag, identifying_class, heading_tag, secondary_tag, link_tag):
        self.website_name = website_name
        self.html = html
        self.tag = tag
        self.identifying_class = identifying_class
        self.heading_tag = heading_tag
        self.secondary_tag = secondary_tag
        self.link_tag = link_tag
        self.scraped_values = self.scraped_values(self.tag, self.html, self.identifying_class)
        self.headings = self.headings(self.heading_tag)
        self.secondary_info = self.secondary_info(self.secondary_tag)
        self.links = self.links(self.link_tag)
    
    def scraped_values(self, tag, html, identifying_class):
        '''docstring'''
        website_content = html.find_all(tag, class_= identifying_class)
        return website_content
    
    def headings(self):
        '''docstring'''
        headings = []
        website_content = self.scraped_values
        for each in website_content:
            heading_text = each.find(self.heading_tag).get_text()
            heading_text = heading_text.replace('\n', '')
            heading_text = heading_text.strip(' ')
            headings.append(heading_text)
        return headings
    
    def secondary_info(self):
        '''docstring'''
        secondary = []
        website_content = self.scraped_values
        for each in website_content:
            try:
                secondary_text = each.find(self.secondary_tag).get_text()
            except:
                secondary_text = 'No supporting text supplied, access the link for more info'
            secondary_text = secondary_text.replace('\n', '')
            secondary_text = secondary_text.replace('"', '')
            secondary_text = secondary_text.strip(' ')
            secondary.append(secondary_text)
        return secondary

    def links(self):
        '''docstring'''
        links = []
        website_content = self.scraped_values
        for each in website_content:
            link = each.find_next(self.link_tag).get('href')
            link = link.replace('\n', '')
            link = link.strip(' ')
            if 'https' not in link:
                link = self.website_name + link[1:]
            links.append(link)
        return links
    
    def news_dataframe(self):
        '''docstring'''
