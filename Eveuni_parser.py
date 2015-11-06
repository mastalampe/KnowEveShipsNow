from urllib2 import urlopen

__author__ = 'frederic.drew'

from Ship_bonuses import Ship_bonuses
from Html_parser import Html_parser


class Eveuni_parser():
    baseurl = 'http://wiki.eveuniversity.org/'
    ecm = '//div[@class="ecm-priority"]//div[contains(@class,"label2")]//text()';
    faction = '//td[@class="faction"]/text()';
    hull = '//td[@class="hull-type"]/a/text()';

    def __init__(self):
        self.html_parser = None

    def fetch_ship_info(self, ship):
        self.ship_name = ship
        # html = (open("ashimmu.html","r").read());
        html = urlopen(Eveuni_parser.baseurl + ship).read()
        self.html_parser = Html_parser(html)

    def get_bonuses(self):
        bonuses = Ship_bonuses(self.html_parser)
        bonuses.parse_bonuses()
        return bonuses

    def get_hull(self):
        return self.html_parser.parse_text(Eveuni_parser.hull).pop()

    def get_ecm(self):
        return self.html_parser.parse_text(Eveuni_parser.ecm).pop()

    def get_faction(self):
        return self.html_parser.parse_text(Eveuni_parser.faction).pop()
