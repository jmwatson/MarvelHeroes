import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class MHMath:
    DMG_RATING_PER_PERCENT = 40

    def __init__(self):
        return

    @staticmethod
    def dmg_rating_to_percent(dmg_rating):
        return float(dmg_rating / MHMath.DMG_RATING_PER_PERCENT)

    @staticmethod
    def percent_to_dmg_rating(percent):
        return MHMath.DMG_RATING_PER_PERCENT * percent

    @staticmethod
    def percent_to_dps(percent, damage, hits_per_second):
        dps = (damage * MHMath.percent_to_decimal(percent)) * hits_per_second
        dps = int(dps * 100)
        dps /= 100.0
        return dps

    @staticmethod
    def percent_to_decimal(percent):
        return percent / 100.0

    @staticmethod
    def avg(num_range):
        return float(sum(num_range) / len(num_range))

    @staticmethod
    def average_dps(base_dmg_range, hits_per_second, percent_bonus, crit_chance, crit_bonus, brut_chance, brut_bonus):
        dps = MHMath.percent_to_dps(percent_bonus, base_dmg_range, hits_per_second)
        crit_dps = MHMath.percent_to_dps(crit_bonus, base_dmg_range, hits_per_second)
        brut_dps = MHMath.percent_to_dps(brut_bonus, base_dmg_range, hits_per_second)
        base_chance = (100 - crit_chance) / 100
        crit_chance = (crit_chance - brut_chance) / 100
        brut_chance = brut_chance / 100
        logger.log(base_chance + crit_chance + brut_chance)
        return (dps * base_chance) + (crit_dps * crit_chance) + (brut_dps * brut_chance)

