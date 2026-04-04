def add_settings(current_settings: dict, setting: tuple):
    key = str(setting[0]).lower()
    value = str(setting[1]).lower()
    
    if key.lower() in current_settings.keys():
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        current_settings.update({key: value})
        return f"Setting '{key}' added with value '{value}' successfully!"

test_settings = {
    'theme': 'dark',
    'notifications': 'enabled',
    'volume': 'high',
    'brightness': 75 
}