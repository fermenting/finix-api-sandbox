import finix

from finix.config import configure
from finix.resources import BankAccount, Merchant, PaymentCard, Authorization


configure(root_url="https://finix.sandbox-payments-api.com", auth=("USuJESezDxCrDtkDjLUxTJP1", "347e1349-92b3-405a-bd3a-ecd9beb36ab4"))

from finix.resources import Identity

merchant_identity = Identity(**
    {
        "tags": {
            "Studio Rating": "4.7"
        },
        "entity": {
            "last_name": "Sunkhronos",
            "max_transaction_amount": 12000000,
            "has_accepted_credit_cards_previously": True,
            "default_statement_descriptor": "Lees Sandwiches",
            "personal_address": {
                "city": "San Mateo",
                "country": "USA",
                "region": "CA",
                "line2": "Apartment 7",
                "line1": "741 Douglass St",
                "postal_code": "94114"
            },
            "incorporation_date": {
                "year": 1978,
                "day": 27,
                "month": 6
            },
            "business_address": {
                "city": "San Mateo",
                "country": "USA",
                "region": "CA",
                "line2": "Apartment 8",
                "line1": "741 Douglass St",
                "postal_code": "94114"
            },
            "ownership_type": "PRIVATE",
            "first_name": "dwayne",
            "title": "CEO",
            "business_tax_id": "123456789",
            "doing_business_as": "Lees Sandwiches",
            "principal_percentage_ownership": 50,
            "email": "user@example.org",
            "mcc": "0742",
            "phone": "1234567890",
            "business_name": "Namey",
            "tax_id": "123456789",
            "business_type": "INDIVIDUAL_SOLE_PROPRIETORSHIP",
            "business_phone": "+1 (408) 756-4497",
            "dob": {
                "year": 1978,
                "day": 27,
                "month": 6
            },
            "url": "www.LeesSandwiches.com",
            "annual_card_volume": 12000000
        }
    }).save()






# print("\n")
print (merchant_identity)
# print (merchant_identity.tags['Studio Rating'])
# print("\n")
# print (merchant_identity.entity['business_address']['city'])
# print(merchant_identity.disputes)

bank_account = BankAccount(**
    {
        "account_type": "SAVINGS",
        "name": "Fran Lemke",
        "tags": {
            "Bank Account": "Company Account"
        },
        "country": "USA",
        "bank_code": "123123123",
        "account_number": "123123123",
        "type": "BANK_ACCOUNT",
        "identity": merchant_identity.id
    }).save()

print (bank_account.identity)

# merchant = merchant_identity.provision_merchant_on(Merchant())
# print (merchant)
# print (merchant.onboarding_state)


# buyer_identity = Identity(**
    # {
    #     "tags": {
    #         "key": "value"
    #     },
    #     "entity": {
    #         "phone": "7145677613",
    #         "first_name": "Ricardo",
    #         "last_name": "Sterling",
    #         "email": "therock@gmail.com",
    #         "personal_address": {
    #             "city": "San Mateo",
    #             "country": "USA",
    #             "region": "CA",
    #             "line2": "Apartment 7",
    #             "line1": "741 Douglass St",
    #             "postal_code": "94114"
    #         }
    #     }
    # }).save()

# print (buyer_identity.entity['personal_address']["line2"])
# print(buyer_identity.id)
# print(buyer_identity.updated_at)


# card = PaymentCard(**
    # {
    #     "name": "Steph Diaz",
    #     "expiration_year": 2020,
    #     "tags": {
    #         "card_name": "Business Card"
    #     },
    #     "number": "4895142232120006",
    #     "expiration_month": 3,
    #     "address": {
    #         "city": "San Francisco",
    #         "region": "CA",
    #         "postal_code": "94404",
    #         "line1": "900 Metro Center Blv",
    #         "country": "USA"
    #     },
    #     "security_code": "022",
    #     "type": "PAYMENT_CARD",
    #     "identity": buyer_identity.id
    # }).save()

# print (card)

# To create an Authorization we’ll 
# supply the buyer’s Payment Instrument ID as the source field and the 
# seller’s Identity ID in the merchant_identity field. 
# Note that the amount field is in cents.

# authorization = Authorization(**
    # {
    #     "source": card.id,
    #     "merchant_identity": merchant_identity.id,
    #     "tags": {
    #         "order_number": "21DFASJSAKAS"
    #     },
    #     "currency": "USD",
    #     "amount": 100,
    #     "processor": "DUMMY_V1"
    # }).save()

# print (authorization.transfer)
# authorization = Authorization.get(id=authorization.id)
# authorization.capture(**
#     {
#         "fee": "10",
#         "capture_amount": 100
#     })

# print (authorization.transfer)



print("\n")