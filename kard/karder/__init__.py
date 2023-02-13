from . import bankAccount
from . import cards
from . import cashback
from . import details
from . import family
from . import offers
from . import subscription

def setup(kard):
    kard.bankAccount = bankAccount.KardBank(kard)
    kard.cards = cards.KardCards(kard)
    kard.cashback = cashback.KardCashback(kard)
    kard.cashback.offers = offers.KardOffers(kard)
    kard.details = details.KardAccount(kard)
    kard.family = family.KardFamily(kard)
    kard.subscription = subscription.KardSubscription(kard)
    
    return kard
