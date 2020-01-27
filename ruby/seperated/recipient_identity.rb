$recipient_identity = Finix::Identity.new(
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