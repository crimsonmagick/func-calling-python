def tools():
    return [
        {
            "type": "function",
            "function": {
                "name": "search",
                "description": "Searches for hotels that match the provided criteria. Call this when you need to find hotels based on geographic criteria, for example when a user asks \"Which hotels are available in Phoenix, AZ?\"",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "hotel_name": {
                            "type": "string",
                            "description": "The name of the hotel."
                        },
                        "city": {
                            "type": "string",
                            "description": "The city in proximity of the hotel."
                        },
                        "state": {
                            "type": "string",
                            "description": "The state code of the state the hotel is located in."
                        },
                        "country": {
                            "type": "string",
                            "description": "The country code of the country the hotel is located in."
                        },
                        "latitude": {
                            "type": "number",
                            "description": "The latitude in proximity of the hotel's location. If provided, a corresponding latitude should be also be provided."
                        },
                        "longitude": {
                            "type": "number",
                            "description": "The latitude in proximity of the hotel's location. If provided, a corresponding latitude should be also be provided."
                        }
                    },
                    "required": [],
                    "additionalProperties": False
                }
            }
        }
    ]
