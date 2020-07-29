
class Scanner:

    def __init__(self, excel_worksheet_obj):
        self.ws = excel_worksheet_obj

# header df
# date df
# exchange df
# yth discount df
class NonTabularDFScanner(Scanner):

    def __init__(self, excel_worksheet_obj, label_data):
        """
        Args:
            excel_worksheet_obj (openpyxl.worksheet): Worksheet object
            label_data (list): List of tuples [(addr_str, label_str)]
        """
        super().__init__(excel_worksheet_obj)
        self.label_data = label_data

# summary df
class SummaryDFScanner(Scanner):

    def __init__(self, excel_worksheet_obj):
        """
        Args:
            excel_worksheet_obj (openpyxl.worksheet): Worksheet object
        """
        super().__init__(excel_worksheet_obj)
        self.label_column = 'N'

# fabric df
# trims df
# new sew application
# packaging
class TabularDFScanner(Scanner):

    def __init__(self, excel_worksheet_obj, label_data):
        """
        Args:
            excel_worksheet_obj (openpyxl.worksheet): Worksheet object
            label_data (list): List of tuples [(addr_str, label_str)]
        """
        super().__init__(excel_worksheet_obj)
        self.label_data = label_data

# worksheet object

# scanner criteria
# type 1 - non-tabular, static
    # uses absolute references for data label fields
    # returns single row dataframe

# type 2 - non-tabular, non-static
    # assumption: data label field set will be the same, but may start on differing rows
    # assumption: column structure is not changing

# type 3 - tabular, non-static
    # criteria: table title followed by header row
    # note: header row is the same for all tabular DFs
    # note: need to determine last record row
