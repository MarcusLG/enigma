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

    It should also handle the motion of the rotor and upon completion of the current
    iteration, it should move the rotor to the next position.
    """
    def __init__(self, rotor_type_list):
    	"""
        Parameters:
            rotor_type_list: The list includes the type of rotor the user would wish 
                             to use.
                             Example:
                             A 3-rotor system with the first rotor being, III, and I, and V
                             the input of the parameter should take the form ["III", "I", "V"]

        We then initialize an internal list (2D) to represent the rotor state and the number of 
        rotors.
    	"""
    	# pb_setting: Plug-board setting
        self.pb_setting = coreblocks.plug_internal()
        self.rtr_setting = []

    def plug_board_init(self, plugs_list):
        for element in plugs_list:
            self.pb_setting.connect_plug(element)