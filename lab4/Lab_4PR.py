import requests

base_url = "https://localhost:5001/api/Category"


def get_categories():
    response = requests.get(f"{base_url}/categories", verify=False)
    if response.status_code == 200:
        categories = response.json()
        for category in categories:
            print(category)
    else:
        print("Failed to retrieve categories.")


def get_category_details(category_id):
    response = requests.get(f"{base_url}/categories/{category_id}", verify=False)
    if response.status_code == 200:
        category = response.json()
        print(category)
    else:
        print("Failed to retrieve category details.")


def create_category(category_name):
    payload = {"title": category_name}
    response = requests.post(f"{base_url}/categories", json=payload, verify=False)
    print(response.status_code)
    if response.status_code == 200:
        print("Category created successfully.")
    else:
        print("Failed to create category.")


def delete_category(category_id):
    response = requests.delete(f"{base_url}/categories/{category_id}", verify=False)
    print(response.status_code)
    if response.status_code == 204:
        print("Category deleted successfully.")


def update_category_title(category_id, new_title):
    payload = {"title": new_title}  # Assuming the title field is named 'name'
    response = requests.put(f"{base_url}/{category_id}", json=payload, verify=False)
    print(response.status_code)
    if response.status_code == 200:
        print("Category title updated successfully.")
    else:
        print("Failed to update category title.")


def create_product(category_id, product_name, price):
    payload = {"title": product_name, "price": price}
    response = requests.post(
        f"{base_url}/categories/{category_id}/products", json=payload, verify=False
    )
    print(response.status_code)
    if response.status_code == 200:
        print("Product created successfully.")
    else:
        print("Failed to create product.")


def get_category_products(category_id):
    response = requests.get(
        f"{base_url}/categories/{category_id}/products", verify=False
    )
    print(response.status_code)
    if response.status_code == 200:
        products = response.json()
        for product in products:
            print(product)
    else:
        print("Failed to retrieve category products.")


# Example usage
# get_categories()
# get_category_details(1)
# create_category("TESt")
# delete_category(10)
# update_category_title(1, "Schimba")
# create_product(1, "Products3", 10)
get_category_products(1)
