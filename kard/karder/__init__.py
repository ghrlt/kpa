from . import bankAccount
from . import cards
from . import cashback
from . import details
from . import family
from . import kyc
from . import offers
from . import subscription
from . import vaults
from . import vault

def setup(kard):
    kard.bankAccount = bankAccount.KardBank(kard)
    kard.cards = cards.KardCards(kard)
    kard.cashback = cashback.KardCashback(kard)
    kard.cashback.offers = offers.KardOffers(kard)
    kard.details = details.KardAccount(kard)
    kard.family = family.KardFamily(kard)
    kard.kyc = kyc.KardKYC(kard)
    kard.subscription = subscription.KardSubscription(kard)
    kard.vaults = vaults.KardVaults(kard)
    kard.vaults.vault = vault.KardVault(kard)

    return kard
