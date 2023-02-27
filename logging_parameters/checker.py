import logging

#authored by Geovana Mosquera
# logging information that is going to be used throughout the code
def log_parameters():
    logging.basicConfig(filename="logfile.log", format='%(asctime)s - %(levelname)s - %(message)s',
                        filemode="w", level=logging.DEBUG)
    logging.getLogger().addHandler(logging.StreamHandler())
    # logging while using matplotlip cases alot of un-needed information flowing lines is for cleaning the logging
    logging.getLogger('matplotlib').setLevel(logging.WARNING)
    logging.getLogger('matplotlib.font_manager').disabled = True
    logging.getLogger('matplotlib.tick_params').disabled = True



def logger(func):
    def wrapper(*args, **kwargs):
        print('Processing Data...')
        log_parameters()
        func(*args, **kwargs)
        logging.shutdown()
        print('Work Finished. For more information, access the logfile.log.')
    return wrapper
