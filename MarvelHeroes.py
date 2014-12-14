import flask
from flask import Flask
from power import *
import hashlib
import logging


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

    photon_pistols = EnergyPower(1)
    m78_plasma_launcher = EnergyPower(2)
    big_flarkin_gun = EnergyPower(3)
    shoot_and_run = EnergyPower(4)
    photon_minigun = EnergyPower(5)
    heavy_plasma_rifle = EnergyPower(6)
    heavy_gauss_rifle = EnergyPower(7)

    my_friend_groot = SummonedPower(8)
    my_friend_groot_charge = SummonedPower(9)
    blaster_turret = SummonedPower(10)
    c12_stun_grenade = EnergyPower(11)
    time_warp_turret = SummonedPower(12)
    suppression_turret = SummonedPower(13)
    gravity_mine = EnergyPower(14)

    rocket_dash = EnergyPower(15)
    h7_fleetslayer = EnergyPower(16)

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
        'galactic_guardian': {
            'my_friend_groot': my_friend_groot.average_dps('rocket_raccoon'),
            'my_friend_groot_charge': my_friend_groot_charge.average_dps('rocket_raccoon'),
            'blaster_turret': blaster_turret.average_dps('rocket_raccoon'),
            'c12_stun_grenade': c12_stun_grenade.average_dps('rocket_raccoon'),
            'time_warp_turret': time_warp_turret.average_dps('rocket_raccoon'),
            'suppression_turret': suppression_turret.average_dps('rocket_raccoon'),
            'gravity_mine': gravity_mine.average_dps('rocket_raccoon'),
        },
        'tactical_genius': {
            'rocket_dash': rocket_dash.average_dps('rocket_raccoon'),
            'h7_fleetslayer': h7_fleetslayer.average_dps('rocket_raccoon'),
        },
        'summoner': Power.average([h7_fleetslayer.average_dps('rocket_raccoon'),
                                   gravity_mine.average_dps('rocket_raccoon'),
                                   suppression_turret.average_dps('rocket_raccoon'),
                                   time_warp_turret.average_dps('rocket_raccoon'),
                                   my_friend_groot.average_dps('rocket_raccoon'),
                                   m78_plasma_launcher.average_dps('rocket_raccoon'),
                                   photon_pistols.average_dps('rocket_raccoon')]),
        'gunner': Power.average([h7_fleetslayer.average_dps('rocket_raccoon'),
                                 photon_minigun.average_dps('rocket_raccoon'),
                                 my_friend_groot.average_dps('rocket_raccoon'),
                                 m78_plasma_launcher.average_dps('rocket_raccoon'),
                                 heavy_gauss_rifle.average_dps('rocket_raccoon')]),
        'hybrid': Power.average([h7_fleetslayer.average_dps('rocket_raccoon'),
                                 photon_minigun.average_dps('rocket_raccoon'),
                                 my_friend_groot.average_dps('rocket_raccoon'),
                                 m78_plasma_launcher.average_dps('rocket_raccoon'),
                                 suppression_turret.average_dps('rocket_raccoon'),
                                 time_warp_turret.average_dps('rocket_raccoon'),
                                 heavy_gauss_rifle.average_dps('rocket_raccoon')]),
    })


@app.route('/rr/build/<key>')
def rocket_raccoon_build(key):
    return 'Rocket Raccoon key %s' % key


def generate_build_url(params):
    hash = hashlib.md5(''.join(params))
    return hash.hexdigest()


if __name__ == '__main__':
    app.run()
