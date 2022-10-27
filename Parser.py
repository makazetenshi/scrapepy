from bs4 import BeautifulSoup


class Parser:
    @staticmethod
    def find_elements_by_tag(content, tag, limit, recursive):
        if tag == '':
            return 'No tag specified.'
        soup = BeautifulSoup(content, 'html.parser')
        return soup.find_all(tag, limit=limit, recursive=recursive)

    @staticmethod
    def find_all_image_urls(content, limit, recursive):
        soup = BeautifulSoup(content, 'html.parser')
        urls = []
        for image in soup.find_all('img', limit=limit, recursive=recursive):
            urls.append(image.get('src'))
        return urls

    @staticmethod
    def find_all_link_urls(content, limit, recursive):
        soup = BeautifulSoup(content, 'html.parser')
        urls = []
        for link in soup.find_all('a', limit=limit, recursive=recursive):
            urls.append(link.get('src'))
        return urls

    @staticmethod
    def find_all_with_class(content, class_name, limit, recursive):
        soup = BeautifulSoup(content, 'html.parser')
        result = soup.find_all(attrs={"class": class_name}, limit=limit, recursive=recursive)
        return result

    @staticmethod
    def find_all_with_attribute(content, attribute, limit, recursive):
        attributes      = attribute.split(':')
        attribute_name  = attributes[0]
        attribute_value = attributes[1]

        soup = BeautifulSoup(content, 'html.parser')
        result = soup.find_all(attrs={attribute_name: attribute_value}, limit=limit, recursive=recursive)
        return result
