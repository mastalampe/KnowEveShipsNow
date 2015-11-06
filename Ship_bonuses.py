__author__ = 'frederic.drew'

import re
from collections import OrderedDict


class Ship_bonuses(OrderedDict):
    bonuses = '//div[@class="box-line box-bonuses"]/p//text()'

    def __init__(self, html_parser):
        self.html_parser = html_parser
        OrderedDict.__init__(self)

    def parse_bonuses(self):

        text = self.html_parser.parse_text(Ship_bonuses.bonuses)

        title = ""
        for line in text:
            if re.search(':$', line):
                title = line
                self[line] = list()
            else:
                self[title].append(line)
