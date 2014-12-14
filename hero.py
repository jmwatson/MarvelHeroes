import logging
from db import DB

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Hero:
    def __init__(self, hero_name):
        info = DB.get_document('heroes/' + hero_name + '.json')
        self.attribute_bonus = DB.get_document('stats/attribute_bonuses.json')
        self.stats = dict(info['defensive_stats'].items() + info['offensive_stats'].items() +
                          info['utility_stats'].items())
        self.attribute = dict()

        for attribute, points in info['attributes']:
            self.add_attribute_points(attribute, info['attributes'][attribute])

    def add_attribute_points(self, name, points):
        self.attribute[name] += points
        for attribute, bonus in self.attribute_bonus[name]['rank'].iteritems():
            if attribute in self.stats:
                self.stats[attribute] += bonus
                
        for attribute, bonus in self.attribute_bonus[name]['rank_per_level']:
            if attribute in self.stats:
                self.stats[attribute] += (60 * bonus)
