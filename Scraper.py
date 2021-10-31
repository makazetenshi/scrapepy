import sys
from Fetcher import Fetcher
from Parser import Parser
from datetime import datetime


class Scraper(object):
    @staticmethod
    def find_all_with_tag(content, tag, write, limit):
        if write:
            date_obj = datetime.now()
            timestamp = str(date_obj.timestamp())
            results = Parser.find_elements_by_tag(content, tag, limit)
            file = open(timestamp + 'txt', 'w+')
            for result in results:
                file.write(result+"\r\n")
        else:
            print(Parser.find_elements_by_tag(content, tag, limit))

    @staticmethod
    def find_all_image_urls(content, write, limit):
        if write:
            date_obj = datetime.now()
            timestamp = str(date_obj.timestamp())
            results = Parser.find_all_image_urls(content, limit)
            file = open(timestamp + 'txt', 'w+')
            for result in results:
                file.write(result+"\r\n")
        else:
            print(Parser.find_all_image_urls(content, limit))

    @staticmethod
    def find_all_link_urls(content, write, limit):
        if write:
            date_obj = datetime.now()
            timestamp = str(date_obj.timestamp())
            results = Parser.find_all_link_urls(content, limit)
            file = open(timestamp + '.txt', 'w+')
            for result in results:
                file.write(result+"\r\n")
        else:
            print(Parser.find_all_link_urls(content, limit))

    @staticmethod
    def find_all_with_class(content, class_name, write, limit):
        if write:
            date_obj = datetime.now()
            timestamp = str(date_obj.timestamp())
            results = Parser.find_all_with_class(content, class_name, limit)
            file = open(timestamp + '.txt', 'w+')
            for result in results:
                file.write(result+"\r\n")
        else:
            print(Parser.find_all_with_class(content, class_name, limit))


    @staticmethod
    def display_help_menu():
        help_string = 'usage: Scrape.py <mode> <target> [option] ... [arg] [l=<integer>] [w]'
        help_string = help_string + '\n Modes: '
        help_string = help_string + '-t : Find all with specified tag, requires the tag passed as arg\n'
        help_string = help_string + '-c : Find all with specified class, requires the class passed as arg\n'
        help_string = help_string + '-i : Find all image urls\n'
        help_string = help_string + '-a : Find all link urls\n'
        help_string = help_string + '-l=<integer> : Sets limit for results returned\n'
        help_string = help_string + '-h : Display help menu\n'
        help_string = help_string + '\n'
        help_string = help_string + 'Optional:\n'
        help_string = help_string + '[tag] : Needs to be specified for finding all of a certain tag type\n'
        help_string = help_string + '[w] : If this parameter is used, ' \
                                    'the result of the search will be outputted to a .txt file in file dir'
        print(help_string)

    def main(self):
        args = sys.argv
        if len(args) < 2:
            print('Please add arguments to proceed.')
        else:
            if len(args) > 2:
                target = args[2]
            else:
                target = ''
            mode = args[1]
            mode = mode.replace('-', '')
            if len(args) >= 4 and mode == 't':
                arguments = args[3]
            else:
                arguments = ''

            limit = 0

            if any('-l=' in s for s in args):
                results = list(filter(lambda x: '-l=' in x, args))
                limit = int(str.split(results[0], '=')[1])
                # Just in case someone adds a negative integer by accident, the limit will be set to 0.
                if limit < 0:
                    limit = 0

            if 'w' in args:
                write = True
            else:
                write = False

            if mode == 'h' or mode == 'help':
                self.display_help_menu()
            else:
                fetcher = Fetcher
                page = fetcher.get_page(target)
                content = page.content
                if mode == 't':
                    self.find_all_with_tag(content, arguments, write, limit)
                elif mode == 'c':
                    self.find_all_with_class(content, arguments, write, limit)
                elif mode == 'i':
                    self.find_all_image_urls(content, write, limit)
                elif mode == 'a':
                    self.find_all_link_urls(content, write, limit)


if __name__ == '__main__':
    scraper = Scraper()
    scraper.main()
