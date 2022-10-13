from blockchain import Blockchain

if __name__ == "__main__":
    skins = [(1, 45), (5, 78), (67, 89), (6, 90)]
    _from = "0xe2E1220512c61734c650E654f63f900A4ED3bbC5"

    blockchain = Blockchain()
    blockchain.insertBlock(_from, skins)
    blockchain.insertBlock(_from, skins)
    print(blockchain)
