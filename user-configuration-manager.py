def add_setting(current_settings: dict, setting: tuple):
    key = str(setting[0]).lower()
    value = str(setting[1]).lower()
    
    if key in current_settings.keys():
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        current_settings.update({key: value})
        return f"Setting '{key}' added with value '{value}' successfully!"
    
def update_setting(current_settings: dict, setting: tuple):
    key = str(setting[0]).lower()
    value = str(setting[1]).lower()

    if key in current_settings.keys():
        current_settings.update({key: value})
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."
    
def delete_setting(current_settings: dict, key: str):
    key = key.lower()

    if key in current_settings.keys():
        current_settings.pop(key)
        return f"Setting '{key}' deleted successfully!"
    else:
        return "Setting not found!"
    
def view_settings(current_settings: dict):
    full_settings = "Current User Settings:\n"

    if current_settings == {}:
        return "No settings available."
    else:
        for key, value in current_settings.items():
            full_settings += key.capitalize() + ": " + str(value) + "\n"
        return full_settings

test_settings = {
    'theme': 'dark',
    'notifications': 'enabled',
    'volume': 'high',
    'brightness': 75 
}