import sys
from logger_file import logger
def error_message(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()   #extracting the traceback
    print(error_detail.exc_info())
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = f"Error {error} occurred in file {file_name} at line number {line_number}: "
    return error_message



#creating our custom error class for raising the error
class CustomError(Exception):
    def __init__(self,message,error_detail:sys):
        self.error_message = error_message(message,error_detail=error_detail)
    def __str__(self):
     return self.error_message


if __name__=="__main__":
    try:
        1 / 0
    except Exception as e:
        logger.info(e)
        raise CustomError(message=str(e),error_detail=sys)