# scrapepy
## Usage
To use, simply run `python Scraper.py <target> <mode> <arguments> [w]`, w is an optional argument, if added the results will be written to a file in the same folder.
 `<arguments>` is also optional and used for specifying search parameters for `t` and `c` modes.

_Modes_
  - t: Search for all occurrences of a specified tag (this requires you to specify the tag to search for)
  - c: Search for all occurrences af a specified class (this requires you to specify the class to search for, as an arg)
  - i: Find the image source for all images at specified target
  - a: Find all link hrefs at specified target
  - h: Display help menu
