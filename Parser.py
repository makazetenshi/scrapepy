from bs4 import BeautifulSoup


class Parser:
    @staticmethod
    def find_elements_by_tag(content, tag, limit):
        if tag == '':
            return 'No tag specified.'
        soup = BeautifulSoup(content, 'html.parser')
        return soup.find_all(tag, limit=limit)

    @staticmethod
    def find_all_image_urls(content, limit):
        soup = BeautifulSoup(content, 'html.parser')
        urls = []
        for image in soup.find_all('img', limit=limit):
            urls.append(image.get('src'))
        return urls

    @staticmethod
    def find_all_link_urls(content, limit):
        soup = BeautifulSoup(content, 'html.parser')
        urls = []
        for link in soup.find_all('a', limit=limit):
            urls.append(link.get('src'))
        return urls

    @staticmethod
    def find_all_with_class(content, class_name, limit):
        soup = BeautifulSoup(content, 'html.parser')
        result = soup.find_all(attrs={"class": class_name}, limit=limit)
        return result
