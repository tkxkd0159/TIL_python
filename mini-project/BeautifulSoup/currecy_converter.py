import os
import requests
from bs4 import BeautifulSoup
from babel.numbers import format_currency
from lib import currency_converter, WrongNum

2
os.system("clear")

"""
Use the 'format_currency' function to format the output of the conversion
format_currency(AMOUNT, CURRENCY_CODE, locale="ko_KR" (no need to change this one))
"""


url = "https://www.iban.com/currency-codes"

web_result = requests.get(url)
soup = BeautifulSoup(web_result.text, "html.parser")
code_table = soup.find("table")
table_row = code_table.find("tbody")
country_list = table_row.find_all('tr')

max_num = len(country_list)
country_dict = {}
for i in range(max_num):
  country_dict[i] = country_list[i].get_text().split("\n")[1:-1]

print('Welcome to currency converter')

for key, value in country_dict.items():
  print(f'# {key} {value[0]}')

while True:
  while True:
    try:

      print("Where are you from? Choose a country by number.")
      source_num = int(input('#: '))
      if source_num >= max_num or source_num <= 0:
        raise IndexError
      source = country_dict[source_num]
      print(f'{source[0]} \n')
      break

    except ValueError:
      print('That wasn\'t a number')
    except IndexError:
      print('Choose a number from the list')

  while True:
    try:

      print("Now Choose another country.")
      target_num = int(input('#: '))
      if target_num >= max_num or target_num <= 0:
        raise IndexError

      target = country_dict[target_num]
      print(f'{target[0]} \n')
      break

    except ValueError:
      print('That wasn\'t a number')
    except IndexError:
      print('Choose a number from the list')

  src_code = source[2]
  tgt_code = target[2]
  print(source)

  while True:
    try:
      print(f'How many {src_code} do you want to convert to {tgt_code}? ')
      origin_money = float(input())
      if origin_money < 0:
        raise WrongNum
      break

    except ValueError:
      print('That wasn\'t a number')
    except WrongNum:
      print('Choose Positive Number')

  result = currency_converter(origin_money, src_code, tgt_code)
  if result is not False:
    result = format_currency(result, target[2], locale="ko_KR")
    print(f'{src_code}{origin_money:,.2f} is {result} \n')
  else:
    print(f'This pair is not valid \n')

