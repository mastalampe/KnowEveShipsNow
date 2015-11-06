__author__ = 'frederic.drew'

from anki_formatter import Anki_formatter


class Ship():
    def __init__(self, name):
        self.printer = Anki_formatter
        self.name = name
        self.bonuses = None
        self.ecm = None
        self.faction = None
        self.hull = None

    def print_hull(self):
        return self.printer.format_kv("Hull Type", self.hull)

    def print_ecm(self):
        return self.printer.format_kv("ECM Type", self.ecm)

    def print_faction(self):
        return self.printer.format_kv("Faction", self.faction)

    def print_bonuses(self):
        string = "</br>"
        for key in self.bonuses:
            string = '%s%s</br>' % (string, self.printer.format_kv(key, self.bonuses[key]))

        return string

    def print_ship(self):
        back = [self.print_faction(), self.print_hull(), self.print_ecm(), self.print_bonuses()]
        tags = [self.hull, self.faction]
        return self.printer.format_all(self.name, back, tags)
