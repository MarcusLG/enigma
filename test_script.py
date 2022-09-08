"""
Generic moved-command-line to file test script
"""

from encryptor import *

x = EnigSingle(["III","II"],[0,24],["AZ"])
x.set_debug_mode(True)
x.encryp_char('A')
