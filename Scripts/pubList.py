import googlemaps
import time
import csv

# Replace 'YOUR_API_KEY' with your actual API key
API_KEY = 'YOUR_API_KEY'
gmaps = googlemaps.Client(key=API_KEY)

# Define the search parameters
location = 'Dublin, Ireland'
radius = 5000  # Radius in meters
place_type = 'bar'  # You can also use 'pub'

def get_pubs():
    pubs = []
    next_page_token = None

    while True:
        places_result = gmaps.places_nearby(
            location=location,
            radius=radius,
            type=place_type,
            page_token=next_page_token
        )

        for place in places_result.get('results', []):
            pubs.append({
                'name': place.get('name'),
                'address': place.get('vicinity'),
                'place_id': place.get('place_id')
            })

        next_page_token = places_result.get('next_page_token')
        if next_page_token:
            # Wait for the next page token to become valid
            time.sleep(2)
        else:
            break

    return pubs

def get_pub_details(pubs):
    for pub in pubs:
        details = gmaps.place(place_id=pub['place_id'], fields=['website'])
        pub['website'] = details.get('result', {}).get('website')
        # Respect rate limits
        time.sleep(0.1)
    return pubs

if __name__ == '__main__':
    pubs = get_pubs()
    pubs = get_pub_details(pubs)

    # Save to CSV
    with open('pubs_in_dublin.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['name', 'address', 'website']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for pub in pubs:
            writer.writerow(pub)

    print("Data saved to pubs_in_dublin.csv")