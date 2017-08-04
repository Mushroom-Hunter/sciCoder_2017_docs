# The class "Spectrum" is located in the file "spectrum.py".
# Normally, you'd have to import it as:
#
# from SDSSSpec.spectrum import Spectrum
#
# or use it as:
#
# import SDSSSpec.spectrum
# s = SDSSSpec.Spectrum
#
# We don't want the use to have to know which file the class is
# defined in, so we can pull it into the top level with the following line.
# Now we can do:
#
# from SESSSpec import Spectrum
#
from .spectrum import Spectrum

# Reference: https://stackoverflow.com/a/64130/2712652
# If "__all__" is defined, it specifies what is imported
# when you type:
#
# from SDSSSpec import *
#
# If something else were defined here but not listed in
# __all__, it won't be imported with "*" so is "hidden".
# (Things aren't really hidden though if you do know where
# they are defined.)
#

__all__ = ['Spectrum']
