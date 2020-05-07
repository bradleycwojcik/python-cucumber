
import logging

if __name__ == '__main__':
    logging.basicConfig(
        format='[%(asctime)s - %(levelname)s] %(message)s',
        level=logging.INFO,
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    logging.info('some message')
