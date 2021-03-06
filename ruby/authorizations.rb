require 'finix'

Finix.configure(
    :root_url => 'https://finix.sandbox-payments-api.com',
    :user=>'USuJESezDxCrDtkDjLUxTJP1',
    :password => '347e1349-92b3-405a-bd3a-ecd9beb36ab4'
)

puts ""
identity = Finix::Identity.new(
    {
        "tags"=> {
            "Studio Rating"=> "4.7"
        },
        "entity"=> {
            "last_name"=> "Sunkhronos",
            "max_transaction_amount"=> 12000000,
            "has_accepted_credit_cards_previously"=> true,
            "default_statement_descriptor"=> "Lees Sandwiches",
            "personal_address"=> {
                "city"=> "San Mateo",
                "country"=> "USA",
                "region"=> "CA",
                "line2"=> "Apartment 7",
                "line1"=> "741 Douglass St",
                "postal_code"=> "94114"
            },
            "incorporation_date"=> {
                "year"=> 1978,
                "day"=> 27,
                "month"=> 6
            },
            "business_address"=> {
                "city"=> "San Mateo",
                "country"=> "USA",
                "region"=> "CA",
                "line2"=> "Apartment 8",
                "line1"=> "741 Douglass St",
                "postal_code"=> "94114"
            },
            "ownership_type"=> "PRIVATE",
            "first_name"=> "dwayne",
            "title"=> "CEO",
            "business_tax_id"=> "123456789",
            "doing_business_as"=> "Lees Sandwiches",
            "principal_percentage_ownership"=> 50,
            "email"=> "user@example.org",
            "mcc"=> "0742",
            "phone"=> "1234567890",
            "business_name"=> "Lees Sandwiches",
            "tax_id"=> "123456789",
            "business_type"=> "INDIVIDUAL_SOLE_PROPRIETORSHIP",
            "business_phone"=> "+1 (408) 756-4497",
            "dob"=> {
                "year"=> 1978,
                "day"=> 27,
                "month"=> 6
            },
            "url"=> "www.LeesSandwiches.com",
            "annual_card_volume"=> 12000000
        }
    }).save

puts "Merchant Identity"
puts identity

        bank_account = Finix::BankAccount.new(
            {
                "account_type"=> "SAVINGS",
                "name"=> "Fran Lemke",
                "tags"=> {
                    "Bank Account"=> "Company Account"
                },
                "country"=> "USA",
                "bank_code"=> "123123123",
                "account_number"=> "123123123",
                "type"=> "BANK_ACCOUNT",
                "identity"=> identity.id,
            }).save

puts "Merchant Bank Account"
puts bank_account

merchant = identity.provision_merchant

puts""
puts merchant


buyer = Finix::Identity.new(
    {
        "tags"=> {
            "key"=> "value"
        },
        "entity"=> {
            "phone"=> "7145677613",
            "first_name"=> "Ricardo",
            "last_name"=> "Sterling",
            "email"=> "therock@gmail.com",
            "personal_address"=> {
                "city"=> "San Mateo",
                "country"=> "USA",
                "region"=> "CA",
                "line2"=> "Apartment 7",
                "line1"=> "741 Douglass St",
                "postal_code"=> "94114"
            }
        }
    }).save

    puts""
    puts buyer

buyer.entity["first_name"] = "Michael"
buyer.save

puts ""
puts buyer

card = Finix::PaymentCard.new(
    {
        "name"=> "Steph Diaz",
        "expiration_year"=> 2020,
        "tags"=> {
            "card_name"=> "Business Card"
        },
        "number"=> "4895142232120006",
        "expiration_month"=> 3,
        "address"=> {
            "city"=> "San Francisco",
            "region"=> "CA",
            "postal_code"=> "94404",
            "line1"=> "900 Metro Center Blv",
            "country"=> "USA"
        },
        "security_code"=> "022",
        "type"=> "PAYMENT_CARD",
        "identity"=> buyer.id
    }).save

puts "Card:"
puts card


authorization = Finix::Authorization.new(
    {
        "source"=> card.id,
        "merchant_identity"=> merchant.identity,
        "tags"=> {
            "order_number"=> "21DFASJSAKAS"
        },
        "currency"=> "USD",
        "amount"=> 100,
        "processor"=> "DUMMY_V1"
    }).save

puts "Authorization: "
puts authorization
