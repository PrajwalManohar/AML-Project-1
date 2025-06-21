from src.logger import get_logger
from src.custom_exception import CustomException
import sys

logger=get_logger(__name__)

def divide_number(a,b):
    try:
        result=a/b
        logger.info("Dividing 2 Numbers")
        return result
    except Exception as e:
        logger.error("Error Occured:")
        raise CustomException("Customer Error Zero",sys)


if __name__=="__main__":
    try:
        logger.info("Starting Main Program")
        divide_number(10,2)
    except CustomException as ce:
        logger.error(str(ce))