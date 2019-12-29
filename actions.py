from rasa_sdk import Action


def get_restaurants(restaurant=None, cuisine=None):
    restaurants = [
        {
            "id": 0,
            "name": "سپائس بازار",
            "cuisine": "دیسی",
            "price-range": "mid-range"
        },
        {
            "id": 1,
            "name": "دی لکھنوی",
            "cuisine": "دیسی",
            "price-range": "cheap"
        },
        {
            "id": 2,
            "name": "انداز ریسٹورنٹ",
            "cuisine": "English",
            "price-range": "mid-range"
        },
        {
            "id": 3,
            "name": "آر کیڈین کیفے",
            "cuisine": "اٹالین",
            "price-range": "cheap"
        },
        {
            "id": 4,
            "name": "پاستا لا وستا",
            "cuisine": "اٹالین",
            "price-range": "mid-range"
        },
        {
            "id": 5,
            "name": "لاہور چٹخارہ",
            "cuisine": "دیسی",
            "price-range": "mid-range"
        },
        {
            "id": 6,
            "name": "واسابی",
            "cuisine": "English",
            "price-range": "cheap"
        }
    ]
    if cuisine:
        return [restaurant for restaurant in restaurants if
                restaurant['cuisine'] == cuisine], "یہ ہیں کچھ مشہور {} ریسٹورنٹس".format(cuisine)
    else:
        return restaurants, "یہ ہیں کچھ مشہور ریسٹورنٹس"


def get_hotels():
    hotels = [
        {
            "id": 0,
            "name": "پی سی ہوٹل",
            "price-range": "expensive",
            "city": "Lahore",
            "star-rating": 5,

        },
        {
            "id": 1,
            "name": "دی نشاط ہوٹل",
            "price-range": "expensive",
            "city": "Lahore",
            "star-rating": 4,
        },
        {
            "id": 2,
            "name": "فیملی ہوٹل",
            "price-range": "mid-range",
            "city": "Lahore",
            "star-rating": 4,
        },
        {
            "id": 3,
            "name": "سٹپ ان ہوٹل",
            "price-range": "mid-range",
            "city": "Lahore",
            "star-rating": 4,
        },
        {
            "id": 4,
            "name": "لاہور پیلس ہوٹل",
            "price-range": "expensive",
            "city": "Lahore",
            "star-rating": 4,
        }
    ]
    return hotels, "یہ ہیں کچھ مشہور ہوٹلز"


# def get_cuisine(cuisine):
# restaurants = get_restaurants()
# return [restaurant for restaurant in restaurants if restaurant['cuisine'] == cuisine]


class ActionQueryDatabase(Action):
    def name(self):
        return "action_query_database"

    def run(self, dispatcher, tracker, domain):
        restaurant = tracker.get_slot("restaurant")
        hotel = tracker.get_slot("hotel")
        cuisine = tracker.get_slot("cuisine")
        results = [{"name": "دی لکھنوی"}]
        message = ""
        if restaurant or cuisine:
            results, message = get_restaurants(restaurant=restaurant, cuisine=cuisine)
        elif hotel:
            results, message = get_hotels()
        dispatcher.utter_message(message)
        # limit to top 5 queries
        for i, obj in enumerate(results[:5]):
            dispatcher.utter_message(str(i + 1) + " - " + obj['name'])

        return []

# class ActionQueryCuisine(Action):
#     def name(self):
#         return "action_query_cuisine"
#
#     def run(self, dispatcher, tracker, domain):
#         cuisine = tracker.get_slot("cuisine")
#
#         results = get_cuisine(cuisine)
#
#         dispatcher.utter_message("یہ ہیں کچھ مشہور {} ریسٹورنٹس".format(cuisine))
#         # limit to top 5 queries
#         for i, obj in enumerate(results[:3]):
#             dispatcher.utter_message(str(i+1) + " - " + obj['name'])
#
#         return []
