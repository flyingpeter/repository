"""
Replace all Special Characters by utf-8 characters
"""

# Every special character is present in the string below will be searched and replaced for the equivalent
search_string = "ëėēèéêęūùúüûīïįìíîäåæªáãàâčçćñËĖĒÈÉÊĘŪÙÚÜÛĪÏĮÌÍÎÄÅÆÁÃÀÂČÇĆÑ"

# Simplified string with utf-8 charactes only
replace_string = "eeeeeeeuuuuuiiiiiiaaaaaaaacccnEEEEEEEUUUUUIIIIIIAAAAAAACCCN"

def replace(rx_string):
    """
    latin.replace(string to convert)
    """
    rx_string = list(rx_string)
    for index, letter in enumerate(rx_string):
        if search_string.find(letter) != -1:
            rx_string[index] = replace_string[search_string.find(letter)]
    rx_string = ''.join(rx_string)
    return rx_string
