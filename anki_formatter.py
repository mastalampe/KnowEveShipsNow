__author__ = 'frederic.drew'

import re

class Anki_formatter:
    @staticmethod
    def format_kv(key, value):
        key = '<b>%s</b>' % key

        if not re.match(".*:", key):
            key = '%s:' % key
        key = '%s ' % key
        if isinstance(value,list):
            key = '%s</br>' % key
            value = "</br>".join(value)
        return '%s%s' % (key, value)

    @staticmethod
    def format_all(front, back, tags):
        back = "</br>".join(back)

        tags_string = ""
        for tag in tags:
            tag = tag.replace(" ", "_")
            tags_string = '%s %s' % (tags_string, tag)

        return '%s ; %s; %s\n' % (front, back, tags_string)
