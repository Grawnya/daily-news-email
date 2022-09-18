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
    
    def headings(self):
        '''docstring'''
        headings = []
        website_content = self.scraped_values()
        for each in website_content:
            heading_text = each.find(self.heading_tag).get_text()
            heading_text = heading_text.replace('\n', '')
            heading_text = heading_text.strip(' ')
            headings.append(heading_text)
        return headings
    
    def secondary_info(self):
        '''docstring'''
        secondary = []
        website_content = self.scraped_values()
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
        print(df)
        return df

class BBC(WebsiteInformation):
    def __init__(self, website_name, html):
        super().__init__(website_name, html, tag='div', identifying_class='media__content', heading_tag='h3', secondary_tag='p', link_tag='a')