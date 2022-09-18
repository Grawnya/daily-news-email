import pandas as pd

class WebsiteInformation:

    def __init__(self, website_name, html, type_of_news, tag, identifying_class, heading_tag, secondary_tag, link_tag):
        self.website_name = website_name
        self.html = html
        self.tag = tag
        self.identifying_class = identifying_class
        self.heading_tag = heading_tag
        self.secondary_tag = secondary_tag
        self.link_tag = link_tag
        self.type_of_news = type_of_news
    
    def tags_based_on_news_type(self):
        '''docstring'''
        if self.type_of_news == 'general':
            return

    def scraped_values(self):
        '''docstring'''
        website_content = self.html.find_all(self.tag, class_= self.identifying_class)
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
            heading_text = each.find(self.heading_tag).get_text()
            heading_text = self.clean_title_values(heading_text)
            headings.append(heading_text)
        return headings
    
    def secondary_info(self):
        '''docstring'''
        secondary = []
        for each in self.scraped_values():
            try:
                secondary_text = each.find(self.secondary_tag).get_text()
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
                link = self.website_name + link[1:]
            links.append(link)
        return links
    
    def news_dataframe(self):
        '''docstring'''
        df = pd.DataFrame({'Headings':self.headings(),'Secondary Info':self.secondary_info(), 'Links':self.links()})
        return df

class BBC(WebsiteInformation):
    def __init__(self, website_name, html, type_of_news):
        super().__init__(website_name, html, type_of_news, tag='div', identifying_class='media__content', heading_tag='h3', secondary_tag='p', link_tag='a')

    def tags_based_on_news_type(self):
        '''docstring'''
        if self.type_of_news == 'general':
            return
        elif self.type_of_news == 'sport':
            self.tag = 'a'
            self.identifying_class = 'e1f5wbog0'
            self.heading_tag = 'span'