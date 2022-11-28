import sys,os


'''
Note: sys. exc_info() returns a tuple with three values (type, value, traceback). 
Here type gets the exception type of the Exception being handled. 
value is the arguments that are being passed to constructor of exception class.
traceback contains the stack information like where the exception occurred etc.

Note 2 : The __str__ method in Python represents the class objects as a string 
exception_type, exception_object, exception_traceback = sys.exc_info()
filename = exception_traceback.tb_frame.f_code.co_filename
line_number = exception_traceback.tb_lineno
'''
def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message



class SensorException(Exception):

    def __init__(self,error_message, error_detail:sys):
        self.error_message = error_message_detail(
            error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message