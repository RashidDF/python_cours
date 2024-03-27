button_info = {
    'text': 'Buy',
}

button_style = {
    'color': 'yellow',
    'wight': 200,
    'height': 300,
}

# button = button_info | button_style

button = {
    **button_info,
    **button_style,
}

print(button)
print(button_info)
print(button_style)
