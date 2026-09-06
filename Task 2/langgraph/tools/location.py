from pydantic import BaseModel, Field
from typing import Dict, Any
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import pytz

class LocationInput(BaseModel):
    location_name: str = Field(description="Name of the city, landmark, or country.")

def location_info_tool(location_name: str) -> Dict[str, Any]:
    """Returns country, timezone, and current local time for a given location."""
    try:
        geolocator = Nominatim(user_agent="ai_agent_geo_tool")
        location = geolocator.geocode(location_name)
        
        if not location:
            return {"error": f"Location '{location_name}' not found or invalid."}
        
        lat, lon = location.latitude, location.longitude
        
    
        address_components = location.address.split(",")
        country = address_components[-1].strip()
        

        tf = TimezoneFinder()
        tz_string = tf.timezone_at(lat=lat, lng=lon)
        
        if not tz_string:
            return {"error": "Could not determine timezone for this location."}
        

        local_tz = pytz.timezone(tz_string)
        local_time = datetime.now(local_tz).strftime("%Y-%m-%d %H:%M:%S")
        
        return {
            "location": location_name,
            "country": country,
            "timezone": tz_string,
            "current_local_time": local_time
        }
    except Exception as e:
        return {"error": str(e)}