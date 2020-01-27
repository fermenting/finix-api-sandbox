$payment_instrument = Finix::PaymentCard.new(
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
        "identity"=> $recipient_identity.id
    }).save

puts "Tokenized!"