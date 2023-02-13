from . import details
from . import family
from . import subscription

def setup(kard):
    kard.details = details.KardAccount(kard)
    kard.family = family.KardFamily(kard)
    kard.subscription = subscription.KardSubscription(kard)
    return kard
