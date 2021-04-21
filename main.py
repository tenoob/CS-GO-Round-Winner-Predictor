from pywebio.input import *
from pywebio.output import *
from model import crete_input_for_model , scale_data , test_model
from pywebio import STATIC_PATH
from flask import Flask, send_from_directory
from pywebio.platform.flask import webio_view
from pywebio import start_server
import argparse

app = Flask(__name__)

# list of all weapons, maps and bomb plant status
guns_list = ['AK-47', 'AUG', 'FAMAS', 'Galil AR', 'M4A1-S', 'M4A4', 'SG 553', 'AWP', 'G3SG1', 'SCAR-20', 'SSG 08',
             'MAC-10', 'MP5-SD', 'MP7', 'MP9', 'P90', 'PP-Bizon', 'UMP-45', 'MAG-7', 'Nova', 'Sawed-Off', 'XM1014',
             'M249', 'Negev']
# guns_list = guns_list_1+guns_list_2
pistols_list = ['CZ75-Auto', 'Desert Eagle', 'Dual Berettas', 'Five-Seven', 'Glock-18', 'P2000', 'P250', 'R8 Revolver',
                'Tec-9', 'USP-S']
# pistols_list = pistols_list_1+pistols_list_2
utility_list = ['Decoy', 'Flashbang', 'Smoke', 'HE', 'Incendiary', 'Molotov Cocktail']
map_list = ['de_dust2', 'de_mirage', 'de_nuke', 'de_inferno', 'de_overpass', 'de_vertigo', 'de_train', 'de_cache']
bomb_planted_list = ['False', "True"]



# function for Counter-Terrosist
def Counter_terrorist():
    with use_scope('ct'):
        tital = open('images/ct_head.jpg', 'rb').read()
        left = open('images/ct_left.jpg', 'rb').read()
        right = open('images/ct_right.jpg', 'rb').read()

        put_image(tital, width='100%')

        # taking input for all weapons
        ct_info = input_group('Counter Terrorist', [
            input('Time Left:', name='time_left', type=NUMBER, min='0',max='270', style='color:blue'),
            radio('Map:', name='map', options=map_list, inline=True),
            radio('Bomb Planted:', name='bomb_planted', options=bomb_planted_list, inline=True),

            input('CT Score:', name='ct_score', type=NUMBER, min='0', style='color:blue'),
            input('CT Money:', name='ct_money', type=NUMBER, min='0', style='color:blue'),
            input('Combined CT Health:', name='ct_health', type=NUMBER, help_text='Range 0 - 500', min='0', max='500',
                  style='color:blue'),
            input('Combined CT Armor:', name='ct_armor', type=NUMBER, help_text='Range 0 - 500', min='0', max='500',
                  style='color:blue'),
            radio('Total CT Helmets:', name='ct_helmets', options=[0, 1, 2, 3, 4, 5], inline=True, style='color:blue'),
            radio('Total CT Defuse Kits:', name='ct_defuse_kits', options=[0, 1, 2, 3, 4, 5], inline=True,
                  style='color:blue'),
            radio('Total CT PLayers Alive:', name='ct_players_alive', options=[0, 1, 2, 3, 4, 5], inline=True,
                  style='color:blue'),
            checkbox('Primary Weapon:', name='selected_guns', options=guns_list, inline=True),
            checkbox('Secondary Weapon:', name='selected_pistols', options=pistols_list, style='color:blue',
                     inline=True),
            checkbox('Utility:', name='selected_utility', options=utility_list, style='color:blue', inline=True)
        ])

        # Getting the Quantity for the primart weapon else set it to 0
        for weapons in guns_list:
            if weapons in ct_info['selected_guns']:
                x = 'ct_weapons_' + weapons
                y = input('Number of weapons for {}'.format(weapons), type=NUMBER, min=0, max=5)
                ct_info.update({x: y})
            else:
                x = 'ct_weapons_' + weapons
                y = 0
                ct_info.update({x: y})

        # Getting the Quantity for the Secondary weapn else set to 0
        for weapons in pistols_list:
            if weapons in ct_info['selected_pistols']:
                x = 'ct_weapons_' + weapons
                y = input('Number of weapons for {}'.format(weapons), type=NUMBER, min=0, max=5)
                ct_info.update({x: y})
            else:
                x = 'ct_weapons_' + weapons
                y = 0
                ct_info.update({x: y})

        # Getting the Quantity for the Utilits else set to 0
        for util in utility_list:
            if util in ct_info['selected_utility']:
                x = 'ct_weapons_' + util
                y = input('Number of weapons for {}'.format(util), type=NUMBER, min=0, max=5)
                ct_info.update({x: y})
            else:
                x = 'ct_weapons_' + util
                y = 0
                ct_info.update({x: y})

        # convert the categorical value into numerical
        x, y = ct_info['map'], ct_info['bomb_planted']
        ct_info['map'] = map_list.index(x)
        ct_info['bomb_planted'] = bomb_planted_list.index(y)

        # style([put_text(ct_info)],'color:red' ,)
        # close the use_scope(ct)
        remove('ct')
    return ct_info


# function for Terrorist
def terrorist():
    with use_scope('t'):
        tital = open('images/t_tital.jpg', 'rb').read()
        put_image(tital, width='100%')

        # taking input for all weapons
        t_info = input_group('Terrorist', [
            input('T Score:', name='t_score', type=NUMBER, min='0', style='color:orange'),
            input('T Money:', name='t_money', type=NUMBER, min='0', style='color:orange'),
            input('Combined T Health:', name='t_health', type=NUMBER, help_text='Range 0 - 500', min='0', max='500',
                  style='color:orange'),
            input('Combined T Armor:', name='t_armor', type=NUMBER, help_text='Range 0 - 500', min='0', max='500',
                  style='color:orange'),
            radio('Total T Helmets:', name='t_helmets', options=[0, 1, 2, 3, 4, 5], inline=True, style='color:yellow'),
            radio('Total T PLayers Alive:', name='t_players_alive', options=[0, 1, 2, 3, 4, 5], inline=True,
                  style='color:yellow'),
            checkbox('Primary Weapon:', name='selected_guns', options=guns_list, inline=True),
            checkbox('Secondary Weapon:', name='selected_pistols', options=pistols_list, style='color:yellow',
                     inline=True),
            checkbox('Utility:', name='selected_utility', options=utility_list, style='color:yellow', inline=True)
        ])

        # Getting the Quantity for the primary weapon else set it to 0
        for weapons in guns_list:
            if weapons in t_info['selected_guns']:
                x = 't_weapons_' + weapons
                y = input('Number of weapons for {}'.format(weapons), type=NUMBER, min=0, max=5)
                t_info.update({x: y})
            else:
                x = 't_weapons_' + weapons
                y = 0
                t_info.update({x: y})

        # Getting the Quantity for the Secondary weapn else set to 0
        for weapons in pistols_list:
            if weapons in t_info['selected_pistols']:
                x = 't_weapons_' + weapons
                y = input('Number of weapons for {}'.format(weapons), type=NUMBER, min=0, max=5)
                t_info.update({x: y})
            else:
                x = 't_weapons_' + weapons
                y = 0
                t_info.update({x: y})

        # Getting the Quantity for the Utilits else set to 0
        for util in utility_list:
            if util in t_info['selected_utility']:
                x = 't_weapons_' + util
                y = input('Number of weapons for {}'.format(util), type=NUMBER, min=0, max=5)
                t_info.update({x: y})
            else:
                x = 't_weapons_' + util
                y = 0
                t_info.update({x: y})

        # style([put_text(t_info)],'color:red' ,)
        remove('t')
    return t_info

def prediction(ans):
    with use_scope('pred'):
        tital = open('images/csgo.png', 'rb').read()
        put_image(tital,width='100%')
        style(put_text(ans),'color:red , font-size:30px')



# main function
def main_fun():
    ct = Counter_terrorist()
    t = terrorist()
    print('ct:', ct)
    print('t:', t)

    l1 = crete_input_for_model(ct, t)
    x = scale_data(l1)
    ans = test_model(x)

    actual = prediction(ans)

    print(actual)



app.add_url_rule('/', 'webio_view', webio_view(main_fun), methods=['GET', 'POST', 'OPTIONS'])
app.run(host='localhost', port=80, debug=True)
'''if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=int, default=8080)
    args = parser.parse_args()

    start_server(main_fun, port=args.port)'''

