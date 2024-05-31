import requests

block_height = 281760 # matched 블록 번호
response = requests.get(f"https://api.blockcypher.com/v1/btc/test3/blocks/{block_number}")
block_data = response.json()
block_hash = block_data['hash']

block_hash
