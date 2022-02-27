from floodsystem.station import MonitoringStation
from floodsystem.stationdata import update_water_levels


def stations_level_over_threshold(stations, tol):
    """
    a list of tuples (station object at which latest relative water level is 
    over tol, the relative water level at the station)
    returned list is sorted by the relative level in descending order
    """
    station_list = []
    update_water_levels(stations)

    for station in stations:
        if station.latest_level:
            relative_level = station.relative_water_level()
            if relative_level and relative_level > tol:
                station_list.append((station, relative_level))

    station_list.sort(key=lambda item: item[1], reverse=True)

    return station_list


def stations_highest_rel_level(stations, N):
    """
    Returns a list of the N stations (objects) at which the water level, 
    relative to the typical range, is highest.
    Sorted in descending order by relative level
    """

    update_water_levels(stations)

    station_list = []
    for station in stations:
        relative_level = station.relative_water_level()
        if relative_level:
            station_list.append((station))

    highest_water_level.sort(key=lambda item: item.relative_water_level(), reverse=True)
    highest_water_level = station_list[:N]
   

    return highest_water_level
