import locale

# Map currency codes to locales
currency_to_locale = {
    'USD': 'en_US.UTF-8',  # US Dollar
    'EUR': 'de_DE.UTF-8',  # Euro
    'GBP': 'en_GB.UTF-8',  # British Pound
    'NGN': 'en_NG.UTF-8',  # Nigerian Naira (locale might not be available)
}

def format_price(price, currency_code):
    # Set the locale dynamically based on the currency code
    locale_str = currency_to_locale.get(currency_code)
    
    if locale_str:
        locale.setlocale(locale.LC_ALL, locale_str)
    else:
        print(f"Locale for currency code '{currency_code}' not found, defaulting to US locale.")
        locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

    # Format the price as currency
    formatted_price = locale.currency(price, grouping=True)
    return formatted_price


price = 1234567
currency_code = 'USD'  

formatted_price = format_price(price, currency_code)
print(formatted_price) 
