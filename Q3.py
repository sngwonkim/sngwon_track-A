import requests

def get_tx_outputs_count(block):
    try:
        url = f"https://api.blockcypher.com/v1/btc/test3/blocks/{block}"
        response = requests.get(url)
        response.raise_for_status()
        block_data = response.json()
        transactions = block_data["txids"]
        
        total_outputs = 0
        for txid in transactions:
            tx_url = f"https://api.blockcypher.com/v1/btc/test3/txs/{txid}"
            tx_response = requests.get(tx_url)
            tx_response.raise_for_status()
            tx_data = tx_response.json()
            total_outputs += len(tx_data["outputs"])
        
        return total_outputs
    except Exception as error:
        print("Error fetching block data:", error)
        raise

def main():
    block = 2817691

    try:
        count = get_tx_outputs_count(block)
        print(f"Number of new outputs created by block at block {block}: {count}")
    except Exception as error:
        print("Error from fetching outputs:", error)

if __name__ == "__main__":
    main()
