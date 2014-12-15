import logging
from db import DB

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Hero:
    MAX_POWER_POINTS = 20

    def __init__(self, hero_name):
        info = DB.get_document('heroes/' + hero_name + '.json')
        self.attribute_bonus = DB.get_document('stats/attribute_bonuses.json')
        self.attribute = dict()
        self.power = dict()
        self.available_powers = info['available_powers']
        self.stats = dict(info['stats']['defensive_stats'].items() + info['stats']['offensive_stats'].items() +
                          info['stats']['utility_stats'].items())
        for attribute, points in info['attributes'].iteritems():
            self.add_attribute_points(attribute, info['attributes'][attribute])
        for power_id, points in info['powers'].iteritems():
            self.add_power_points(int(power_id), info['powers'][power_id])

    def add_attribute_points(self, name, points):
        if name not in self.attribute:
            self.attribute[name] = points
        else:
            self.attribute[name] += points
        for attribute, bonus in self.attribute_bonus[name]['rank'].iteritems():
            if attribute in self.stats:
                self.stats[attribute] += bonus
        if 'rank_per_level' in self.attribute_bonus[name]:
            for attribute, bonus in self.attribute_bonus[name]['rank_per_level'].iteritems():
                if attribute in self.stats:
                    self.stats[attribute] += (60 * bonus)

    def add_power_points(self, power_id, points):
        if power_id in self.available_powers:
            if power_id not in self.power:
                self.power[power_id] = points
            else:
                if self.power[power_id] + points > self.MAX_POWER_POINTS:
                    self.power[power_id] = self.MAX_POWER_POINTS
                else:
                    self.power[power_id] += points

    def set_power_points(self, power_id, points):
        if power_id in self.available_powers:
            self.power[power_id] = points if points <= self.MAX_POWER_POINTS else self.MAX_POWER_POINTS
