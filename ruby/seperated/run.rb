require 'finix'
require_relative 'authentication'

#MERCHANT
require_relative 'merchant'
require_relative 'bank_account'
require_relative 'provision_merchant_acct'

#BUYER
require_relative 'buyer_identity.rb'
require_relative 'tokenize_card'

#AUTHORIZATION
# require_relative 'create_authorization'
# require_relative 'capture_authorization'

#PUSH-TO-CARD
require_relative 'recipient_identity'
require_relative 'payment_instrument'
require_relative 'verify_eligibility'

puts "run ruby ran"
