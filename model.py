from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd
from keras.models import load_model


# create input for the model
def crete_input_for_model(ct_info, t_info):
    lst_1 = [ct_info['time_left'], ct_info['ct_score'], t_info['t_score'], ct_info['map'], ct_info['bomb_planted'],
             ct_info['ct_health'], t_info['t_health'] , ct_info['ct_armor'], t_info['t_armor'], ct_info['ct_money'],
             t_info['t_money'], ct_info['ct_helmets'],
             t_info['t_helmets'], ct_info['ct_defuse_kits'], ct_info['ct_players_alive'], t_info['t_players_alive'] ,
             ct_info['ct_weapons_AK-47'], t_info['t_weapons_AK-47'], ct_info['ct_weapons_AUG'], t_info['t_weapons_AUG'],
             ct_info['ct_weapons_AWP'], t_info['t_weapons_AWP'], ct_info['ct_weapons_PP-Bizon'],
             t_info['t_weapons_PP-Bizon'], ct_info['ct_weapons_CZ75-Auto'], t_info['t_weapons_CZ75-Auto'],
             ct_info['ct_weapons_Dual Berettas'], t_info['t_weapons_Dual Berettas'] , ct_info['ct_weapons_FAMAS'],
             t_info['t_weapons_FAMAS'], ct_info['ct_weapons_G3SG1'],
             t_info['t_weapons_G3SG1'], ct_info['ct_weapons_Galil AR'], t_info['t_weapons_Galil AR'],
             ct_info['ct_weapons_Glock-18'], t_info['t_weapons_Glock-18'], ct_info['ct_weapons_M249'],
             t_info['t_weapons_M249'], ct_info['ct_weapons_M4A1-S'] , t_info['t_weapons_M4A1-S'],
             ct_info['ct_weapons_M4A4'], t_info['t_weapons_M4A4'],
             ct_info['ct_weapons_MAC-10'], t_info['t_weapons_MAC-10'], ct_info['ct_weapons_MAG-7'],
             t_info['t_weapons_MAG-7'], ct_info['ct_weapons_MP5-SD'], t_info['t_weapons_MP5-SD'] ,
             ct_info['ct_weapons_MP7'], t_info['t_weapons_MP7'], ct_info['ct_weapons_MP9'], t_info['t_weapons_MP9'],
             ct_info['ct_weapons_Negev'], t_info['t_weapons_Negev'], ct_info['ct_weapons_Nova'],
             t_info['t_weapons_Nova'], ct_info['ct_weapons_P90'], t_info['t_weapons_P90'] ,
             ct_info['ct_weapons_R8 Revolver'], t_info['t_weapons_R8 Revolver'], ct_info['ct_weapons_Sawed-Off'],
             t_info['t_weapons_Sawed-Off'], ct_info['ct_weapons_SCAR-20'], t_info['t_weapons_SCAR-20'],
             ct_info['ct_weapons_SG 553'], t_info['t_weapons_SG 553'], ct_info['ct_weapons_SSG 08'],
             t_info['t_weapons_SSG 08'] ,ct_info['ct_weapons_UMP-45'], t_info['t_weapons_UMP-45'],
             ct_info['ct_weapons_XM1014'],
             t_info['t_weapons_XM1014'], ct_info['ct_weapons_Desert Eagle'], t_info['t_weapons_Desert Eagle'],
             ct_info['ct_weapons_Five-Seven'], t_info['t_weapons_Five-Seven'], ct_info['ct_weapons_USP-S'],
             t_info['t_weapons_USP-S'], ct_info['ct_weapons_P250'], t_info['t_weapons_P250'] ,
             ct_info['ct_weapons_P2000'], t_info['t_weapons_P2000'], ct_info['ct_weapons_Tec-9'],
             t_info['t_weapons_Tec-9'], ct_info['ct_weapons_HE'], t_info['t_weapons_HE'],
             ct_info['ct_weapons_Flashbang'], t_info['t_weapons_Flashbang'], ct_info['ct_weapons_Smoke'],
             t_info['t_weapons_Smoke'], ct_info['ct_weapons_Incendiary'], t_info['t_weapons_Incendiary'],
             ct_info['ct_weapons_Molotov Cocktail'], t_info['t_weapons_Molotov Cocktail'], ct_info['ct_weapons_Decoy'],
             t_info['t_weapons_Decoy']]

    lst = lst_1
    return lst

#standard scaling the data
def scale_data(lst):
    x = pd.DataFrame(lst)
    print(x)
    scaler = StandardScaler()
    x_scale = scaler.fit_transform(scaler.fit_transform(x))
    x_scale_2 = list(np.concatenate(x_scale).flat)
    return x_scale_2

#model predition
def test_model(x_scale):
    model = load_model('models/predictor_v5.h5')
    x_data = np.array([x_scale], dtype=np.int32)

    my_pred = model.predict([x_data])

    if my_pred[0][0] <= 0.5:
        ans = 'Round Winner predicted : Counter-Terrorist'
    else:
        ans = "Round Winner predicted : Terrorist"

    print(my_pred)
    return ans




'''#Terrorrist
lst = [234, 65, 72, 234, 234, 45, 173, 40, 160, 24, 342, 0, 2, 0, 0, 2, 5, 5, 0, 0, 0, 0, 0, 0, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 1, 0, 0, 1, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5]
x_scale = scale_data(lst)
ans = test_model(x_scale)
print(ans)
'''


"""#cT
lst_2 = [114,	2,	0,	1,	0,	500,	500,	496,	500,	2200,	1000,	4,	5,	2,	5,	5,	0,	5,	0,	0,	1,	0,	0,	0,	0,	0,	0,	0,	1,	0,	0,	0,	0,	0,	0,	5,	0,	0,	0,	0,	2,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	1,	0,	0,	0,	0,	0,	0,	0,	0,	0,	4,	0,	0,	0,	1,	0,	0,	0,	1,	0,	4,	5,	4,	5,	2,	0,	0,	1,	0,	1]
x_scale = scale_data([lst_2])
print(x_scale)
ans = test_model(x_scale)
print(ans)
"""


'''#CT
lst = [	89,	6,	4,	3,	0,	500,	400,	491,	400,	2000,	550,	4,	4,	2,	5,	4,	0,	1,	0,	0,	1,	1,	0,	0,	0,	0,	0,	0,	1,	0,	0,	0,	0,	1,	0,	4,	0,	0,	1,	0,	2,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	1,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	5,	0,	0,	0,	0,	0,	0,	0,	2,	0,	3,	1,	4,	3,	1,	0,	0,	3,	0,	0]
x_scale = scale_data(lst)
print(x_scale)
ans = test_model(x_scale)
print(ans)
'''

