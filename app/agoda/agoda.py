from schema import Hotel,Evaluate
import requests
import json
from typing import Any,List
class Agoda:
    def __init__(self):
        pass
    def __find_url_hotel(self,id:Any) -> str:   
        response = requests.post(
            url="https://www.agoda.com/api/cronos/property/review/HotelReviews",
            headers={
                "AG-Language-Locale": "vi-vn",
            },
            json={
                "hotelId":id,
	            "pageNo":5,
	            "pageSize":5,
	            "paginationSize":5
            }
        )
        response = json.loads(response.text)   
        return response['commentList']['reviewPageUrl']
    def findHotel(self,id:Any) -> Hotel:
        url = self.__find_url_hotel(id)
        # Get Referer
        response = requests.post(
            url="https://www.agoda.com/api/cronos/seo/property",
            headers={
                "AG-Language-Locale": "vi-vn",
                "Referer": f"https://www.agoda.com{url}"
            },
            json={
                "objectId":id,
                "subTypeId":1
            }
        )
        response_dict = json.loads(response.text)
        openGraphs = response_dict.get("openGraphs")
        return Hotel(
            id=id,
            name= openGraphs.get("hotelName"),
            description=openGraphs.get("description"),
            address=openGraphs.get("address") +", " +openGraphs.get("region") +", " +openGraphs.get("locality") +", "+openGraphs.get("country"),
            location=openGraphs.get("locality")
        )
    def reviewHotel(self,hotelId:Any,pageNo:int=1,pageSize:int=5,paginationSize:int=5) -> List[Evaluate]:
        response = requests.post(
            url="https://www.agoda.com/api/cronos/property/review/HotelReviews",
            headers={
                "AG-Language-Locale": "vi-vn",
            },
            json={
                "hotelId":hotelId,
	            "pageNo":pageNo,
	            "pageSize":pageSize,
	            "paginationSize":paginationSize
            }
        )
        response = json.loads(response.text)   
        return response