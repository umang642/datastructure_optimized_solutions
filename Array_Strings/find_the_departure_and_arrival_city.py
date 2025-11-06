class find_departure_and_arrival_city:
    def get_the_itenary(self, cities: dict) -> str:
        # set the first city as a departure
        departure = list(cities.keys())[0]

        for city in cities:
            departure = departure + " -> " + cities[city]
        
        return departure

if __name__ == '__main__':
    cities = {'sfo': 'lax', 'lax':'chn', 'chn':'bom'}
    s = find_departure_and_arrival_city()
    print(s.get_the_itenary(cities=cities))
