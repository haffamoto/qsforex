from decimal import Decimal
import os


ENVIRONMENTS = { 
    "streaming": {
        "real": "stream-fxtrade.oanda.com",
        "practice": "stream-fxpractice.oanda.com",
        "sandbox": "stream-sandbox.oanda.com"
    },
    "api": {
        "real": "api-fxtrade.oanda.com",
        "practice": "api-fxpractice.oanda.com",
        "sandbox": "api-sandbox.oanda.com"
    }
}

# for environment variables use "os.environ.get('QSFOREX_OUTPUT_RESULTS_DIR', None)"
# currently hardcoded 
CSV_DATA_DIR = "/media/deckard/External/FOREX/Dukascopy/csv_files"
OUTPUT_RESULTS_DIR = "/media/deckard/External/FOREX/qsforex_output"

DOMAIN = "practice"
STREAM_DOMAIN = ENVIRONMENTS["streaming"][DOMAIN]
API_DOMAIN = ENVIRONMENTS["api"][DOMAIN]
ACCESS_TOKEN = "c1888d2cec63c18f0fc943c9dc46ce37-37172e454f1162e8cab2499e917b64c0"
ACCOUNT_ID = "1910407"

BASE_CURRENCY = "GBP"
EQUITY = Decimal("100000.00")
