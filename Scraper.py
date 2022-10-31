import sys
from Fetcher import Fetcher
from Parser import Parser
from datetime import datetime


class Scraper(object):
    @staticmethod
    def find_all_with_tag(content, tag, write, limit, recursive):
        if write:
            date_obj = datetime.now()
            timestamp = str(date_obj.timestamp())
            results = Parser.find_elements_by_tag(content, tag, limit, recursive)
            file = open(timestamp + 'txt', 'w+')
            for result in results:
                file.write(result+"\r\n")
        else:
            print(Parser.find_elements_by_tag(content, tag, limit, recursive))

    @staticmethod
    def find_all_image_urls(content, write, limit, recursive):
        if write:
            date_obj = datetime.now()
            timestamp = str(date_obj.timestamp())
            results = Parser.find_all_image_urls(content, limit, recursive)
            file = open(timestamp + 'txt', 'w+')
            for result in results:
                file.write(result+"\r\n")
        else:
            print(Parser.find_all_image_urls(content, limit, recursive))

    @staticmethod
    def find_all_link_urls(content, write, limit, recursive):
        if write:
            date_obj = datetime.now()
            timestamp = str(date_obj.timestamp())
            results = Parser.find_all_link_urls(content, limit, recursive)
            file = open(timestamp + '.txt', 'w+')
            for result in results:
                file.write(result+"\r\n")
        else:
            print(Parser.find_all_link_urls(content, limit, recursive))

    @staticmethod
    def find_all_with_class(content, class_name, write, limit, recursive):
        if write:
            date_obj = datetime.now()
            timestamp = str(date_obj.timestamp())
            results = Parser.find_all_with_class(content, class_name, limit, recursive)
            file = open(timestamp + '.txt', 'w+')
            for result in results:
                file.write(result+"\r\n")
        else:
            print(Parser.find_all_with_class(content, class_name, limit, recursive))

    @staticmethod
    def find_all_with_attribute(content, attribute, write, limit, recursive):
        if write:
            date_obj = datetime.now()
            timestamp = str(date_obj.timestamp())
            results = Parser.find_all_with_attribute(content, attribute, limit, recursive)
            file = open(timestamp + '.txt', 'w+')
            for result in results:
                file.write(result + "\r\n")
        else:
            print(Parser.find_all_with_attribute(content, attribute, limit, recursive))

    @staticmethod
    def find_with_inner_text(content, argument, write, limit, recursive):
        if write:
            date_obj = datetime.now()
            timestamp = str(date_obj.timestamp())
            results = Parser.find_all_inner_text(content, argument, limit, recursive)
            file = open(timestamp + '.txt', 'w+')
            for result in results:
                file.write(result + "\r\n")
        else:
            print(Parser.find_all_inner_text(content, argument, limit, recursive))

    @staticmethod
    def find_parents_from_inner_text(content, argument, write):
        if write:
            date_obj = datetime.now()
            timestamp = str(date_obj.timestamp())
            results = Parser.find_parent_from_inner_text(content, argument)
            file = open(timestamp + '.txt', 'w+')
            for result in results:
                file.write(result + "\r\n")
        else:
            print(Parser.find_parent_from_inner_text(content, argument))

    @staticmethod
    def display_help_menu():
        help_string = 'usage: Scrape.py <mode> <target> [option] ... [arg] [l=<integer>] [w] [n]'
        help_string = help_string + '\n Modes: '
        help_string = help_string + '-t : Find all with specified tag, requires the tag passed as arg\n'
        help_string = help_string + '-c : Find all with specified class, requires the class passed as arg\n'
        help_string = help_string + '-i : Find all image urls\n'
        help_string = help_string + '-a : Find all link urls\n'
        help_string = help_string + 'n : Disable recursive searching, only display direct children\n'
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
        modes_with_arguments = ['t', 'c', 'v', 'r', 'p']
        if len(args) < 2:
            print('Please add arguments to proceed.')
        else:
            if len(args) > 2:
                target = args[2]
            else:
                target = ''
            mode = args[1]
            mode = mode.replace('-', '')
            if len(args) >= 4 and mode in modes_with_arguments:
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

            if 'n' in args:
                recursive = False
            else:
                recursive = True

            if mode == 'h' or mode == 'help':
                self.display_help_menu()
            else:
                fetcher = Fetcher
                page = fetcher.get_page(target)
                content = page.content
                if mode == 't':
                    self.find_all_with_tag(content, arguments, write, limit, recursive)
                elif mode == 'c':
                    self.find_all_with_class(content, arguments, write, limit, recursive)
                elif mode == 'i':
                    self.find_all_image_urls(content, write, limit, recursive)
                elif mode == 'a':
                    self.find_all_link_urls(content, write, limit, recursive)
                elif mode == 'v':
                    self.find_all_with_attribute(content, arguments, write, limit, recursive)
                elif mode == 'r':
                    self.find_with_inner_text(content, arguments, write, limit, recursive)
                elif mode == 'p':
                    self.find_parents_from_inner_text(content, arguments, write)


if __name__ == '__main__':
    scraper = Scraper()
    scraper.main()
