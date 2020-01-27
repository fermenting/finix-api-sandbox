require 'finix'
require_relative 'authentication'

#MERCHANT
require_relative 'merchant'
require_relative 'bank_account'
require_relative 'provision_merchant_acct'

#BUYER
require_relative 'buyer_identity.rb'
require_relative 'tokenize_card'
require_relative 'create_auth'
require_relative 'capture_auth'



puts "run ruby ran"
