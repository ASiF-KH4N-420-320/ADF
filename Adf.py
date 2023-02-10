import os, platform

def Run():

        bit = platform.architecture()[0]

        if bit == '64bit':

            import ADF

        elif bit == '32bit':

            import ADF

Run()
