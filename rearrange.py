#!/usr/bin/env python3

import re

"""This scrip will rearrange names when give "Doe, John" to "John Doe"."""

def rearrange_name(name):
  result = re.search(r"^([\w.]*), ([\w.]*)$", name)
  if result is None:
    return  name

  return "{} {}".format(result[2], result[1])

