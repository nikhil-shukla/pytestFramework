import pytest
from datetime import datetime


@pytest.mark.usefixtures("setup_and_teardown")
class BaseTest:

    @staticmethod
    def generate_timestamp():
        return datetime.now().strftime("%Y%m%d%H%M%S")
