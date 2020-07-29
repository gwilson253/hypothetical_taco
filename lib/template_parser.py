
# get_error_df should return a default DF if empty
import dataframe_parser

class TemplateParser:

    def __init__(self, excel_worksheet_obj):
        self.ws = excel_worksheet_obj

    def get_target_sheet(self):
        """still don't know how to do this"""
        pass

    def get_header_df(self):
        pass

    def get_bom_df(self):
        pass

    """
    insert the other get_x_df functions here
    """