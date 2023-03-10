from typing import IO

import pytest
from django.conf import settings


@pytest.fixture()
def deals_csv() -> str:
    return settings.TEST_FILES["deals_csv"]


@pytest.fixture()
def deals_csv_second() -> str:
    return settings.TEST_FILES["deals_csv_second"]


@pytest.fixture()
def deals_csv_invalid_file_extension() -> str:
    return settings.TEST_FILES["deals_csv_invalid_file_extension"]


@pytest.fixture()
def deals_txt_invalid_data() -> str:
    return settings.TEST_FILES["deals_txt_invalid_data"]


@pytest.fixture
def expect_fail_invalid_data():
    return [
        {
            "total": ["A valid number is required."],
            "quantity": ["A valid integer is required."],
            "date": [
                "Datetime has wrong format. "
                "Use one of these formats instead: "
                "YYYY-MM-DDThh:mm[:ss[.uuuuuu]][+HH:MM|-HH:MM|Z]."
            ],
            "line": "2",
        },
        {
            "date": [
                "Datetime has wrong format. "
                "Use one of these formats instead: "
                "YYYY-MM-DDThh:mm[:ss[.uuuuuu]][+HH:MM|-HH:MM|Z]."
            ],
            "line": "5",
        },
    ]
