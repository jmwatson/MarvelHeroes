import flask
from flask import *
from power import *
from hero import *
# import hashlib

app = Flask(__name__)


@app.route('/')
def hello_world():
    return flask.jsonify({
        'message': 'Hello World',
    })


@app.route('/rr/')
@app.route('/rr/', methods='POST')
def rocket_raccoon():
    data = request.json
    rocket = Hero('rocket_raccoon')
    for power_id, points in data['powers']:
        rocket.set_power_points(int(power_id), points)
    # rocket.set_power_points(2, Hero.MAX_POWER_POINTS)
    # rocket.set_power_points(3, Hero.MAX_POWER_POINTS)
    # rocket.set_power_points(5, Hero.MAX_POWER_POINTS)
    # rocket.set_power_points(8, Hero.MAX_POWER_POINTS)
    # rocket.set_power_points(9, Hero.MAX_POWER_POINTS)
    # rocket.set_power_points(16, Hero.MAX_POWER_POINTS)
    app.logger.info(rocket.power)

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


# @app.route('/rr/build/<key>')
# def rocket_raccoon_build(key):
#     return 'Rocket Raccoon key %s' % key
#
#
# def generate_build_url(params):
#     hash = hashlib.md5(''.join(params))
#     return hash.hexdigest()

if __name__ == '__main__':
    # app.debug = True
    app.run()
