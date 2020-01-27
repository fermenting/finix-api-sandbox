$authorization = Finix::Authorization.new(
    {
        "source"=> $card.id,
        "merchant_identity"=> $merchant.identity,
        "tags"=> {
            "order_number"=> "21DFASJSAKAS"
        },
        "currency"=> "USD",
        "amount"=> 100,
        "processor"=> "DUMMY_V1"
    }).save

    puts "Authorized!"