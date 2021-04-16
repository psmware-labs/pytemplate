#!/usr/bin/env python

#  SPDX-License-Identifier: AGPL-3.0-only
#  Copyright (C) 2020-2021  Patrick McLean - psmware ltd

#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.

#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.

# Import the path function as this allows us to check for a file
from pathlib import Path

the_file_i_want_to_find = Path("/path/to/the/file.csv")

# Now we check to see if the source file exists
if the_file_i_want_to_find.exists():
    print("Hurray! The data I want is in {}.".format(the_file_i_want_to_find))
else:
    # wrapping this line because pep8 coding standard
    print("Dang it! It looks like {} does "
          "not exist.".format(the_file_i_want_to_find))

# to run me type `python main.py` in the VS Code terminal
