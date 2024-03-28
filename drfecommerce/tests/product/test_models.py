import pytest

pytestmark = pytest.mark.django_db


class TestCategoryModel:
    def test_str_method(self, category_factory):
        # Arrange
        # Act
        x = category_factory(name="test_cat")
        # Assert
        assert x.__str__() == "test_cat"


class TestBrandModel:
    def test_str_method(self, brand_factory):
        # Arrange
        # Act
        obj = brand_factory(name="test_brand")
        # Assert
        assert obj.__str__() == "test_brand"


class TestProductModel:
    def test_product_method(self, product_factory):
        # Arrange
        # Act
        obj = product_factory(name="test_product")
        # Assert
        assert obj.__str__() == "test_product"
