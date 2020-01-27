# verification = Finix::Verification.new(
# {
#     "processor" => "VISA_V1"
# })
# puts verification

identity = Identity.get(id=$merchant.id)
$merchant = identity.provision_merchant_on(Merchant())