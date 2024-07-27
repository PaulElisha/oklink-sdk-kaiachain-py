import requests
from typing import List, Optional, Dict

BASE_URL = "https://www.oklink.com/"
chainId = "8217"
chainFullName = "KLAYTN"
chainShortName = "KLAYTN"

class Oklink:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = BASE_URL

    def header(self) -> Dict[str, str]:
        return {
            "Content-Type": "application/json",
            "Ok-Access-Key": self.api_key,
        }

    def address_info(self, address: str) -> Dict:
        params = {
            "chainShortName": chainShortName,
            "address": address,
        }
        url = f"{self.base_url}api/v5/explorer/address/address-summary"
        response = requests.get(url, headers=self.header(), params=params)
        return response.json()

    def evm_address_info(self, address: str) -> Dict:
        params = {
            "chainShortName": chainShortName,
            "address": address,
        }
        url = f"{self.base_url}api/v5/explorer/address/information-evm"
        response = requests.get(url, headers=self.header(), params=params)
        return response.json()

    def address_active_chain(self, address: str) -> Dict:
        params = {
            "chainShortName": chainShortName,
            "address": address,
        }
        url = f"{self.base_url}api/v5/explorer/address/address-active-chain"
        response = requests.get(url, headers=self.header(), params=params)
        return response.json()

    def address_token_balance(self, address: str, protocol_type: str, token_contract_address: Optional[str] = None, page: Optional[str] = None, limit: Optional[str] = None) -> Dict:
        params = {
            "chainShortName": chainShortName,
            "address": address,
            "protocolType": protocol_type,
        }
        if token_contract_address:
            params["tokenContractAddress"] = token_contract_address
        if page:
            params["page"] = page
        if limit:
            params["limit"] = limit
        url = f"{self.base_url}api/v5/explorer/address/token-balance"
        response = requests.get(url, headers=self.header(), params=params)
        return response.json()

    def address_balance_details(self, address: str, protocol_type: str, token_contract_address: Optional[str] = None, page: Optional[str] = None, limit: Optional[str] = None) -> Dict:
        params = {
            "chainShortName": chainShortName,
            "address": address,
            "protocolType": protocol_type,
        }
        if token_contract_address:
            params["tokenContractAddress"] = token_contract_address
        if page:
            params["page"] = page
        if limit:
            params["limit"] = limit
        url = f"{self.base_url}api/v5/explorer/address/address-balance-fills"
        response = requests.get(url, headers=self.header(), params=params)
        return response.json()

    def address_balance_history(self, address: str, height: str, token_contract_address: Optional[str] = None) -> Dict:
        params = {
            "chainShortName": chainShortName,
            "address": address,
            "height": height,
        }
        if token_contract_address:
            params["tokenContractAddress"] = token_contract_address
        url = f"{self.base_url}api/v5/explorer/block/address-balance-history"
        response = requests.get(url, headers=self.header(), params=params)
        return response.json()

    def address_transaction_list(self, address: str, protocol_type: Optional[str] = None, symbol: Optional[str] = None, start_block_height: Optional[str] = None, end_block_height: Optional[str] = None, is_from_or_to: Optional[str] = None, page: Optional[str] = None, limit: Optional[str] = None) -> Dict:
        params = {
            "chainShortName": chainShortName,
            "address": address,
        }
        if protocol_type:
            params["protocolType"] = protocol_type
        if symbol:
            params["symbol"] = symbol
        if start_block_height:
            params["startBlockHeight"] = start_block_height
        if end_block_height:
            params["endBlockHeight"] = end_block_height
        if is_from_or_to:
            params["isFromOrTo"] = is_from_or_to
        if page:
            params["page"] = page
        if limit:
            params["limit"] = limit
        url = f"{self.base_url}api/v5/explorer/address/transaction-list"
        response = requests.get(url, headers=self.header(), params=params)
        return response.json()

    def address_normal_transaction_list(self, address: str, start_block_height: Optional[str] = None, end_block_height: Optional[str] = None, is_from_or_to: Optional[str] = None, page: Optional[str] = None, limit: Optional[str] = None) -> Dict:
        params = {
            "chainShortName": chainShortName,
            "address": address,
        }
        if start_block_height:
            params["startBlockHeight"] = start_block_height
        if end_block_height:
            params["endBlockHeight"] = end_block_height
        if is_from_or_to:
            params["isFromOrTo"] = is_from_or_to
        if page:
            params["page"] = page
        if limit:
            params["limit"] = limit
        url = f"{self.base_url}api/v5/explorer/address/normal-transaction-list"
        response = requests.get(url, headers=self.header(), params=params)
        return response.json()

    def address_internal_transaction_list(self, address: str, start_block_height: Optional[str] = None, end_block_height: Optional[str] = None, is_from_or_to: Optional[str] = None, page: Optional[str] = None, limit: Optional[str] = None) -> Dict:
        params = {
            "chainShortName": chainShortName,
            "address": address,
        }
        if start_block_height:
            params["startBlockHeight"] = start_block_height
        if end_block_height:
            params["endBlockHeight"] = end_block_height
        if is_from_or_to:
            params["isFromOrTo"] = is_from_or_to
        if page:
            params["page"] = page
        if limit:
            params["limit"] = limit
        url = f"{self.base_url}api/v5/explorer/address/internal-transaction-list"
        response = requests.get(url, headers=self.header(), params=params)
        return response.json()

    def address_token_transaction_list(self, address: str, protocol_type: str, token_contract_address: Optional[str] = None, page: Optional[str] = None, limit: Optional[str] = None) -> Dict:
        params = {
            "chainShortName": chainShortName,
            "address": address,
            "protocolType": protocol_type,
        }
        if token_contract_address:
            params["tokenContractAddress"] = token_contract_address
        if page:
            params["page"] = page
        if limit:
            params["limit"] = limit
        url = f"{self.base_url}api/v5/explorer/address/token-transaction-list"
        response = requests.get(url, headers=self.header(), params=params)
        return response.json()

    def address_entity_labels(self, address: str) -> Dict:
        params = {
            "chainShortName": chainShortName,
            "address": address,
        }
        url = f"{self.base_url}api/v5/explorer/address/entity-labels"
        response = requests.get(url, headers=self.header(), params=params)
        return response.json()

    def batch_address_balances(self, addresses: List[str]) -> Dict:
        if len(addresses) > 100:
            raise ValueError("The maximum number of addresses is 100")
        params = {
            "chainShortName": chainShortName,
            "addresses": ",".join(addresses),
        }
        url = f"{self.base_url}api/v5/explorer/address/balance-multi"
        response = requests.get(url, headers=self.header(), params=params)
        return response.json()

    def batch_address_token_balances(self, addresses: List[str], protocol_type: Optional[str] = None, page: Optional[str] = None, limit: Optional[str] = None) -> Dict:
        if len(addresses) > 50:
            raise ValueError("The maximum number of addresses is 50")
        params = {
            "chainShortName": chainShortName,
            "addresses": ",".join(addresses),
        }
        if protocol_type:
            params["protocolType"] = protocol_type
        if page:
            params["page"] = page
        if limit:
            params["limit"] = limit
        url = f"{self.base_url}api/v5/explorer/address/token-balance-multi"
        response = requests.get(url, headers=self.header(), params=params)
        return response.json()

    def batch_address_normal_transaction_list(self, addresses: List[str], start_block_height: Optional[str] = None, end_block_height: Optional[str] = None, is_from_or_to: Optional[str] = None, page: Optional[str] = None, limit: Optional[str] = None) -> Dict:
        if len(addresses) > 50:
            raise ValueError("The maximum number of addresses is 50")
        params = {
            "chainShortName": chainShortName,
            "addresses": ",".join(addresses),
        }
        if start_block_height:
            params["startBlockHeight"] = start_block_height
        if end_block_height:
            params["endBlockHeight"] = end_block_height
        if is_from_or_to:
            params["isFromOrTo"] = is_from_or_to
        if page:
            params["page"] = page
        if limit:
            params["limit"] = limit
        url = f"{self.base_url}api/v5/explorer/address/normal-transaction-list-multi"
        response = requests.get(url, headers=self.header(), params=params)
        return response.json()

    def batch_address_internal_transaction_list(self, addresses: List[str], start_block_height: Optional[str] = None, end_block_height: Optional[str] = None, is_from_or_to: Optional[str] = None, page: Optional[str] = None, limit: Optional[str] = None) -> Dict:
        if len(addresses) > 20:
            raise ValueError("The maximum number of addresses is 20")
        params = {
            "chainShortName": chainShortName,
            "addresses": ",".join(addresses),
        }
        if start_block_height:
            params["startBlockHeight"] = start_block_height
        if end_block_height:
            params["endBlockHeight"] = end_block_height
        if is_from_or_to:
            params["isFromOrTo"] = is_from_or_to
        if page:
            params["page"] = page
        if limit:
            params["limit"] = limit
        url = f"{self.base_url}api/v5/explorer/address/internal-transaction-list-multi"
        response = requests.get(url, headers=self.header(), params=params)
        return response.json()

    def batch_address_token_transaction_list(self, addresses: List[str], start_block_height: str, end_block_height: str, page: Optional[str] = None, limit: Optional[str] = None, protocol_type: Optional[str] = None, token_contract_address: Optional[str] = None, is_from_or_to: Optional[str] = None) -> Dict:
        if len(addresses) > 20:
            raise ValueError("The maximum number of addresses is 20")
        params = {
            "chainShortName": chainShortName,
            "addresses": ",".join(addresses),
            "startBlockHeight": start_block_height,
            "endBlockHeight": end_block_height,
        }
        if page:
            params["page"] = page
        if limit:
            params["limit"] = limit
        if protocol_type:
            params["protocolType"] = protocol_type
        if token_contract_address:
            params["tokenContractAddress"] = token_contract_address
        if is_from_or_to:
            params["isFromOrTo"] = is_from_or_to
        url = f"{self.base_url}api/v5/explorer/address/token-transaction-list-multi"
        response = requests.get(url, headers=self.header(), params=params)
        return response.json()

    def rich_list(self, address: Optional[str] = None) -> Dict:
        params = {
            "chainShortName": chainShortName,
        }
        if address:
            params["address"] = address
        url = f"{self.base_url}api/v5/explorer/address/rich-list"
        response = requests.get(url, headers=self.header(), params=params)
        return response.json()

    def native_token_ranking(self, page: Optional[str] = None, limit: Optional[str] = None) -> Dict:
        params = {
            "chainShortName": chainShortName,
        }
        if page:
            params["page"] = page
        if limit:
            params["limit"] = limit
        url = f"{self.base_url}api/v5/explorer/address/native-token-position-list"
        response = requests.get(url, headers=self.header(), params=params)
        return response.json()

    def transaction_list(self, block_hash: Optional[str] = None, height: Optional[str] = None, page: Optional[str] = None, limit: Optional[str] = None) -> Dict:
        params = {
            "chainShortName": chainShortName,
        }
        if block_hash:
            params["blockHash"] = block_hash
        if height:
            params["height"] = height
        if page:
            params["page"] = page
        if limit:
            params["limit"] = limit
        url = f"{self.base_url}api/v5/explorer/transaction/transaction-list"
        response = requests.get(url, headers=self.header(), params=params)
        return response.json()

    def large_transaction_list(self, type: Optional[str] = None, height: Optional[str] = None, page: Optional[str] = None, limit: Optional[str] = None) -> Dict:
        params = {
            "chainShortName": chainShortName,
        }
        if type:
            params["type"] = type
        if height:
            params["height"] = height
        if page:
            params["page"] = page
        if limit:
            params["limit"] = limit
        url = f"{self.base_url}api/v5/explorer/transaction/large-transaction-list"
        response = requests.get(url, headers=self.header(), params=params)
        return response.json()

    def unconfirmed_transaction_list(self, page: Optional[str] = None, limit: Optional[str] = None) -> Dict:
        params = {
            "chainShortName": chainShortName,
        }
        if page:
            params["page"] = page
        if limit:
            params["limit"] = limit
        url = f"{self.base_url}api/v5/explorer/transaction/unconfirmed-transaction-list"
        response = requests.get(url, headers=self.header(), params=params)
        return response.json()

    def internal_transaction_details(self, tx_id: str, page: Optional[str] = None, limit: Optional[str] = None) -> Dict:
        params = {
            "chainShortName": chainShortName,
            "txId": tx_id,
        }
        if page:
            params["page"] = page
        if limit:
            params["limit"] = limit
        url = f"{self.base_url}api/v5/explorer/transaction/internal-transaction-detail"
        response = requests.get(url, headers=self.header(), params=params)
        return response.json()

    def token_transaction_details(self, tx_id: str, protocol_type: str, page: Optional[str] = None, limit: Optional[str] = None) -> Dict:
        params = {
            "chainShortName": chainShortName,
            "txId": tx_id,
        }
        if protocol_type:
            params["protocolType"] = protocol_type
        if page:
            params["page"] = page
        if limit:
            params["limit"] = limit
        url = f"{self.base_url}api/v5/explorer/transaction/token-transaction-detail"
        response = requests.get(url, headers=self.header(), params=params)
        return response.json()

    def transaction_details(self, tx_id: str) -> Dict:
        params = {
            "chainShortName": chainShortName,
            "txId": tx_id,
        }
        url = f"{self.base_url}api/v5/explorer/transaction/transaction-fills"
        response = requests.get(url, headers=self.header(), params=params)
        return response.json()

    def batch_transaction_details(self, tx_ids: List[str]) -> Dict:
        if len(tx_ids) > 20:
            raise ValueError("The maximum number of transactions is 20")
        params = {
            "chainShortName": chainShortName,
            "txIds": ",".join(tx_ids),
        }
        url = f"{self.base_url}api/v5/explorer/transaction/transaction-multi"
        response = requests.get(url, headers=self.header(), params=params)
        return response.json()

    def batch_internal_transaction_details(self, tx_ids: List[str]) -> Dict:
        if len(tx_ids) > 20:
            raise ValueError("The maximum number of transactions is 20")
        params = {
            "chainShortName": chainShortName,
            "txIds": ",".join(tx_ids),
        }
        url = f"{self.base_url}api/v5/explorer/transaction/internal-transaction-multi"
        response = requests.get(url, headers=self.header(), params=params)
        return response.json()

    def batch_token_transaction_details(self, tx_ids: List[str], protocol_type: Optional[str] = None, page: Optional[str] = None, limit: Optional[str] = None) -> Dict:
        if len(tx_ids) > 20:
            raise ValueError("The maximum number of transactions is 20")
        params = {
            "chainShortName": chainShortName,
            "txIds": ",".join(tx_ids),
        }
        if protocol_type:
            params["protocolType"] = protocol_type
        if page:
            params["page"] = page
        if limit:
            params["limit"] = limit
        url = f"{self.base_url}api/v5/explorer/transaction/token-transfer-multi"
        response = requests.get(url, headers=self.header(), params=params)
        return response.json()

    def token_list(self, protocol_type: Optional[str] = None, token_contract_address: Optional[str] = None, start_time: Optional[str] = None, end_time: Optional[str] = None, order_by: Optional[str] = None, page: Optional[str] = None, limit: Optional[str] = None) -> Dict:
        params = {
            "chainShortName": chainShortName,
        }
        if protocol_type:
            params["protocolType"] = protocol_type
        if token_contract_address:
            params["tokenContractAddress"] = token_contract_address
        if start_time:
            params["startTime"] = start_time
        if end_time:
            params["endTime"] = end_time
        if order_by:
            params["orderBy"] = order_by
        if page:
            params["page"] = page
        if limit:
            params["limit"] = limit
        url = f"{self.base_url}api/v5/explorer/token/token-list"
        response = requests.get(url, headers=self.header(), params=params)
        return response.json()

    def token_position_list(self, token_contract_address: str, holder_address: Optional[str] = None, page: Optional[str] = None, limit: Optional[str] = None) -> Dict:
        params = {
            "chainShortName": chainShortName,
            "tokenContractAddress": token_contract_address,
        }
        if holder_address:
            params["holderAddress"] = holder_address
        if page:
            params["page"] = page
        if limit:
            params["limit"] = limit
        url = f"{self.base_url}api/v5/explorer/token/position-list"
        response = requests.get(url, headers=self.header(), params=params)
        return response.json()

    def token_position_statistics(self, token_contract_address: str, holder_address: Optional[str] = None, page: Optional[str] = None, limit: Optional[str] = None) -> Dict:
        params = {
            "chainShortName": chainShortName,
            "tokenContractAddress": token_contract_address,
        }
        if holder_address:
            params["holderAddress"] = holder_address
        if page:
            params["page"] = page
        if limit:
            params["limit"] = limit
        url = f"{self.base_url}api/v5/explorer/token/position-statistics"
        response = requests.get(url, headers=self.header(), params=params)
        return response.json()

    def token_transfer_details(self, token_contract_address: str, max_amount: Optional[str] = None, min_amount: Optional[str] = None, page: Optional[str] = None, limit: Optional[str] = None) -> Dict:
        params = {
            "chainShortName": chainShortName,
            "tokenContractAddress": token_contract_address,
        }
        if max_amount:
            params["maxAmount"] = max_amount
        if min_amount:
            params["minAmount"] = min_amount
        if page:
            params["page"] = page
        if limit:
            params["limit"] = limit
        url = f"{self.base_url}api/v5/explorer/token/transaction-list"
        response = requests.get(url, headers=self.header(), params=params)
        return response.json()

    def batch_token_transaction(self, token_contract_address: str, start_block_height: str, end_block_height: str, page: Optional[str] = None, limit: Optional[str] = None) -> Dict:
        params = {
            "chainShortName": chainShortName,
            "tokenContractAddress": token_contract_address,
            "startBlockHeight": start_block_height,
            "endBlockHeight": end_block_height,
        }
        if page:
            params["page"] = page
        if limit:
            params["limit"] = limit
        url = f"{self.base_url}api/v5/explorer/token/token-transaction-list-multi"
        response = requests.get(url, headers=self.header(), params=params)
        return response.json()

    def token_supply_history(self, token_contract_address: str, height: str) -> Dict:
        params = {
            "chainShortName": chainShortName,
            "tokenContractAddress": token_contract_address,
            "height": height,
        }
        url = f"{self.base_url}api/v5/explorer/token/supply-history"
        response = requests.get(url, headers=self.header(), params=params)
        return response.json()

    def token_transaction_statistics(self, token_contract_address: str, order_by: Optional[str] = None, page: Optional[str] = None, limit: Optional[str] = None) -> Dict:
        params = {
            "chainShortName": chainShortName,
            "tokenContractAddress": token_contract_address,
        }
        if order_by:
            params["orderBy"] = order_by
        if page:
            params["page"] = page
        if limit:
            params["limit"] = limit
        url = f"{self.base_url}api/v5/explorer/token/transaction-stats"
        response = requests.get(url, headers=self.header(), params=params)
        return response.json()