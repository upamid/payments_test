import json 
import random
from random import randint, uniform

periods = 12
accounts = 3
bill_list = []

i = 0
for account in range(accounts):
    for period in range(periods):
        bill_list.append( 
            {
                "model": "bill.bill",
                "pk": i,
                "fields": {
                    "account_id": account,
                    "period_id": period
                }
            })
        i += 1

json_string = json.dumps(bill_list)

with open('json_bill.json', 'w') as outfile:
    outfile.write(json_string)


bill_det_list = []

i = 0
for bill in range(len(bill_list)):
    for bill_det in range(5):
        bill_det_list.append( 
        {
            "model": "bill.bill_det",
            "pk": i,
            "fields": {
                "bill_id": bill,
                "service_id": randint(0, 9),
                "value": round(uniform(0.00, 4000.00),2)
            }
        })
        i += 1

print(bill_det_list)

json_string = json.dumps(bill_det_list)

with open('json_bill_det.json', 'w') as outfile:
    outfile.write(json_string)

payments_list = []
i = 0

for payment in range(2):
    for account in range(accounts):
        for period in range(periods):
            payments_list.append( 
            {
                "model": "bill.payment",
                "pk": i,
                "fields": {
                    "account_id": account,
                    "period_id": period,
                    "value": round(uniform(0.00, 4000.00),2)
                }
            })
            i += 1

json_string = json.dumps(payments_list)

with open('json_payment.json', 'w') as outfile:
    outfile.write(json_string)
