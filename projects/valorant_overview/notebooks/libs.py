def cprint(text, color, **kwargs):
    color_number = None

    if color == 'blue':
        color_number = 34
    elif color == 'green':
        color_number = 32
    elif color == 'red':
        color_number = 31
    elif color == 'yellow':
        color_number = 33
    elif color == 'purple':
        color_number = 35
    elif color == 'cyan':
        color_number = 36
    else:
        color_number = 37

    print(f'\033[{color_number}m{text}\033[0m', **kwargs)
