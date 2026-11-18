from enum import Enum


class MeterProWeatherIcon(Enum):
    """Weather icons supported by the Meter Pro and Meter Pro CO2 displays."""

    NONE = 0
    SUNNY = 1
    CLOUDY = 2
    OVERCAST = 3
    LIGHT_RAIN = 4
    HEAVY_RAIN = 5
    LIGHT_SNOW = 6
    HEAVY_SNOW = 7
    # Reported until weather is first set, e.g. when no SwitchBot hub is paired.
    NOT_SET = 100
