# Fast-Address-Book
FastAddressBook is a simple address book application built using FastAPI, SQLite, and Python. It allows users to create, read, update, and delete addresses, as well as retrieve addresses within a specified distance from a given location.

## Getting Started
Follow these steps to get the FastAddressBook application up and running on your local machine.

## Prerequisites
* Python 3.7 or higher installed on your system.
* pip package manager installed.

## Installation

1. Clone the repository:

```
git clone https://github.com/NirajPatel07/Fast-Address-Book
cd Fast-Address-Book
```

2. Create a virtual environment (recommended):

```
python -m venv venv
```

3. Activate the virtual environment:

```
venv\Scripts\activate
```

4. Install the required Python packages:

```
pip install -r requirements.txt
```

5. Start the FastAPI application:

```
uvicorn main:app --reload
```
The application will start and be accessible at ```http://localhost:8000/docs#/```.

## API Endpoints

![Home](https://github.com/NirajPatel07/Fast-Address-Book/assets/66070865/9a8bf3e1-7b26-40fd-b281-9e4b8db1d8eb)

### 1. Create an Address

![create address](https://github.com/NirajPatel07/Fast-Address-Book/assets/66070865/fb81db47-949e-4773-9fc8-1b023465f854)

* Endpoint: /addresses/ (POST)
* Description: Create a new address with coordinates.
* Request Body (JSON):
```
{
    "name": "Address Name",
    "latitude": 37.7749,
    "longitude": -122.4194
}
```
* Response (JSON): Returns the created address.

### 2. Read an Address

![get address](https://github.com/NirajPatel07/Fast-Address-Book/assets/66070865/6c09adce-9c04-4c08-9c34-411806328ccc)

* Endpoint: /addresses/{address_id} (GET)
* Description: Retrieve an address by its ID.
* Response (JSON): Returns the address details.

### 3. Update an Address

![update addrs](https://github.com/NirajPatel07/Fast-Address-Book/assets/66070865/ce70526f-2fb7-48bf-b0c6-8ee11edf61d9)

* Endpoint: /addresses/{address_id} (PUT)
* Description: Update an existing address by its ID.
* Request Body (JSON):
```
{
    "name": "Updated Address Name",
    "latitude": 37.7749,
    "longitude": -122.4194
}
```
* Response (JSON): Returns the updated address.

### 4. Delete an Address

![delete add](https://github.com/NirajPatel07/Fast-Address-Book/assets/66070865/cb482423-c4cb-47bc-8c6c-18fecd9a9738)

* Endpoint: /addresses/{address_id} (DELETE)
* Description: Delete an address by its ID.
* Response (JSON): Returns the deleted address.

### 5. Get Addresses within a Distance

![get_distance_rage](https://github.com/NirajPatel07/Fast-Address-Book/assets/66070865/e9690ac3-5b48-4e9e-a027-9f52097bf07c)

* Endpoint: /addresses/nearby/ (GET)
* Description: Retrieve addresses within a specified distance from a given location.
* ### Query Parameters:
* latitude (float): Latitude of the location.
* longitude (float): Longitude of the location.
* distance (float): Distance in kilometers.
