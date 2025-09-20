import re

#Regex for phone numbers
text_phone = "(123) 456-7890 , 123-456-7890 , 123.456.7890"
pattern_phone = r"(\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4})"
matches_phone = re.findall(pattern_phone, text_phone)
print("Phone Numbers:", matches_phone)

#Regex for credit card numbers
text_credit = " 1234 5678 9012 3456, 1234-5678-9012-3456"
pattern_credit = r"(\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4})"
matches_credit = re.findall(pattern_credit, text_credit)
print("Credit Card Numbers:", matches_credit)

#Regex for hashtags
text_hashtag = "#example , #ThisIsAHashtag"
pattern_hashtag = r"(#[\w-]+)"
matches_hashtag = re.findall(pattern_hashtag, text_hashtag)
print("Hashtags:", matches_hashtag)

#Regex for currency amounts
text_currency = "$19.99 , $1,234.56"
pattern_currency = r"(\$\d{1,3}(?:,\d{3})*|\$\d+)(?:\.\d{2})?"
matches_currency = re.findall(pattern_currency, text_currency)
print("Currency :", matches_currency)

#Regex for time formats
text_time = "14:30 , 2:30 PM"
pattern_time = r"\b((?:[01]?\d|2[0-3]):[0-5]\d(?:\s?(?:AM|PM|am|pm))?)\b"
matches_time = re.findall(pattern_time, text_time)
print("Time :", matches_time)
