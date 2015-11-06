__author__ = 'frederic.drew'

import time

from Eveuni_parser import Eveuni_parser
from Ship import Ship

ships = list()


def main():
    ship_list_file = open("ship_list.txt", "r")
    # ship_list_file =  ["Algos"]
    importfile = open("anki_import.txt", "a")
    eve_uni = Eveuni_parser()

    for ship_name in ship_list_file:
        ship_name = ship_name.replace(" ", "_")
        ship_name = ship_name.strip()
        ship = Ship(ship_name)
        eve_uni.fetch_ship_info(ship.name)
        ship.bonuses = eve_uni.get_bonuses()
        ship.faction = eve_uni.get_faction()
        ship.ecm = eve_uni.get_ecm()
        ship.hull = eve_uni.get_hull()
        ships.append(ship)

        importfile.write(ship.print_ship());
        importfile.flush()
        print ship_name
        time.sleep(0.5)

        # print ship.print_faction()


if __name__ == '__main__':
    main()
