"""List of popular cryptocurrencies"""

CRYPTOCURRENCIES = [
    # Top tier
    ("Bitcoin", "bitcoin"),
    ("Ethereum", "ethereum"),
    ("Binance Coin", "binancecoin"),
    ("Ripple", "ripple"),
    ("Cardano", "cardano"),

    # Layer 2 & Popular
    ("Solana", "solana"),
    ("Polkadot", "polkadot"),
    ("Dogecoin", "dogecoin"),
    ("Polygon", "matic-network"),
    ("Litecoin", "litecoin"),

    # DeFi
    ("Uniswap", "uniswap"),
    ("Aave", "aave"),
    ("Curve", "curve-dao-token"),
    ("Maker", "maker"),
    ("Yearn Finance", "yearn-finance"),

    # Layer 1 Alternatives
    ("Avalanche", "avalanche-2"),
    ("Fantom", "fantom"),
    ("Cosmos", "cosmos"),
    ("Algorand", "algorand"),
    ("Tezos", "tezos"),

    # Privacy & Other
    ("Monero", "monero"),
    ("Zcash", "zcash"),
    ("Dash", "dash"),
    ("Chainlink", "chainlink"),
    ("VeChain", "vechain"),

    # Meme & Popular
    ("Shiba Inu", "shiba-inu"),
    ("Doge", "dogecoin"),
    ("Pepe", "pepe"),

    # Stablecoins
    ("USDC", "usd-coin"),
    ("USDT", "tether"),
    ("DAI", "dai"),
    ("BUSD", "binance-usd"),

    # Gaming & Metaverse
    ("Decentraland", "decentraland"),
    ("The Sandbox", "the-sandbox"),
    ("Axie Infinity", "axie-infinity"),
    ("Gala", "gala"),

    # AI & Tech
    ("Fetch.ai", "fetch-ai"),
    ("The Graph", "the-graph"),
    ("Helium", "helium"),
    ("Arweave", "arweave"),
]

def get_crypto_names() -> list:
    """Get list of cryptocurrency names"""
    return [name for name, _ in CRYPTOCURRENCIES]

def get_crypto_id(name: str) -> str:
    """Get cryptocurrency ID by name"""
    for crypto_name, crypto_id in CRYPTOCURRENCIES:
        if crypto_name.lower() == name.lower():
            return crypto_id
    return name.lower()

def find_crypto(search: str) -> list:
    """Search cryptocurrencies by partial name"""
    search = search.lower()
    return [name for name, _ in CRYPTOCURRENCIES if search in name.lower()]
