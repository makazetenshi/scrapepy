import sys
from Fetcher import Fetcher
from Parser import Parser
from datetime import datetime


class Scraper(object):
    @staticmethod
    def find_all_with_tag(content, tag, write):
        if write:
            date_obj = datetime.now()
            timestamp = str(date_obj.timestamp())
            results = Parser.find_elements_by_tag(content, tag)
            file = open(timestamp + 'txt', 'w+')
            for result in results:
                file.write(result+"\r\n")
        else:
            print(Parser.find_elements_by_tag(content, tag))

    @staticmethod
    def find_all_image_urls(content, write):
        if write:
            date_obj = datetime.now()
            timestamp = str(date_obj.timestamp())
            results = Parser.find_all_image_urls(content)
            file = open(timestamp + 'txt', 'w+')
            for result in results:
                file.write(result+"\r\n")
        else:
            print(Parser.find_all_image_urls(content))

    @staticmethod
    def find_all_link_urls(content, write):
        if write:
            date_obj = datetime.now()
            timestamp = str(date_obj.timestamp())
            results = Parser.find_all_link_urls(content)
            file = open(timestamp + '.txt', 'w+')
            for result in results:
                file.write(result+"\r\n")
        else:
            print(Parser.find_all_link_urls(content))

    def main(self):
        args = sys.argv
        if len(args) < 2:
            print('Please add arguments to proceed.')
        else:
            target = args[1]
            mode = args[2]
            mode = mode.replace('-', '')
            if mode != 'help' and mode != 'h':
                if len(args) < 4:
                    tags = ''
                else:
                    tags = args[3]

                if 'w' in args:
                    write = True
                else:
                    write = False

                fetcher = Fetcher
                page = fetcher.get_page(target)
                content = page.content
                if mode == 't':
                    self.find_all_with_tag(content, tags, write)
                elif mode == 'i':
                    self.find_all_image_urls(content, write)
                elif mode == 'a':
                    self.find_all_link_urls(content, write)


if __name__ == '__main__':
    scraper = Scraper()
    scraper.main()
