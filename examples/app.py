import os
import dotenv

from kard_private_api import Kard


dotenv.load_dotenv()

myKard = Kard(os.getenv('PHONE_NUMBER'))
myKard.authenticate(forceApiAuth=False)

print(
    myKard.karder.bankAccount.balance
)