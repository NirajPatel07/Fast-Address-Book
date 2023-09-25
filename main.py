import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, Float, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from databases import Database

app = FastAPI()

# Define SQLAlchemy models
Base = declarative_base()


class AddressModel(Base):
    __tablename__ = "addresses"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, unique=True)
    latitude = Column(Float)
    longitude = Column(Float)


# Connect to the SQLite database
DATABASE_URL = "sqlite:///./address.db"
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(bind=engine)

# Create a session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a Database instance for FastAPI
database = Database(DATABASE_URL)


# Pydantic model for address creation
class AddressCreate(BaseModel):
    name: str
    latitude: float
    longitude: float


# Pydantic model for address response
class Address(BaseModel):
    id: int
    name: str
    latitude: float
    longitude: float


# API endpoints

@app.post("/addresses/", response_model=Address)
async def create_address(address: AddressCreate):
    async with database.transaction():
        query = AddressModel.__table__.insert().values(**address.dict())
        last_record_id = await database.execute(query)
        address_db = await database.fetch_one(AddressModel.__table__.select().where(AddressModel.id == last_record_id))
        return address_db


@app.get("/addresses/{address_id}", response_model=Address)
async def read_address(address_id: int):
    query = AddressModel.__table__.select().where(AddressModel.id == address_id)
    address = await database.fetch_one(query)
    if address is None:
        raise HTTPException(status_code=404, detail="Address not found")
    return address


@app.put("/addresses/{address_id}", response_model=Address)
async def update_address(address_id: int, address: AddressCreate):
    query = AddressModel.__table__.update().where(AddressModel.id == address_id).values(**address.dict())
    await database.execute(query)
    updated_address = await database.fetch_one(AddressModel.__table__.select().where(AddressModel.id == address_id))
    if updated_address is None:
        raise HTTPException(status_code=404, detail="Address not found")
    return updated_address


@app.delete("/addresses/{address_id}", response_model=Address)
async def delete_address(address_id: int):
    query = AddressModel.__table__.select().where(AddressModel.id == address_id)
    address = await database.fetch_one(query)
    if address is None:
        raise HTTPException(status_code=404, detail="Address not found")
    await database.execute(query)
    return address


@app.get("/addresses/nearby/")
async def get_addresses_within_distance(latitude: float, longitude: float, distance: float):
    # Assuming the distance is in kilometers
    # Calculate the bounding box for the given distance
    lat_range = distance / 111.32  # 1 degree latitude ≈ 111.32 km
    lon_range = distance / (111.32 * abs(latitude))  # Adjust for longitude
    min_lat, max_lat = latitude - lat_range, latitude + lat_range
    min_lon, max_lon = longitude - lon_range, longitude + lon_range

    query = AddressModel.__table__.select().where(
        AddressModel.latitude.between(min_lat, max_lat) &
        AddressModel.longitude.between(min_lon, max_lon)
    )
    addresses_within_distance = await database.fetch_all(query)
    return addresses_within_distance


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
