__author__ = 'frederic.drew'

from lxml import etree
import html2text


class Html_parser:
    def __init__(self, html):
        self.etree = etree.HTML(html)
        self.h = html2text.HTML2Text()
        self.h.ignore_links = True

    def parse_text(self, query_string):
        result = list()
        for entry in self.etree.xpath(query_string):
            string = self.h.handle(entry).encode('utf-8').strip()
            string = string.replace("\n", " ")
            if string != "":
                result.append(string)
        return result
