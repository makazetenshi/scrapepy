import sys
from Fetcher import Fetcher
from Parser import Parser


class Scraper(object):
    @staticmethod
    def find_all_with_tag(content, tag):
        print(Parser.find_elements_by_tag(content, tag))

    @staticmethod
    def find_all_image_urls(content):
        print(Parser.find_all_image_urls(content))

    @staticmethod
    def find_all_link_urls(content):
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

                fetcher = Fetcher
                page = fetcher.get_page(target)
                content = page.content
                if mode == 't':
                    self.find_all_with_tag(content, tags)
                elif mode == 'i':
                    self.find_all_image_urls(content)
                elif mode == 'a':
                    self.find_all_link_urls(content)


if __name__ == '__main__':
    scraper = Scraper()
    scraper.main()
