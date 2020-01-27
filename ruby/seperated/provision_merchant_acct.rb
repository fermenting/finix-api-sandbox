identity = Finix::Identity.retrieve(:id=>$merchant.id)

$merchant = identity.provision_merchant

puts "Merchant Account Provisioned!"
puts "onboarding_state: " + $merchant.onboarding_state