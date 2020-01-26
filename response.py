Merchant_Identity(
uri='/identities/ID9NMqp9PdTdDzdfgzwc4pP', 
application='APiwqrQ7wxQQ6AgJtKz8ibC7', 
created_at='2020-01-17T00:01:58.49Z', 
entity=OrderedDict(
        [('amex_mid', None), 
        ('annual_card_volume', 12000000), 
        
        ('business_address', 
        Object({
            'city': 'San Mateo', 
            'country': 'USA', 
            'line1': '741 Douglass St', 
            'line2': 'Apartment 8', 
            'postal_code': '94114', 
            'region': 'CA'})
            ),
        ('business_name', 'Lees Sandwiches'),
        ('business_phone', '+1 (408) 756-4497'
        ('business_tax_id_provided', True
        ('business_type', 'INDIVIDUAL_SOLE_PROPRIETORSHIP'
        ('default_statement_descriptor', 'Lees Sandwiches'
        ('discover_mid', None
        ('dob', Object({'day': 27, 'month': 6, 'year': 1978})
        ('doing_business_as', 'Lees Sandwiches'
        ('email', 'user@example.org'
        ('first_name', 'dwayne'
        ('has_accepted_credit_cards_previously', True
        ('incorporation_date', Object({'day': 27, 'month': 6, 'year': 1978})
        ('last_name', 'Sunkhronos'
        ('max_transaction_amount', 12000000
        ('mcc', '0742'
        ('ownership_type', 'PRIVATE'
        ('personal_address', Object({'city': 'San Mateo', 'country': 'USA', 'line1': '741 Douglass St', 'line2': 'Apartment 7', 'postal_code': '94114', 'region': 'CA'})
        ('phone', '1234567890'
        ('principal_percentage_ownership', 50
        ('short_business_name', None
        ('tax_id_provided', True
        ('title', 'CEO'
        ('url', 'www.LeesSandwiches.com')],
    id='ID9NMqp9PdTdDzdfgzwc4pP', 
    tags=OrderedDict([('Studio Rating', '4.7')]
        updated_at='2020-01-17T00:01:58.49Z', 
        associated_identities=<wac.ResourceCollection object at 0x103224b20>, 
        authorizations=<wac.ResourceCollection object at 0x10325a610>, 
        disputes=<wac.ResourceCollection object at 0x10325a820>, 
        merchants=<wac.ResourceCollection object at 0x10325a730>, 
        payment_instruments=<wac.ResourceCollection object at 0x10325a7c0>, 
        settlements=<wac.ResourceCollection object at 0x10325a8e0>, 
        transfers=<wac.ResourceCollection object at 0x10325a9a0>, 
        verifications=<wac.ResourceCollection object at 0x10325aa60>)


BankAccount(
    uri='/payment_instruments/PIbyReiBundAJb9KPfWgFLiq', 
    account_type='SAVINGS', 
    application='APiwqrQ7wxQQ6AgJtKz8ibC7', 
    bank_code='123123123', 
    country='USA', 
    created_at='2020-01-17T00:22:51.90Z', 
    currency='USD', 
    fingerprint='FPRd5moHxL3Ltuvk4cczxetCg', 
    id='PIbyReiBundAJb9KPfWgFLiq', 
    identity='IDrE9ezGKCZhFN7NCigZ3TbC', 
    instrument_type='BANK_ACCOUNT', 
    masked_account_number='XXXXX3123', 
    name='Fran Lemke', 
    tags=OrderedDict([('Bank Account', 
    'Company Account')]), 
    type='BANK_ACCOUNT', 
    updated_at='2020-01-17T00:22:51.90Z', 
    authorizations=<wac.ResourceCollection object at 0x11042f0d0>, 
    transfers=<wac.ResourceCollection object at 0x11045a280>, 
    verifications=<wac.ResourceCollection object at 0x11045ab50>)

Merchant(
    uri='/merchants/MUjqZJfQFEfGsQfQYYkzVduQ', 
    application='APiwqrQ7wxQQ6AgJtKz8ibC7', 
    created_at='2020-01-17T00:43:43.40Z', 
    creating_transfer_from_report_enabled=False, 
    gross_settlement_enabled=False, 
    id='MUjqZJfQFEfGsQfQYYkzVduQ', 
    identity='IDpArW3Accovep6QF1rkdsbc', 
    mcc='0742', 
    merchant_name='Lees Sandwiches', 
    merchant_profile='MP8k7r3fK3P7vnZPUVAjgTix', 
    mid=None, 
    onboarding_state='APPROVED', 
    processing_enabled=True, 
    processor='DUMMY_V1', 
    processor_details=OrderedDict([('api_key', 
    'secretValue')]), 
    settlement_enabled=True, 
    tags=OrderedDict(), 
    updated_at='2020-01-17T00:43:43.81Z', 
    verification='VIwaqkW4fuWetZNHb5JFj54h', 
    verifications=<wac.ResourceCollection object at 0x10984ce50>)

Buyer_Identity(
uri='/identities/ID9h8DPWucWjnn4HB7EyFp8t', 
application='APiwqrQ7wxQQ6AgJtKz8ibC7', 
created_at='2020-01-17T16:41:42.60Z', 
entity=OrderedDict([
    ('amex_mid', None), 
    ('annual_card_volume', 0),
    ('business_address', None),
    ('business_name', None),
    ('business_phone', None),
    ('business_tax_id_provided', False),
    ('business_type', None),
    ('default_statement_descriptor', None),
    ('discover_mid', None),
    ('dob', None),
    ('doing_business_as', None),
    ('email', 'therock@gmail.com'),
    ('first_name', 'Ricardo'),
    ('has_accepted_credit_cards_previously', False),
    ('incorporation_date', None),
    ('last_name', 'Sterling'),
    ('max_transaction_amount', 0),
    ('mcc', None),
    ('ownership_type', None),
    ('personal_address', 
        Object({
        'city': 'San Mateo', 
        'country': 'USA', 
        'line1': '741 Douglass St', 
        'line2': 'Apartment 7', 
        'postal_code': '94114', 
        'region': 'CA'
        })), 
    ('phone', '7145677613'), 
    ('principal_percentage_ownership', None), 
    ('short_business_name', None), 
    ('tax_id_provided', False), 
    ('title', None), 
    ('url', None)]), 
id='ID9h8DPWucWjnn4HB7EyFp8t', 
tags=OrderedDict([('key', 'value')]), 
updated_at='2020-01-17T16:41:42.60Z', 
associated_identities=<wac.ResourceCollection object at 0x10d32d2e0>, 
authorizations=<wac.ResourceCollection object at 0x10e45a310>, 
disputes=<wac.ResourceCollection object at 0x10e45a3d0>, 
merchants=<wac.ResourceCollection object at 0x10e45a490>, 
payment_instruments=<wac.ResourceCollection object at 0x10e45a550>, 
settlements=<wac.ResourceCollection object at 0x10e45a610>, 
transfers=<wac.ResourceCollection object at 0x10e45a6d0>, 
verifications=<wac.ResourceCollection object at 0x10e45a790>)

PaymentCard(
    uri='/payment_instruments/PIrQ85UsjCMkErjJX51uJuUc', 
    address=OrderedDict([
        ('city', 'San Francisco'), 
        ('country', 'USA'), 
    ('line1', '900 Metro Center Blv'), 
    ('line2',  None), 
    ('postal_code', '94404'), 
    ('region', 'CA')
    ]), 
    address_verification='UNKNOWN', 
    application='APiwqrQ7wxQQ6AgJtKz8ibC7', 
    bin='489514', 
    brand='VISA', 
    card_type='UNKNOWN', 
    created_at='2020-01-17T17:34:42.45Z', 
    currency='USD', 
    expiration_month=3, 
    expiration_year=2020, 
    fingerprint='FPRogKWsRQks2HGaau5eGR9AF', 
    id='PIrQ85UsjCMkErjJX51uJuUc', 
    identity='IDw1UHPEmZTeteUtAzCjg4F7', 
    instrument_type='PAYMENT_CARD', 
    last_four='0006', 
    name='Steph Diaz', 
    security_code_verification='UNKNOWN', 
    tags=OrderedDict([
        ('card_name', 'Business Card')]), 
    type='PAYMENT_CARD', 
    updated_at='2020-01-17T17:34:42.45Z', 
    authorizations=<wac.ResourceCollection object at 0x108658cd0>, 
    transfers=<wac.ResourceCollection object at 0x108671760>, 
    updates=<wac.ResourceCollection object at 0x108671820>, 
    verifications=<wac.ResourceCollection object at 0x1086718e0>)

Authorization(
    uri='/authorizations/AUvAyjxDGtH5LCi5qjUPvKL8', 
    3ds_redirect_url=None, 
    amount=100, 
    application='APiwqrQ7wxQQ6AgJtKz8ibC7', 
    created_at='2020-01-17T17:44:40.74Z', 
    currency='USD', 
    expires_at='2020-01-24T17:44:40.74Z', 
    id='AUvAyjxDGtH5LCi5qjUPvKL8', 
    idempotency_id=None, 
    is_void=False, 
    merchant_identity='ID5iN1jsgMNF4rp6Ad4SFSPo', 
    messages=Array([]), 
    raw=None, 
    source='PIqFcJNwWUTZuJz2AYD6mzNo', 
    state='SUCCEEDED', 
    tags=OrderedDict([('order_number', 
    '21DFASJSAKAS')]), 
    trace_id='db0287d5-7ea8-4245-a4eb-9c3f5e9c447b', 
    transfer=None, 
    updated_at='2020-01-17T17:44:40.87Z', 
    void_state='UNATTEMPTED')