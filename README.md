# scrapepy
## Usage
To use, simply run `python Scraper.py <mode> <target> <arguments> [-l=] [n] [w]`.
 

`<arguments>` is optional and used for specifying search parameters for `t` and `c` modes.

`w`, `-l=` and `n` can be added in any order after any `<arguments>`

`w`: is an optional argument, if added the results will be written to a file in the same folder.

`-l=`x: is an optional argument. Sets a limit for the results the parser returns. X represents a positive integer that sets the limit.

`n`: Disables recursive searching and will only find tag and direct children. Optional, as recursive is enabled by default.

All arguments (except write `w` and disable recursive `n`) must be prefixed with a `-`.

_Modes_
  - t: Search for all occurrences of a specified tag (this requires you to specify the tag to search for)
  - c: Search for all occurrences af a specified class (this requires you to specify the class to search for, as an arg)
  - v: Search for all occurrences af a specified attribute pair (this requires you to specify the value pair to search for, as an arg). Arg format is ``attribute:value``
  - r: Search for all occurrences af a specified inner text (this requires you to specify the inner text to search for, as an arg)
  - i: Find the image source for all images at specified target
  - a: Find all link hrefs at specified target
  - h: Display help menu
