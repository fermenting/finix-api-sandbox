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