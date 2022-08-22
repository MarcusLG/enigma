""" 
This file contains the functions to implement the structure of
the encryption. 
"""

import coreblocks

class enig_single:
    """
    This class creates an object to take the input character, consider this as the
    object for one iteration of the enigma encryption based on the initial 
    state of the rotors setting as well as the movement of rotors for each character.
    """
    def __init__(self):
    	# pb_setting: Plug-board setting
        self.pb_setting = coreblocks.plug_internal()

    def plug_board_init(self, plugs_list):
        for element in plugs_list:
            self.pb_setting.connect_plug(element)