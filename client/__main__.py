import logging
from config_parser import DFParser
from queries import QuerieManager

def main():
    logging.basicConfig()
    parsed_data = DFParser('Data/config.json')
    query = QuerieManager(parsed_data)
    query.run()

if __name__ == '__main__':
    main()