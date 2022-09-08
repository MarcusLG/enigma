"""
This file contains both the rotor and plug-board classes.
Reference: https://en.wikipedia.org/wiki/Enigma_rotor_details
"""

class Rotor:
    """
    This is the main rotor class to create the individual rotor to be inserted.
    Depending on the number of rotor, multiple rotor objects can be created to
    accomodate that.
    """
    def __init__(self):
        # Here we encode the different rotor configuration
        # Refer to Reference for details
        # Note: Now after realising there are so many rotors configuration,
        # probably is not a wise idea to initialize everything at one go.
        self.order_def   = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N',
                            'O','P','Q','R','S','T','U','V','W','X','Y','Z']
        self.ic          = ['D','M','T','W','S','I','L','R','U','Y','Q','N','K','F',
                            'E','J','C','A','Z','B','P','G','X','O','H','V']
        self.iic         = ['H','Q','Z','G','P','J','T','M','O','B','L','N','C','I',
                            'F','D','Y','A','W','V','E','U','S','R','K','X']
        self.iiic        = ['U','Q','N','T','L','S','Z','F','M','R','E','H','D','P',
                            'X','K','I','B','V','Y','G','J','C','W','O','A']
        # Before we figured out the documentation page, comment these sets out for now.
        #self.i           = ['J','G','D','Q','O','X','U','S','C','A','M','I','F','R',
        #                   'V','T','P','N','E','W','K','B','L','Z','Y','H']
        #self.i          = ['N','T','Z','P','S','F','B','O','K','M','W','R','C','J',
        #                    'D','I','V','L','A','E','Y','U','X','H','G','Q']
        #self.iii         = ['J','V','I','U','B','H','T','C','D','Y','A','K','E','Q',
        #                    'Z','P','O','S','G','X','N','R','M','W','F','L']
        self.ukw         = ['Q','Y','H','O','G','N','E','C','V','P','U','Z','T','F',
                            'D','J','A','X','W','M','K','I','S','R','B','L']
        self.etw         = ['Q','W','E','R','T','Z','U','I','O','A','S','D','F','G',
                            'H','J','K','P','Y','X','C','V','B','N','M','L']
        self.i_k         = ['P','E','Z','U','O','H','X','S','C','V','F','M','T','B',
                            'G','L','R','I','N','Q','J','W','A','Y','D','K']
        self.ii_k        = ['Z','O','U','E','S','Y','D','K','F','W','P','C','I','Q',
                            'X','H','M','V','B','L','G','N','J','R','A','T']
        self.iii_k       = ['E','H','R','V','X','G','A','O','B','Q','U','S','I','M',
                            'Z','F','L','Y','N','W','K','T','P','D','J','C']
        self.ukw_k       = ['I','M','E','T','C','G','F','R','A','Y','S','Q','B','Z',
                            'X','W','L','H','K','D','V','U','P','O','J','N']
        self.etw_k       = ['Q','W','E','R','T','Z','U','I','O','A','S','D','F','G',
                            'H','J','K','P','Y','X','C','V','B','N','M','L']
        self.i           = ['E','K','M','F','L','G','D','Q','V','Z','N','T','O','W',
                            'Y','H','X','U','S','P','A','I','B','R','C','J']
        self.ii          = ['A','J','D','K','S','I','R','U','X','B','L','H','W','T',
                            'M','C','Q','G','Z','N','P','Y','F','V','O','E']
        self.iii         = ['B','D','F','H','J','L','C','P','R','T','X','V','Z','N',
                            'Y','E','I','W','G','A','K','M','U','S','Q','O']
        self.iv          = ['E','S','O','V','P','Z','J','A','Y','Q','U','I','R','H',
                            'X','L','N','F','T','G','K','D','C','M','W','B']
        self.v           = ['V','Z','B','R','G','I','T','Y','U','P','S','D','N','H',
                            'L','X','A','W','M','J','Q','O','F','E','C','K']
        self.vi          = ['J','P','G','V','O','U','M','F','Y','Q','B','E','N','H',
                            'Z','R','D','K','A','S','X','L','I','C','T','W']
        self.vii         = ['N','Z','J','H','G','R','C','X','M','Y','S','W','B','O',
                            'U','F','A','I','V','L','P','E','K','Q','D','T']
        self.viii        = ['F','K','Q','H','T','L','X','O','C','B','J','S','P','D',
                            'Z','R','A','M','E','W','N','I','U','Y','G','V']
        self.beta        = ['L','E','Y','J','V','C','N','I','X','W','P','B','Q','M',
                            'D','R','T','A','K','Z','G','F','U','H','O','S']
        self.gamma       = ['F','S','O','K','A','N','U','E','R','H','M','B','T','I',
                            'Y','C','W','L','Q','P','Z','X','V','G','J','D']
        self.reflector_a = ['E','J','M','Z','A','L','Y','X','V','B','W','F','C','R',
                            'Q','U','O','N','T','S','P','I','K','H','G','D']
        self.reflector_b = ['Y','R','U','H','Q','S','L','D','P','X','N','G','O','K',
                            'M','I','E','B','F','Z','C','W','V','J','A','T']
        self.reflector_c = ['F','V','P','J','I','A','O','Y','E','D','R','Z','X','W',
                            'G','C','T','K','U','Q','S','B','N','M','H','L']
        self.reflector_b_thin = ['E','N','K','Q','A','U','Y','W','J','I','C','O','P',
                            'B','L','M','D','X','Z','V','F','T','H','R','G','S']
        self.reflector_c_thin = ['R','D','O','B','J','N','T','K','V','E','H','M','L',
                            'F','C','W','Z','A','X','G','Y','I','P','S','U','Q']

    def calc_offset_distance(self, detail_list):
        """
        This is the function to generate the relative offset between each side of a rotor
        (i.e. the internal wiring)
        """
        return [self.order_def.index(detail_list[i]) - i for i in range(0, len(detail_list))]

    def rotor_selector(self, rotor_sel):
        """
        This functions will be the selector for the rotor based on user input

        Parameter:
            rotor_sel: The selector text, should make the class parameter definition
        """
        if rotor_sel == "IC":
            return self.ic
        if rotor_sel == "IIC":
            return self.iic
        if rotor_sel == "IIIC":
            return self.iiic
        if rotor_sel == "IIC":
            return self.iic
        if rotor_sel == "IIIC":
            return self.iiic
        if rotor_sel == "IIC":
            return self.iic
        if rotor_sel == "IIIC":
            return self.iiic
        if rotor_sel == "UKW":
            return self.ukw
        if rotor_sel == "ETW":
            return self.etw
        if rotor_sel == "I_K":
            return self.i_k
        if rotor_sel == "II_K":
            return self.ii_k
        if rotor_sel == "III_K":
            return self.iii_k
        if rotor_sel == "UKW_K":
            return self.ukw_k
        if rotor_sel == "ETW_K":
            return self.etw_k
        if rotor_sel == "I":
            return self.i
        if rotor_sel == "II":
            return self.ii
        if rotor_sel == "III":
            return self.iii
        if rotor_sel == "IV":
            return self.iv
        if rotor_sel == "V":
            return self.v
        if rotor_sel == "VI":
            return self.vi
        if rotor_sel == "VII":
            return self.vii
        if rotor_sel == "VIII":
            return self.viii
        if rotor_sel == "beta":
            return self.beta
        if rotor_sel == "gamma":
            return self.gamma
        if rotor_sel == "reflector_a":
            return self.reflector_a
        if rotor_sel == "reflector_b":
            return self.reflector_b
        if rotor_sel == "reflector_c":
            return self.reflector_c
        if rotor_sel == "reflector_b_thin":
            return self.reflector_b_thin
        if rotor_sel == "reflector_c_thin":
            return self.reflector_c_thin

class PlugInternal:
    """
    This is the main plug-board class to create the substitution of character
    as was served by the plug board
    """
    def __init__(self):
        # Here we create a base list for the character, then each character can
        # be switched-places with another character.
        self.base_list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N',
                          'O','P','Q','R','S','T','U','V','W','X','Y','Z']
        self.mapping_list = self.base_list.copy()

    def connect_plug(self, plugs):
        """
        Example:
        _________________________________________
        |                                       |
        |   A  B  C  D  E  F  G  H  I  J        |
        |  /                                    |
        | | K  L  M  N  O  P  Q  R  S  T        |
        | |                                     |
        | | U  V  W  X  Y  Z                    |
        | _________________|                    |
        |_______________________________________|
        Plugging A to Z shall make "plugs" to come in the form "BZ"
        Here we split BZ into constituent character and swap the position
        in the base list, this could be repeated as many times depending
        on the number of plugs-wire to be connected.
        """

        # Potentially in the future we will add a safeguard on this,
        # now just leave it to wrapper to make sure the variable is
        # limited to 2 characters.
        pos_a = list(plugs)[0]
        pos_b = list(plugs)[1]
        a, b = self.mapping_list.index(pos_a), self.mapping_list.index(pos_b)
        self.mapping_list[b], self.mapping_list[a] = self.mapping_list[a], self.mapping_list[b]
        