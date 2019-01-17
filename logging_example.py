import logging

# default write changed (in stream, not in file)
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s : %(message)s', datefmt='%d-%b-%y %H:%M:%S',
                    level=logging.INFO)
logger = logging.getLogger()  # get the logger with default name 'root'


# add handler to write log to file
f_handler = logging.FileHandler('file.log', 'w')  # 'w' erase, 'a' append
f_handler.setLevel(logging.INFO)
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')  # format in file!
f_handler.setFormatter(f_format)
logger.addHandler(f_handler)
# end write log to file

# add a stream without format (in stream, not in file)
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
logger.addHandler(stream_handler)


logger.info("test to write in file and streams")  # 2 streams: 1 formatted, one not; 1 file: date formatted differently