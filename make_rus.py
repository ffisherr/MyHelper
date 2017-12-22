def make_rus_stat(stat):
    if stat=='Rain':
        return'Идет дождь'
    elif stat=='Snow':
        return'Идет снег'
    elif stat=='Clear':
        return 'Ясно'
    elif stat=='Clouds':
        return 'Облачно'
    elif stat=='Misty':
        return 'Туманно'
    elif stat=='Mist':
        return 'Туман'
    elif stat=='Fog':
        return 'Дымка'
    else:
        return 'Error: %s' %stat