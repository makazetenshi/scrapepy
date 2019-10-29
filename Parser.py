from bs4 import BeautifulSoup


class Parser:
    @staticmethod
    def find_elements_by_tag(content, tag):
        if tag == '':
            return 'No tag specified.'
        soup = BeautifulSoup(content, 'html.parser')
        return soup.find_all(tag)

    @staticmethod
    def find_all_image_urls(content):
        soup = BeautifulSoup(content, 'html.parser')
        urls = []
        for image in soup.find_all('img'):
            urls.append(image.get('src'))
        return urls

    def find_all_link_urls(content):
        soup = BeautifulSoup(content, 'html.parser')
        urls = []
        for link in soup.find_all('a'):
            urls.append(link.get('src'))
        return urls
