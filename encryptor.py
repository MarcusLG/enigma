"""
This file contains the functions to implement the structure of
the encryption.
"""

import coreblocks
import enig_util

class EnigSingle:
    """
    This class creates an object to take the input character, consider this as the
    object for one iteration of the enigma encryption based on the initial
    state of the rotors setting as well as the movement of rotors for each character.

    It should also handle the motion of the rotor and upon completion of the current
    iteration, it should move the rotor to the next position.
    """
    def __init__(self, rotor_type_list, rotor_starting_pos, reflector_type, plugs_list):
        """
        Parameters:
            rotor_type_list:    The list includes the type of rotor the user would wish
                                to use.
                                Example:
                                A 3-rotor system with the first rotor being, III, and I, and V
                                the input of the parameter should take the form ["III", "I", "V"]
            rotor_starting_pos:
            reflector_type:
                                Similar format as rotor_type_list, though not a list as there should
                                only be one reflector
            plugs_list:         The list includes all the characters to be connected on the virtual
                                plug board.
                                Example:
                                The user wishes to connect the following pairs of characters:
                                AZ, BO, HM
                                The parameter will take the form ["AZ", "BO", "HM"]
        We then initialize an internal list (2D) to represent the rotor state and the number of
        rotors.
        pb_setting:   Plug-board setting
        rtr_offsets:  Rotors setting
        rtr_mappings: Rotors actual mapping (aka, the characters)
        rflt_setting: Reflector setting
        """
        self.pb_setting = coreblocks.PlugInternal()
        self.rtr_offsets = []
        self.rtr_mappings = []
        self.rflt_offset = []
        self.rflt_mapping = []
        self.global_debug = False
        self.rotor_obj = coreblocks.Rotor()

        # Here we perform the plug-board initialization:
        self.plug_board_init(plugs_list)
        self.rotors_construct(rotor_type_list, rotor_starting_pos)
        self.reflector_construct(reflector_type)

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
        for count, element in enumerate(rotor_type_list):
            curr_type = self.rotor_obj.rotor_selector(element)
            curr_offset = enig_util.rotate(self.rotor_obj.calc_offset_distance(curr_type),
                                           rotor_starting_pos[count])
            self.rtr_offsets.append(curr_offset)
            self.rtr_mappings.append(enig_util.rotate(curr_type, rotor_starting_pos[count]))

    def reflector_construct(self,reflector_type):
        """
        Parameters:
            reflector_type:    Passed from initializer, see __init__ for details.
        Works similarly to rotors_construct, but for reflectors
        """
        self.rflt_mapping = self.rotor_obj.rotor_selector(reflector_type)
        self.rflt_offset = self.rotor_obj.calc_offset_distance(self.rflt_mapping)

    def set_debug_mode(self, debug_mode):
        """
        A simple function to toggle the internal debug_mode token
        """
        print('Variable global_debug set %s' % (debug_mode))
        self.global_debug = debug_mode

    def rotor_reflector_op(self, char_input, lst_offset):
        """
        Function to perform the basic IO of a rotor and the flector
        """
        temp_idx = self.rotor_obj.order_def.index(char_input)
        temp_idx = temp_idx + lst_offset[temp_idx]
        temp_idx = temp_idx if temp_idx < 26  else temp_idx - 26
        char_output = self.rotor_obj.order_def[temp_idx]
        return char_output

    def encryp_char(self, curr_char):
        """
        Parameter:
            curr_char: Current character to be encrypted.
        Main wrapper to pass the character for encryption and handle the current and next state of
        the machine.
        """

        # Step 1: Pass through plug-board
        #         Here we find the position of the input char in the alphabet order, then
        #         find the corresponding character with the plugboard settings.
        char_pbout = self.pb_setting.mapping_list[self.pb_setting.base_list.index(curr_char)]

        # Step 2: Pass through the rotor
        char_rtrout = char_pbout
        for count,element in enumerate(self.rtr_offsets):
        #for element in self.rtr_offsets: Note: Masked out not using element iter
            # For each rotor, we run the same procedure

            # Step I: Get the index for the input
            char_rtrout = self.rotor_reflector_op(char_rtrout, element)
            if self.global_debug:
                print("Current char_rtrout:\t", char_rtrout)

        # Step 3: Pass through the reflector
        char_rfltout = self.rotor_reflector_op(char_rtrout, self.rflt_offset)
        if self.global_debug:
            print("Current char_rtrout:\t", char_rfltout)

        # Step 3: Rotate the position
