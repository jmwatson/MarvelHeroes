import logging
from db import DB


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Power:
    def __init__(self, power_id):
        self.stats = DB.get_document('powers/power_' + repr(power_id) + '.json')
        self.dmg_range = range(self.stats.low, self.stats.high)
        self.hits_per_second = self.stats.hits_per_second
        self.DMG_RATING_PER_PERCENT = 40

    def calculate_dps(self, dmg_bonus, hero):
        critical_chance = self.dmg_rating_to_percent(hero.offensive_stats.critical_hit_rating)
        critical_bonus = self.dmg_rating_to_percent(hero.offensive_stats.critical_damage_rating)
        brutal_chance = self.dmg_rating_to_percent(hero.offensive_stats.brutal_hit_rating)
        brutal_bonus = self.dmg_rating_to_percent(hero.offensive_stats.brutal_damage_rating)
        dps = self.dps(self.dmg_range, dmg_bonus, self.hits_per_second)
        critical_dps = self.dps(self.dmg_range, critical_bonus, self.hits_per_second)
        brutal_dps = self.dps(self.dmg_range, brutal_bonus, self.hits_per_second)
        base_chance = (100 - critical_chance) / 100
        critical_chance = (critical_chance - brutal_chance) / 100
        brutal_chance /= 100
        logger.log(base_chance + critical_chance + brutal_chance)
        return (dps * base_chance) + (critical_dps * critical_chance) + (brutal_dps * brutal_chance)

    def average_dps(self, hero_name):
        hero = DB.get_document('heroes/' + hero_name + '.json')
        dmg_bonus = hero.offensive_stats.base_damage + \
                    self.dmg_rating_to_percent(hero.offensive_stats.damage_rating)
        return self.calculate_dps(dmg_bonus, hero)

    def dps(self, base_dmg_range, percent_bonus, hits_per_second):
        dps = self.average(base_dmg_range) * percent_bonus * hits_per_second
        dps = int(dps * 100)
        dps /= 100.0
        return dps

    def average(self, dmg_range):
        return sum(dmg_range) / len(dmg_range)

    def dmg_rating_to_percent(self, dmg_rating):
        return float(dmg_rating / self.DMG_RATING_PER_PERCENT)


class PhysicalPower(Power):
    def average_dps(self, hero_name):
        hero = DB.get_document('heroes/' + hero_name + '.json')
        dmg_bonus = hero.offensive_stats.physical_base_damage + \
            self.dmg_rating_to_percent(hero.offensive_stats.physical_damage_rating)
        return self.calculate_dps(dmg_bonus, hero)


class EnergyPower(Power):
    def average_dps(self, hero_name):
        hero = DB.get_document('heroes/' + hero_name + '.json')
        dmg_bonus = hero.offensive_stats.energy_base_damage + \
            self.dmg_rating_to_percent(hero.offensive_stats.energy_damage_rating)
        return self.calculate_dps(dmg_bonus, hero)


class EnergyPower(Power):
    def average_dps(self, hero_name):
        hero = DB.get_document('heroes/' + hero_name + '.json')
        dmg_bonus = hero.offensive_stats.mental_base_damage +\
            self.dmg_rating_to_percent(hero.offensive_stats.mental_damage_rating)
        return self.calculate_dps(dmg_bonus, hero)


class EnergyPower(Power):
    def average_dps(self, hero_name):
        hero = DB.get_document('heroes/' + hero_name + '.json')
        dmg_bonus = hero.offensive_stats.ranged_base_damage + \
            self.dmg_rating_to_percent(hero.offensive_stats.ranged_damage_rating)
        return self.calculate_dps(dmg_bonus, hero)


class EnergyPower(Power):
    def average_dps(self, hero_name):
        hero = DB.get_document('heroes/' + hero_name + '.json')
        dmg_bonus = hero.offensive_stats.melee_base_damage + \
            self.dmg_rating_to_percent(hero.offensive_stats.melee_damage_rating)
        return self.calculate_dps(dmg_bonus, hero)


class EnergyPower(Power):
    def average_dps(self, hero_name):
        hero = DB.get_document('heroes/' + hero_name + '.json')
        dmg_bonus = hero.offensive_stats.summoned_ally_damage
        return self.calculate_dps(dmg_bonus, hero)
