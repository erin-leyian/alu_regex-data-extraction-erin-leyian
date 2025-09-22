# alu_regex-data-extraction-erin-leyian

Regex Data Extraction

This project uses Regular expressions in python to extrach data from text

The script features scan through text and find:
- Phone numbers
- Card numbers
- Currencies
- Time in 4 and 12 hour formats
- Hashtags

HOW TO RUN IT
git clone 
cd alu_regex-data-extraction-erin-leyian
python 3 

SAMPLE OUTPUT
Phone input: (123) 456-7890, 123-456-7890, 1234567890
Output: '(123) 456-7890' , '123-456-7890',  '1234567890'

Currency Input: $19.99, $1,234.56, $100
Output: '$19.99, $1,234.56, $100'

Time Input: 2:30 PM, 14:45, 00:00
Output: '2:30 PM', '14:45', '00:00'

Hashag Input: #example, #ThisIsAHashtag
Output: '#example', '#ThisIsAHashtag'

Card Input: 1234 5678 9012 3456, 1234-5678-9012-3456
Output: '1234 5678 9012 3456', '1234-5678-9012-3456'

EDGE CASE HANDLING

Regex solutions handle common edge cases:

1.Phone Numbers: Multiple separators (spaces, dots, dashes) or none at all.

2.Credit Cards: With or without spaces and dashes.

3.Currency: With/without commas and decimals.

4.Time: Both 12-hour fomats (AM/PM) and 24-hour formats.

 
