import logging
logging.basicConfig(level=logging.INFO)   #set the logging level to info
def decorator_func(*args):
    logging.info("i am an decorator function")
    def inner_func(func):
        logging.info("i am an inner function")
        for arg in args:
            if arg=='Admin':
                func()
            else:
                logging.warning("user don't have access")
    return inner_func
@decorator_func('Admin','thina')
def fun():
    logging.info("Admin can access")


if __name__ == "__main__":
    decorator_func()

# it allows user to add new functionality to an existing object without modifying its structure

        

