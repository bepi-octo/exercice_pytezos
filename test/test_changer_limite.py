from unittest import TestCase, main
from pytezos import MichelsonRuntimeError
from pytezos import ContractInterface
from decimal import Decimal
from os.path import dirname, join

administrator = "tz1ibMpWS6n6MJn73nQHtK5f4ogyYC1z9T9z"
alice = "tz1L738ifd66ah69PrmKAZzckvvHnbcSeqjf"
bob = "tz1LFuHW4Z9zsCwg1cgGTKU12WZAs27ZD14v"
frank = "tz1Qd971cetwNr5f4oKp9xno6jBvghZHRsDr"
pascal = "tz1TgK3oaBaqcCHankT97AUNMjcs87Tfj5vb"
jacob = "tz1VphG4Lgp39MfQ9rTUnsm7BBWyXeXnJSMZ"
lucina = "tz1ZAZo1xW4Veq5t7YqWy2SMbLdskmeBmzqs"
mark = "tz1ccWCuJqMxG4hoa1g5SKhgdTwXoJBM8kpc"
jean = "tz1hQzKQpprB5JhNxZZRowEDRBoieHRAL84b"
boby = "tz1hTic2GpaNumpTtYwqyPSBd9KcWifRMuEN"
bartholome = "tz1hv9CrgtaxiCayc567KUvCyWDQRF9sVNuf"
lucas = "tz1iWMsg4UNSSQNKYsiH5s2maUZ9xBwymXxR"
contract_address = "KT1BEqzn5Wx8uJrZNvuS9DVHmLvG9td3fDLi"

path_to_michelson_contract = join(dirname(dirname(__file__)), 'test/app.tz')


def get_storage(self, compteur=None, cache=None, limite=None, administrateur=None):
    if compteur is None:
        compteur = 0
    if cache is None:
        cache = {}
    if limite is None:
        limite = 10
    if administrateur is None:
        administrateur = administrator
    return {"compteur": compteur,
            "cache": cache,
            "limite": limite,
            "administrateur": administrateur
            }


class TestBoiteNoire(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.nftContract = ContractInterface.create_from(path_to_michelson_contract)
        cls.nftContract.address = contract_address

    get_storage = get_storage

    def test_description_1(self):
        pass

if __name__ == '__main__':
    main()
