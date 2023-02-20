import os
import json
import dotenv

from kard_private_api import Kard


dotenv.load_dotenv()

myKard = Kard(os.getenv('PHONE_NUMBER') or input('Phone number: '))
myKard.authenticate(forceApiAuth=False)

def writeDataToFiles():
    transactions = myKard.karder.transactions.getAll()
    data = {
        "categories": {},
        "merchants": {},
        "withCashback": [],
        "mobilePaymentProviders": {},
        "amounts": []
    }
    with open('transactions.json', 'w', encoding='utf-8') as f:
        json.dump(transactions, f, indent=4, ensure_ascii=False)

    for transaction in transactions:
        # Count only card transactions AND only paiements
        if transaction['__typename'] == 'CardTransaction' and transaction['amount']['value'] < 0:
            if transaction['category']:
                if transaction['category']['name'] not in data['categories']:
                    data['categories'][transaction['category']['name']] = []
                data['categories'][transaction['category']['name']].append(transaction['amount'])

            if transaction['title'] not in data['merchants']:
                data['merchants'][transaction['title']] = []
            data['merchants'][transaction['title']].append(transaction['amount'])

            if transaction['cashback']:
                data['withCashback'].append(transaction['amount'])

            if transaction['mobilePaymentProvider'] not in data['mobilePaymentProviders']:
                data['mobilePaymentProviders'][transaction['mobilePaymentProvider']] = []
            data['mobilePaymentProviders'][transaction['mobilePaymentProvider']].append(transaction['amount'])

            data['amounts'].append(transaction['amount'])

    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


writeDataToFiles() # Comment this line if you don't want/need to overwrite the data

with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print('Spent by categories:')
for category in data['categories']:
    eur = [abs(x['value']) for x in data['categories'][category]]

    print('\t', category)
    print('\t\tTotal: ', sum(eur))
    print('\t\tAverage: ', sum(eur) / len(eur))
    print('\t\tMax: ', max(eur))
    print('\t\tMin: ', min(eur))
    print('\t\tCount: ', len(eur))
    print()

print('Spent by merchants:')
for merchant in data['merchants']:
    eur = [abs(x['value']) for x in data['merchants'][merchant]]
    if len(eur) == 1:
        print('\t', merchant, ' - ', eur[0])
        continue

    print('\t', merchant)
    print('\t\tTotal: ', sum(eur))
    print('\t\tAverage: ', sum(eur) / len(eur))
    print('\t\tMax: ', max(eur))
    print('\t\tMin: ', min(eur))
    print('\t\tCount: ', len(eur))
    print()

print('Spent by mobile payment providers:')
for provider in data['mobilePaymentProviders']:
    eur = [abs(x['value']) for x in data['mobilePaymentProviders'][provider]]

    print('\t', provider)
    print('\t\tTotal: ', sum(eur))
    print('\t\tAverage: ', sum(eur) / len(eur))
    print('\t\tMax: ', max(eur))
    print('\t\tMin: ', min(eur))
    print('\t\tCount: ', len(eur))
    print()


eur = [abs(x['value']) for x in data['amounts']]
print('Total spent: ', sum(eur))
print('Average spent: ', sum(eur) / len(eur))
print('Max spent: ', max(eur))
print('Min spent: ', min(eur))
print('Count: ', len(eur))
print('Count with cashback: ', len(data['withCashback']))

