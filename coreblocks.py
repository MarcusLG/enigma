""" 
This file contains both the rotor and plug-board classes.
Reference: https://en.wikipedia.org/wiki/Enigma_rotor_details
"""

class rotor:
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
        self.order_def   = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        self.IC          = ['D','M','T','W','S','I','L','R','U','Y','Q','N','K','F','E','J','C','A','Z','B','P','G','X','O','H','V']
        self.IIC         = ['H','Q','Z','G','P','J','T','M','O','B','L','N','C','I','F','D','Y','A','W','V','E','U','S','R','K','X']
        self.IIIC        = ['U','Q','N','T','L','S','Z','F','M','R','E','H','D','P','X','K','I','B','V','Y','G','J','C','W','O','A']
        self.I           = ['J','G','D','Q','O','X','U','S','C','A','M','I','F','R','V','T','P','N','E','W','K','B','L','Z','Y','H']
        self.II          = ['N','T','Z','P','S','F','B','O','K','M','W','R','C','J','D','I','V','L','A','E','Y','U','X','H','G','Q']
        self.III         = ['J','V','I','U','B','H','T','C','D','Y','A','K','E','Q','Z','P','O','S','G','X','N','R','M','W','F','L']
        self.UKW         = ['Q','Y','H','O','G','N','E','C','V','P','U','Z','T','F','D','J','A','X','W','M','K','I','S','R','B','L']
        self.ETW         = ['Q','W','E','R','T','Z','U','I','O','A','S','D','F','G','H','J','K','P','Y','X','C','V','B','N','M','L']
        self.I_K         = ['P','E','Z','U','O','H','X','S','C','V','F','M','T','B','G','L','R','I','N','Q','J','W','A','Y','D','K']
        self.II_K        = ['Z','O','U','E','S','Y','D','K','F','W','P','C','I','Q','X','H','M','V','B','L','G','N','J','R','A','T']
        self.III_K       = ['E','H','R','V','X','G','A','O','B','Q','U','S','I','M','Z','F','L','Y','N','W','K','T','P','D','J','C']
        self.UKW_K       = ['I','M','E','T','C','G','F','R','A','Y','S','Q','B','Z','X','W','L','H','K','D','V','U','P','O','J','N']
        self.ETW_K       = ['Q','W','E','R','T','Z','U','I','O','A','S','D','F','G','H','J','K','P','Y','X','C','V','B','N','M','L']
        self.I           = ['E','K','M','F','L','G','D','Q','V','Z','N','T','O','W','Y','H','X','U','S','P','A','I','B','R','C','J']
        self.II          = ['A','J','D','K','S','I','R','U','X','B','L','H','W','T','M','C','Q','G','Z','N','P','Y','F','V','O','E']
        self.III         = ['B','D','F','H','J','L','C','P','R','T','X','V','Z','N','Y','E','I','W','G','A','K','M','U','S','Q','O']
        self.IV          = ['E','S','O','V','P','Z','J','A','Y','Q','U','I','R','H','X','L','N','F','T','G','K','D','C','M','W','B']
        self.V           = ['V','Z','B','R','G','I','T','Y','U','P','S','D','N','H','L','X','A','W','M','J','Q','O','F','E','C','K']
        self.VI          = ['J','P','G','V','O','U','M','F','Y','Q','B','E','N','H','Z','R','D','K','A','S','X','L','I','C','T','W']
        self.VII         = ['N','Z','J','H','G','R','C','X','M','Y','S','W','B','O','U','F','A','I','V','L','P','E','K','Q','D','T']
        self.VIII        = ['F','K','Q','H','T','L','X','O','C','B','J','S','P','D','Z','R','A','M','E','W','N','I','U','Y','G','V']
        self.beta        = ['L','E','Y','J','V','C','N','I','X','W','P','B','Q','M','D','R','T','A','K','Z','G','F','U','H','O','S']
        self.gamma       = ['F','S','O','K','A','N','U','E','R','H','M','B','T','I','Y','C','W','L','Q','P','Z','X','V','G','J','D']
        self.reflector_a = ['E','J','M','Z','A','L','Y','X','V','B','W','F','C','R','Q','U','O','N','T','S','P','I','K','H','G','D']
        self.reflector_b = ['Y','R','U','H','Q','S','L','D','P','X','N','G','O','K','M','I','E','B','F','Z','C','W','V','J','A','T']
        self.reflector_c = ['F','V','P','J','I','A','O','Y','E','D','R','Z','X','W','G','C','T','K','U','Q','S','B','N','M','H','L']
        self.reflector_b_thin = ['E','N','K','Q','A','U','Y','W','J','I','C','O','P','B','L','M','D','X','Z','V','F','T','H','R','G','S']
        self.reflector_c_thin = ['R','D','O','B','J','N','T','K','V','E','H','M','L','F','C','W','Z','A','X','G','Y','I','P','S','U','Q']