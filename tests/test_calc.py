from nonebot_plugin_molar_mass.calc import calc


table = {
    'NaOH': 40,
    'H2SO4': 98,
    '2HCl': 73,
    '(NH4)2SO4': 132,
    'CuSO4+5H2O': 250,
}


def test_calc():
    for chemical, value in table.items():
        assert calc(chemical) == value
