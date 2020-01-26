require 'finix'

Finix.configure(
    :root_url => 'https://finix.sandbox-payments-api.com',
    :user=>'USuJESezDxCrDtkDjLUxTJP1',
    :password => '347e1349-92b3-405a-bd3a-ecd9beb36ab4'
)

identity = Finix::Identity.new(
    {
        "tags"=> {
            "key"=> "value"
        },
        "entity"=> {
            "phone"=> "7145677612",
            "first_name"=> "Steph",
            "last_name"=> "White",
            "email"=> "Steph@gmail.com",
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

    puts "identity:"
puts identity
puts "\n\n"

card = Finix::PaymentCard.new(
    {
        "name"=> "Amy White",
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
        "identity"=> identity.id
    }).save

    puts "card:"
puts card 
puts "\n\n"

push_to_card_eligible_url = "https://finix.sandbox-payments-api.com/payment_instruments/:"+ card.id + "/verifications"

puts push_to_card_eligible_url
puts card["_links"]
# .verifications.href



