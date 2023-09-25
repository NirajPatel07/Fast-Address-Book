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

### 1. Create an Address
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
* Endpoint: /addresses/{address_id} (GET)
* Description: Retrieve an address by its ID.
* Response (JSON): Returns the address details.

### 3. Update an Address
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
* Endpoint: /addresses/{address_id} (DELETE)
* Description: Delete an address by its ID.
* Response (JSON): Returns the deleted address.

### 5. Get Addresses within a Distance
* Endpoint: /addresses/nearby/ (GET)
* Description: Retrieve addresses within a specified distance from a given location.
* ### Query Parameters:
* latitude (float): Latitude of the location.
* longitude (float): Longitude of the location.
* distance (float): Distance in kilometers.
