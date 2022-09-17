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
    
    def headings(self, heading_tag):
        '''docstring'''
        headings = []
        website_content = self.scraped_values
        for each in website_content:
            heading_text = each.find(heading_tag).get_text()
            heading_text = heading_text.replace('\n', '')
            heading_text = heading_text.strip(' ')
            headings.append(heading_text)
        return headings
    
    def secondary_info(self, secondary_tag):
        '''docstring'''
        secondary = []
        website_content = self.scraped_values
        for each in website_content:
            try:
                secondary_text = each.find(secondary_tag).get_text()
            except:
                secondary_text = 'No supporting text supplied, access the link for more info'
            secondary_text = secondary_text.replace('\n', '')
            secondary_text = secondary_text.replace('"', '')
            secondary_text = secondary_text.strip(' ')
            secondary.append(secondary_text)
        return secondary

    def links(self, link_tag):
        '''docstring'''
        links = []
        website_content = self.scraped_values
        for each in website_content:
            link = each.find_next(link_tag).get('href')
            link = link.replace('\n', '')
            link = link.strip(' ')
            if 'https' not in link:
                link = self.website_name + link[1:]
            links.append(link)
        return links