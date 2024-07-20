import requests

BASE_URL = "http://127.0.0.1:5000/products"

def test_products_json():
    response = requests.get(BASE_URL, params={'source': 'json'})
    assert response.status_code == 200
    assert "Laptop" in response.text
    assert "Coffee Mug" in response.text
    print("Test Products JSON passed.")

def test_products_csv():
    response = requests.get(BASE_URL, params={'source': 'csv'})
    assert response.status_code == 200
    assert "Laptop" in response.text
    assert "Coffee Mug" in response.text
    print("Test Products CSV passed.")

def test_invalid_source():
    response = requests.get(BASE_URL, params={'source': 'invalid'})
    assert response.status_code == 400
    assert response.text == "Wrong source"
    print("Test Invalid Source passed.")

def test_products_sql():
    response = requests.get(BASE_URL, params={'source': 'sql'})
    assert response.status_code == 200
    assert "Laptop" in response.text
    assert "Coffee Mug" in response.text
    print("Test Products SQL passed.")

def test_valid_id_sql():
    response = requests.get(BASE_URL, params={'source': 'sql'})
    data = response.json()
    valid_ids = [product['id'] for product in data]
    assert 1 in valid_ids
    assert 2 in valid_ids
    print("Test valid id SQL passed.")

def test_invalid_id_sql():
    response = requests.get(BASE_URL, params={'source': 'sql'})
    data = response.json()
    invalid_ids = [product['id'] for product in data]
    assert 999 not in invalid_ids
    print("Test invalid id SQL passed.")

if __name__ == '__main__':
    test_products_json()
    test_products_csv()
    test_invalid_source()
    test_products_sql()
    test_valid_id_sql()
    test_invalid_id_sql()

