import pytest
import pandas as pd
from project import get_appetizers, get_main, get_desserts, get_info, add_to_cart, clear_cart, cart

@pytest.fixture
def sample_data():
    """Create fake data based on healthy_menu.csv to test"""
    data = {
        "Dish Name": [
            "Avocado and Quinoa Salad", "Smoked Salmon and Cucumber Roll", "Grilled Salmon with Asparagus and Sweet Potato Mash",
            "Chicken and Avocado Lettuce Wraps", "Chia Seed Pudding with Berries"
        ],
        "Category": ["Appetizer", "Appetizer", "Main Course", "Main Course", "Dessert"],
        "Calories (kcal)": [250, 180, 400, 350, 180],
        "Protein (g)": [8, 22, 40, 28, 7],
        "Price (VND)": [345000, 395000, 575000, 390000, 235000],
        "Allergy Info": ["NONE", "Fish, Dairy", "Fish, Dairy", "Dairy, Poultry", "Dairy"]
    }
    return pd.DataFrame(data)

@pytest.fixture(autouse=True)
def reset_cart():
    """Reset cart after each test"""
    global cart
    cart.clear()

def test_get_appetizers(sample_data, monkeypatch):
    """Test the get_appetizers function"""
    monkeypatch.setattr("project.dish", sample_data)
    assert get_appetizers() == ["Avocado and Quinoa Salad", "Smoked Salmon and Cucumber Roll"]

def test_get_main(sample_data, monkeypatch):
    """Test the get_main function"""
    monkeypatch.setattr("project.dish", sample_data)
    assert get_main() == ["Grilled Salmon with Asparagus and Sweet Potato Mash", "Chicken and Avocado Lettuce Wraps"]

def test_get_desserts(sample_data, monkeypatch):
    """Test the get_desserts function"""
    monkeypatch.setattr("project.dish", sample_data)
    assert get_desserts() == ["Chia Seed Pudding with Berries"]

def test_get_info(sample_data, monkeypatch):
    """Test the get_info function"""
    monkeypatch.setattr("project.dish", sample_data)

    # Test with a valid dish from Appetizers
    result = get_info("Avocado and Quinoa Salad")
    assert "## 🥗 **Avocado and Quinoa Salad**" in result
    assert "- **Calories:** 250 kcal" in result
    assert "- **Protein:** 8 g" in result
    assert "- **Price:** 345,000 VND" in result
    assert "- **Allergy Info:** NONE" in result

    # Test with a valid dish from Main Course
    result = get_info("Chicken and Avocado Lettuce Wraps")
    assert "## 🥗 **Chicken and Avocado Lettuce Wraps**" in result
    assert "- **Calories:** 350 kcal" in result
    assert "- **Protein:** 28 g" in result
    assert "- **Price:** 390,000 VND" in result
    assert "- **Allergy Info:** Dairy, Poultry" in result

    # Test with a valid dish from Desserts
    result = get_info("Chia Seed Pudding with Berries")
    assert "## 🥗 **Chia Seed Pudding with Berries**" in result
    assert "- **Calories:** 180 kcal" in result
    assert "- **Protein:** 7 g" in result
    assert "- **Price:** 235,000 VND" in result
    assert "- **Allergy Info:** Dairy" in result

    # Test with an invalid dish
    result = get_info("Invalid Dish")
    assert "⚠ Dish not found :((" in result

def test_add_to_cart(sample_data, monkeypatch):
    """Test the add_to_cart function, allowing multiple instances of the same dish"""
    monkeypatch.setattr("project.dish", sample_data)

    # Add a dish from Appetizers
    output = add_to_cart("Avocado and Quinoa Salad")
    assert len(cart) == 1
    assert cart[0] == ("Avocado and Quinoa Salad", 345000, 250, 8)
    assert "Avocado and Quinoa Salad: 345,000 VND" in output
    assert "Total price: 345,000 VND" in output
    assert "Total calories: 250 kcal" in output
    assert "Total protein: 8 g" in output

    # Add the same dish again (multiple times allowed)
    output = add_to_cart("Avocado and Quinoa Salad")
    assert len(cart) == 2
    assert cart[1] == ("Avocado and Quinoa Salad", 345000, 250, 8)
    assert "Avocado and Quinoa Salad: 345,000 VND" in output
    assert "Avocado and Quinoa Salad: 345,000 VND" in output  # Should appear twice
    assert "Total price: 690,000 VND" in output
    assert "Total calories: 500 kcal" in output
    assert "Total protein: 16 g" in output

    # Add a dish from Main Course
    output = add_to_cart("Chicken and Avocado Lettuce Wraps")
    assert len(cart) == 3
    assert cart[2] == ("Chicken and Avocado Lettuce Wraps", 390000, 350, 28)
    assert "Chicken and Avocado Lettuce Wraps: 390,000 VND" in output
    assert "Total price: 1,080,000 VND" in output
    assert "Total calories: 850 kcal" in output
    assert "Total protein: 44 g" in output

    # Test with invalid dish
    output = add_to_cart("Invalid Dish")
    assert "⚠ Dish not found :((" in output
    assert len(cart) == 3  # Cart should not change

    # Test with no dish selected
    output = add_to_cart(None)
    assert "⚠ Please select a dish to add to cart!!" in output
    assert len(cart) == 3  # Cart should not change

def test_clear_cart(sample_data, monkeypatch):
    """Test the clear_cart function"""
    monkeypatch.setattr("project.dish", sample_data)

    # Add some dishes to the cart
    add_to_cart("Avocado and Quinoa Salad")
    add_to_cart("Grilled Salmon with Asparagus and Sweet Potato Mash")
    assert len(cart) == 2

    # Clear the cart
    result = clear_cart()
    assert len(cart) == 0
    assert "## 🛒 **EMPTY CART**" in result
