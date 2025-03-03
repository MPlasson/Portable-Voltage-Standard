# Portable Voltage Standard: Tests results

## Line regulation
## Load regulation
## Current consumption
When using the alternate power input (through the push-in connector) the board draws around 11mA, which is reasonable.

This should give us an approximate battery life of 500h (considering a typical 9V battery with a cutoff voltage of 6V).

## Low battery LED trigger voltage
## Ambient temperature accuracy

At ambient temperature (~21°C) the output voltage is close to 4.99982V, which corresponds to an error of around 36ppm. Not bad for a ±0.025% (250ppm) chip !

## Temperature drift [20°C - 50°C]
The PVS was put in a small thermal chamber and the temperature was set to around 55°C.
Both the output voltage and the ambient temperature were recorded (respectively with a DMM6500 and a class A PT100 RTD)

The temperature & output voltage profile is in the figure below:
![](https://github.com/MPlasson/Portable-Voltage-Standard/blob/main/tests/temperatureStability/03032025_TempVoltProfile.png?raw=true)

By plotting output voltage deviation (relative to a perfect 5V) relative to he temperature, we get the following picture:
![](https://github.com/MPlasson/Portable-Voltage-Standard/blob/main/tests/temperatureStability/03032025_ErrorVsTemp.png?raw=true)

Each line beginning at 25°C has a slope of ±2ppm/°C, which corresponds to the Ti specification. Out prototype is inside the limits for common lab temperatures.
## Output stability (100h minimum)
