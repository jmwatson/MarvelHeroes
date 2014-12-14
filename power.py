import logging
from db import DB

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Power:
    def __init__(self, power_id):
        self.stats = DB.get_document('powers/power_' + repr(power_id) + '.json')

        if 'low' in self.stats:
            self.average_damage = self.average(range(self.stats['low'], self.stats['high']))
        else:
            self.average_damage = self.stats['damage']

        self.hits_per_second = self.stats['hits_per_second']
        self.DMG_RATING_PER_PERCENT = 40

    def calculate_dps(self, dmg_bonus, hero):
        critical_chance = self.dmg_rating_to_percent(hero['stats']['offensive_stats']['critical_hit_rating'])
        critical_bonus = self.dmg_rating_to_percent(hero['stats']['offensive_stats']['critical_damage_rating'])
        brutal_chance = self.dmg_rating_to_percent(hero['stats']['offensive_stats']['brutal_strike_rating'])
        brutal_bonus = self.dmg_rating_to_percent(hero['stats']['offensive_stats']['brutal_damage_rating'])

        dps = self.dps(dmg_bonus, self.hits_per_second)
        critical_dps = self.dps(critical_bonus, self.hits_per_second)
        brutal_dps = self.dps(brutal_bonus, self.hits_per_second)

        base_chance = (100 - critical_chance) / 100
        critical_chance = (critical_chance - brutal_chance) / 100
        brutal_chance /= 100

        return int(((dps * base_chance) + (critical_dps * critical_chance) + (brutal_dps * brutal_chance)) * 100) / 100.0

    def average_dps(self, hero_name):
        hero = DB.get_document('heroes/' + hero_name + '.json')
        dmg_bonus = hero['stats']['offensive_stats']['base_damage'] + \
                    self.dmg_rating_to_percent(hero['stats']['offensive_stats']['damage_rating'])
        return self.calculate_dps(dmg_bonus, hero)

    def dps(self, percent_bonus, hits_per_second):
        dps = self.average_damage * percent_bonus * hits_per_second
        dps = int(dps * 100)
        dps /= 100.0
        return dps

    @staticmethod
    def average(dmg_range):
        return sum(dmg_range) / len(dmg_range)

    def dmg_rating_to_percent(self, dmg_rating):
        return float(dmg_rating / self.DMG_RATING_PER_PERCENT)


class PhysicalPower(Power):
    def average_dps(self, hero_name):
        hero = DB.get_document('heroes/' + hero_name + '.json')
        dmg_bonus = hero['stats']['offensive_stats']['physical_base_damage'] + \
            self.dmg_rating_to_percent(hero['stats']['offensive_stats']['physical_damage_rating'])
        return self.calculate_dps(dmg_bonus, hero)


class EnergyPower(Power):
    def average_dps(self, hero_name):
        hero = DB.get_document('heroes/' + hero_name + '.json')
        dmg_bonus = hero['stats']['offensive_stats']['energy_base_damage'] + \
            self.dmg_rating_to_percent(hero['stats']['offensive_stats']['energy_damage_rating'])
        return self.calculate_dps(dmg_bonus, hero)


class MentalPower(Power):
    def average_dps(self, hero_name):
        hero = DB.get_document('heroes/' + hero_name + '.json')
        dmg_bonus = hero['stats']['offensive_stats']['mental_base_damage'] +\
            self.dmg_rating_to_percent(hero['stats']['offensive_stats']['mental_damage_rating'])
        return self.calculate_dps(dmg_bonus, hero)


class RangedPower(Power):
    def average_dps(self, hero_name):
        hero = DB.get_document('heroes/' + hero_name + '.json')
        dmg_bonus = hero['stats']['offensive_stats']['ranged_base_damage'] + \
            self.dmg_rating_to_percent(hero['stats']['offensive_stats']['ranged_damage_rating'])
        return self.calculate_dps(dmg_bonus, hero)


class MeleePower(Power):
    def average_dps(self, hero_name):
        hero = DB.get_document('heroes/' + hero_name + '.json')
        dmg_bonus = hero['stats']['offensive_stats']['melee_base_damage'] + \
            self.dmg_rating_to_percent(hero['stats']['offensive_stats']['melee_damage_rating'])
        return self.calculate_dps(dmg_bonus, hero)


class SummonedPower(Power):
    def average_dps(self, hero_name):
        hero = DB.get_document('heroes/' + hero_name + '.json')
        dmg_bonus = hero['stats']['offensive_stats']['summoned_ally_damage']
        return self.calculate_dps(dmg_bonus, hero)
