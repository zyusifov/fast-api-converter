import pytest
from src.domain import model


def test_if_can_create_jpg():
    jpg = model.JPG(src_path="fake.jpg")
    assert jpg.extensions == (".jpeg", ".jpg")


def test_if_jpegs_are_equal():
    jpg1 = model.JPG(src_path="fake.jpg")
    jpg2 = model.JPG(src_path="fake.jpg")

    assert jpg1 == jpg2


def test_if_can_create_pdf():
    pdf = model.PDF(dest_path="fake.pdf")
    assert pdf.extension == ".pdf"