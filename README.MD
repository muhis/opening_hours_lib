[![Build Status](https://travis-ci.com/muhis/opening_hours_lib.svg?branch=master)](https://travis-ci.com/muhis/opening_hours_lib)

# Introduction:
This library helps you parse opening hours of places from epoch time into readable human AM-PM time.


# Installation:
```sh
pip install git+https://github.com/muhis/opening_hours_lib.git
```
I know it requires an egg, but you don't always get what you ask for.


# Basic usage:
```python
from parsing_tools import parse, stringify_parsed_json
# You can use this for JSON/XML responses.
parsed_data = parse(json.load(payload))
# You can print this on big sign and hang it somewhere.
stringified_data = stringify_parsed_json(parsed_data)
```

# Limitations:
This is Alpha version that is not ready to go to production. There are many pitfalls:
    - If the json provided by the user starts with a close time, the result will be messed up.
