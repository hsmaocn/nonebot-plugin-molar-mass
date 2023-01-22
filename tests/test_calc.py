from molar_mass_calc import calc


def test_calc():
    table = {
        'NaOH': 40,
        'H2SO4': 98,
        '2HCl': 73,
        '(NH4)2SO4': 132,
        'CuSO4+5H2O': 250,
    }

    for code, value in table.items():
        assert calc(code) == value
