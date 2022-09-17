class WebsiteInformation:

    def __init__(self, website_name, html):
        self.website_name = website_name
        self.html = html
    
    def scraped_values(self, tag, html, identifying_class):
        '''docstring'''
        website_content = html.find_all(tag, class_= identifying_class)
        return website_content
    
    def headings(self):
        '''docstring'''