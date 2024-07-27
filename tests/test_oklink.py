from src.oklink_py.protocol import ProtocolType
from src.oklink_py.oklink import Oklink
from src.oklink_py.config import Config
import pprint

oklink = Oklink(Config.api_key or "")

# Test get addressInfo
try:
    result = oklink.address_info(Config.test1)
    pprint.pprint(result, depth=None)
except Exception as error:
    print(error)

# Test get addressActiveChain
try:
    result = oklink.address_active_chain(Config.test1)
    pprint.pprint(result, depth=None)
except Exception as error:
    print(error)

# Test get addressBalance
try:
    result = oklink.address_token_balance(Config.test1, ProtocolType.token_20)
    pprint.pprint(result, depth=None)
except Exception as error:
    print(error)