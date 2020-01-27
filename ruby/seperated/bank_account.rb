# require_relative 

$bank_account = Finix::BankAccount.new(
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
    "identity"=> $merchant.id
}).save

puts "Merchant Bank Account created!"