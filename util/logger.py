import logging

logging.basicConfig(
    filename='../cpu/application.log',
    level=logging.INFO,
    filemode='w',
    format= '[%(asctime)s] %(levelname)s - %(message)s',
    datefmt='%H:%M:%S'
)

event_names = {
    'nop': 'Executed NOP'
}


def log_event_by_name(event_name):
    pass


def log_event(event):
    if __debug__:
        logging.info(event)
