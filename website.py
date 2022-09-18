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
    
    def scraped_values(self):
        '''docstring'''
        website_content = self.html.find_all(self.tag, class_= self.identifying_class)
        return website_content
    
    def clean_title_values(self, value_text):
        '''docstring'''
        value_text_cleaned = value_text.replace('\n', '')
        value_text_cleaned = value_text_cleaned.replace('"', '')
        value_text_cleaned = value_text_cleaned.strip(' ')
        return value_text_cleaned

    def title_values(self, value_location):
        '''docstring'''
        values = []
        website_content = self.scraped_values()
        for each in website_content:
            value_text = self.clean_title_values(value_location)
            values.append(value_text)
        return values

    def headings(self, each_heading):
        '''docstring'''
        return self.title_values(each_heading.find(self.heading_tag).get_text())
    
    def secondary_info(self):
        '''docstring'''
        secondary = []
        website_content = self.scraped_values()
        for each in website_content:
            try:
                secondary_text = each.find(self.secondary_tag).get_text()
            except:
                secondary_text = 'No supporting text supplied, access the link for more info'
            secondary_text= self.clean_title_values(secondary_text)
            secondary.append(secondary_text)
        return secondary

    def links(self):
        '''docstring'''
        links = []
        website_content = self.scraped_values()
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
        df = pd.DataFrame({'Headings':self.headings(),'Secondary Info':self.secondary_info(), 'Links':self.links()})
        return df

class BBC(WebsiteInformation):
    def __init__(self, website_name, html):
        super().__init__(website_name, html, tag='div', identifying_class='media__content', heading_tag='h3', secondary_tag='p', link_tag='a')