""" 
This file contains the functions to implement the structure of
the encryption. 
"""

import coreblocks
import enig_util

class enig_single:
    """
    This class creates an object to take the input character, consider this as the
    object for one iteration of the enigma encryption based on the initial 
    state of the rotors setting as well as the movement of rotors for each character.

    It should also handle the motion of the rotor and upon completion of the current
    iteration, it should move the rotor to the next position.
    """
    def __init__(self, rotor_type_list, rotor_starting_pos, plugs_list):
        """
        Parameters:
            rotor_type_list:    The list includes the type of rotor the user would wish 
                                to use.
                                Example:
                                A 3-rotor system with the first rotor being, III, and I, and V
                                the input of the parameter should take the form ["III", "I", "V"]
            rotor_starting_pos: 
            plugs_list:         The list includes all the characters to be connected on the virtual
                                plug board.
                                Example:
                                The user wishes to connect the following pairs of characters:
                                AZ, BO, HM
                                The parameter will take the form ["AZ", "BO", "HM"]
        We then initialize an internal list (2D) to represent the rotor state and the number of 
        rotors.
        pb_setting:   Plug-board setting
        rtr_setting:  Rotors setting
        rflt_setting: Reflector setting
        """
        self.pb_setting = coreblocks.plug_internal()
        self.rtr_setting = []
        self.rflt_setting = []

        # Here we perform the plug-board initialization:
        self.plug_board_init(plugs_list)
        self.rotors_construct(rotor_type_list, rotor_starting_pos)

    def plug_board_init(self, plugs_list):
        """
        Parameters:
            plugs_list: Passed from initializer, see __init__ for details.
        This function takes the plugs_list, for each pair of characters to be connected, swap
        the positions in the plug-board character list.
        """
        for element in plugs_list:
            self.pb_setting.connect_plug(element)

    def rotors_construct(self, rotor_type_list, rotor_starting_pos):
        """
        Parameters:
            rotor_type_list:    Passed from initializer, see __init__ for details.
            rotor_starting_pos: Passed from initializer, see __init__ for details.
        This function takes the rotor_type_list and rotor_starting_pos and build the rotors set.
        """
        rotor_obj = coreblocks.rotor()
        for i in range (0, len(rotor_type_list)):
            curr_type = rotor_obj.rotor_selector(rotor_type_list[i])
            curr_offset = enig_util.rotate(rotor_obj.calc_offset_distance(curr_type), rotor_starting_pos[i])
            self.rtr_setting.append(curr_offset)

    def encryp_char(self, curr_char):
        """
        Parameter:
            curr_char: Current character to be encrypted.
        Main wrapper to pass the character for encryption and handle the current and next state of
        the machine.
        """


        
