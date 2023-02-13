from . import details
from . import family

def setup(kard):
    kard.details = details.KardAccount(kard)
    kard.family = family.KardFamily(kard)
    return kard
