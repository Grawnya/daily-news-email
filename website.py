class WebsiteInformation:

    def __init__(self, website_name, html, tag, identifying_class):
        self.website_name = website_name
        self.html = html
        self.tag = tag
        self.identifying_class = identifying_class
        self.scraped_values = self.scraped_values(self.tag, self.html, self.identifying_class)
    
    def scraped_values(self, tag, html, identifying_class):
        '''docstring'''
        website_content = html.find_all(tag, class_= identifying_class)
        return website_content
    
    def headings(self, tag, heading_title):
        '''docstring'''
        headings = []
        website_content = self.scraped_values
        for each in website_content:
            heading_text = each.find(heading_title).get_text()
            heading_text = heading_text.replace('\n', '')
            heading_text = heading_text.strip(' ')
            headings.append(heading_text)
        return headings