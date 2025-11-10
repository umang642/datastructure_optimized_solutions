class FindDepartureAndArrival:
    def get_the_departure_and_arrival_city(self, itenary: dict) -> str:
        full_itenary = []
        for city in itenary:
            if city not in full_itenary: full_itenary.append(city)
            if itenary[city] not in full_itenary: full_itenary.append(itenary[city]) 
            if city not in itenary.values():
                departure = city
                print('Departure City is ', departure)
            if itenary[city] not in itenary:
                arrival = itenary[city]
                print('Arrival City is', arrival)

        final_itenary = ' -> '.join(full_itenary)

        return final_itenary

if __name__ == '__main__':
    d = {'sfo':'lax','lax':'chn','chn':'bom'}
    s = FindDepartureAndArrival()
    print(s.get_the_departure_and_arrival_city(itenary=d))