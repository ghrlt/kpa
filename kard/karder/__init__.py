from . import cards
from . import family
from . import details
from . import subscription

def setup(kard):
    kard.cards = cards.KardCards(kard)
    kard.family = family.KardFamily(kard)
    kard.details = details.KardAccount(kard)
    kard.subscription = subscription.KardSubscription(kard)
    return kard
