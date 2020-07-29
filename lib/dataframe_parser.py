
"""
Will likely use
- openpyxl
- pandas
"""

from abc import ABC, abstractmethod

class DataFrameParser(ABC):

    def __init__(self, template_file):
        super().__init__()
        self.template_file = template_file
        self.error_df = None

    @abstractmethod
    def parse_dataframe(self):
        pass

    @abstractmethod
    def validate_dataframe(self):
        pass

    def get_dataframe(self):
        df = self.parse_dataframe()
        self.error_df = self.validate_dataframe()
        if self.error_df:
            raise ValueError("Value errors were detected in the CBD Template component dataframes.")
        return df


class HeaderDFParser(DataFrameParser):

    def __init__(self, template_file):
        super().__init__(template_file)

    def check_header_labels(self):
        """Verify header labels are are correct"""
        pass


class DateDFParser(DataFrameParser):

    def __init__(self, template_file):
        super().__init__(template_file)


class YouthStylesDFParser(DataFrameParser):

    def __init__(self, template_file):
        super().__init__(template_file)


class LocalCurrencyDFParser(DataFrameParser):

    def __init__(self, template_file):
        super().__init__(template_file)

class FabricDFParser(DataFrameParser):

    def __init__(self, template_file):
        super().__init__(template_file)

class TrimsDFParser(DataFrameParser):

    def __init__(self, template_file):
        super().__init__(template_file)


class NoSewAppDFParser(DataFrameParser):

    def __init__(self, template_file):
        super().__init__(template_file)

class PackagingDFParser(DataFrameParser):

    def __init__(self, template_file):
        super().__init__(template_file)


class SummaryDFParser(DataFrameParser):

    def __init__(self, template_file):
        super().__init__(template_file)

