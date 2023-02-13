from . import cards
from . import family
from . import details
from . import bankAccount
from . import subscription

def setup(kard):
    kard.cards = cards.KardCards(kard)
    kard.family = family.KardFamily(kard)
    kard.details = details.KardAccount(kard)
    kard.bankAccount = bankAccount.KardBank(kard)
    kard.subscription = subscription.KardSubscription(kard)
    return kard
