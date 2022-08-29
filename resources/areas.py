# Flask RESTful
from flask import jsonify, request
from flask_restful import Resource
from models.area import Area
from schemas.area import area_schema, areas_schema

class AreaListResource(Resource):
    def get(self):
        areas = Area.query.all()
        return areas_schema.dump(areas)

    def post(self):
        """ new_station = Station(
            abbr=request.json["abbr"],
            name=request.json["name"],
            gtfs_latitude=request.json["gtfs_latitude"],
            gtfs_longitude=request.json["gtfs_longitude"],
            address=request.json["address"],
            city=request.json["city"],
            county=request.json["county"],
            state=request.json["state"],
            zipcode=request.json["zipcode"],
        )
        db.session.add(new_station)
        db.session.commit()
        return station_schema.dump(new_station) """
      

class AreaResource(Resource):
    def get(self, area_id):
        station = Area.query.get_or_404(area_id)
        return area_schema.dump(station)

    def patch(self, area_id):
        """station = Station.query.get_or_404(station_id)
        db.session.commit()
        return station_schema.dump(station) """
        pass

    def delete(self, area_id):
        """ station = Station.query.get_or_404(station_id)
        db.session.delete(station)
        db.session.commit()
        return "", 204 """
        pass
