$buyer_identity = Finix::Identity.new(
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

    puts "Buyer Identity Created!"