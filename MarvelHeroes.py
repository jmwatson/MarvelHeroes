from flask import Flask
import flask
import hashlib
# import json
import logging
# import math
from mh_math import MHMath
import power


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)


@app.route('/')
def hello_world():
    return flask.jsonify({
        'message': 'Hello World',
    })


@app.route('/rr/<powers>/<omegas>/<synergies>')
def rocket_raccoon(powers, omegas, synergies):
    # base_dmg_percent = 57.8
    # energy_dmg_percent = 66.1
    # physical_dmg_percent = 44.8
    # ranged_dmg_percent = 3.8
    # summon_dmg_percent = 348.5

    photon_pistols = power.EnergyPower(1)
    m78_plasma_launcher = power.EnergyPower(2)
    big_flarkin_gun = power.EnergyPower(3)
    shoot_and_run = power.EnergyPower(4)
    photon_minigun = power.EnergyPower(5)
    heavy_plasma_rifle = power.EnergyPower(6)
    heavy_gauss_rifle = power.EnergyPower(7)

    my_friend_groot = power.SummonedPower(8)
    my_friend_groot = power.SummonedPower(9)
    blaster_turret = power.SummonedPower(10)
    c12_stun_grenade = power.EnergyPower(11)
    time_warp_turret = power.SummonedPower(12)
    suppression_turret = power.SummonedPower(13)
    gravity_mine = power.EnergyPower(14)

    # rockets_dmg_percent = energy_dmg_percent + ranged_dmg_percent
    return flask.jsonify({
        'character': 'Rocket Raccoon',
        # 'powers': powers,
        # 'omegas': omegas,
        # 'synergies': synergies,
        'weapon_specialist': {
            'photon_pistols': photon_pistols.average_dps('rocket_raccoon'),
            'm78_plasma_launcher': m78_plasma_launcher.average_dps('rocket_raccoon'),
            'big_flarkin_gun': big_flarkin_gun.average_dps('rocket_raccoon'),
            'shoot_and_run': shoot_and_run.average_dps('rocket_raccoon'),
            'photon_minigun': photon_minigun.average_dps('rocket_raccoon'),
            'heavy_plasma_rifle': heavy_plasma_rifle.average_dps('rocket_raccoon'),
            'heavy_gauss_rifle': heavy_gauss_rifle.average_dps('rocket_raccoon'),
        },
        # 'galactic_guardian': {
        #     'my_friend_groot': MHMath.percent_to_dps(summon_dmg_percent, MHMath.avg(range(9752, 14628)), 1),
        #     'my_friend_groot_charge': MHMath.percent_to_dps(summon_dmg_percent, MHMath.avg(range(20587, 30880)), 0.2),
        #     'blaster_turret': MHMath.percent_to_dps(summon_dmg_percent, MHMath.avg(range(911, 1366)), 2),
        #     'c12_stun_grenade': MHMath.percent_to_dps(rockets_dmg_percent, MHMath.avg(range(14817, 22225)), 1.1),
        #     'time_warp_turret': MHMath.percent_to_dps(summon_dmg_percent, MHMath.avg(range(32506, 48758)), 0.25),
        #     'suppression_turret': MHMath.percent_to_dps(summon_dmg_percent, MHMath.avg(range(4211, 6317)), 1),
        #     'gravity_mine': MHMath.percent_to_dps(rockets_dmg_percent, MHMath.avg(range(11120, 16680)), 1.5),
        # },
        # 'tactical_genius': {
        #     'rocket_dash': MHMath.percent_to_dps(rockets_dmg_percent, MHMath.avg(range(11571, 17356)), 3),
        #     'h7_fleetslayer': MHMath.percent_to_dps(rockets_dmg_percent, MHMath.avg(range(55928, 83892)) * 4, 0.04),
        # }
    })


@app.route('/rr/build/<key>')
def rocket_raccoon_build(key):
    return 'Rocket Raccoon key %s' % key


def generate_build_url(params):
    hash = hashlib.md5(''.join(params))
    return hash.hexdigest()


# def calc_power_dps(dmg_range, percent_bonus):
#     return MHMath.percent_to_dps(percent_bonus, MHMath.avg(dmg_range), )


if __name__ == '__main__':
    app.run()
