import requests

def get_restaurants_data(postcode):
    api_url = f"https://uk.api.just-eat.io/discovery/uk/restaurants/enriched/bypostcode/{postcode}"
    response = requests.get(api_url)
    data = response.json()
    
    restaurants = data.get('Restaurants', [])[:10]  # only first 10 restaurants
    filtered_data = []

    #fetch restaurant data
    for restaurant in restaurants:
        restaurant_data = {
            'Name': restaurant.get('Name', ''),
            'Cuisines': ', '.join(restaurant.get('Cuisines', [])),
            'Rating': restaurant.get('RatingStars', {}).get('Stars', 0),
            'Address': restaurant.get('Address', {}).get('FirstLine', '')
        }
        filtered_data.append(restaurant_data)

    return filtered_data
