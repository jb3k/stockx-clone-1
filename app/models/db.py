from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class Apparel(db.Model):
    __tablename__= "apparels"


    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    #should this be a string?
    release_date = db.Column(db.String, nullable=False)
    brand = db.Column(db.String, nullable=False)
    style = db.Column(db.String, nullable=False)
    brand_type = db.Column(db.String, nullable=False)
    colorway = db.Column(db.String, nullable=False)
    condition = db.Column(db.String, nullable=False)
    size = db.Column(db.Integer)
    #something i need to add to the listings for new shoes
    retail_price = db.Column(db.Integer, nullable=False)
    price_sold = db.Column(db.Integer, nullable=False)
    #what if there have been none sold yet...
    quantity_sold = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.now)

    #relationships
    #one-to-many... each item can have many images, an image cannot have many items
    imgs = db.relationship("Images", back_populates="apparel", cascade="all, delete")
    #one-to-many... apparel can have many listings, but a listing can only be for 1 apparel.
    listing = db.relationship("Listings", back_populates="apparel")


    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'releaseDate': self.release_date,
            'brand': self.brand,
            'style': self.style,
            'brandType': self.brand_type,
            'colorway': self.colorway,
            'condition': self.condition,
            'size': self.size,
            'retailPrice': self.retail_price,
            'priceSold': self.price_sold,
            'quantitySold': self.quantity_sold,
            "createdAt": self.created_at,
            "updatedAt": self.updated_at,
        }
