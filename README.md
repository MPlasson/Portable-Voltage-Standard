# Portable Voltage Standard
A portable voltage reference module, based on the REF7050 chip from Ti.

![](https://github.com/MPlasson/Portable-Voltage-Standard/blob/main/enclosure/FrontView.png?raw=true)

## Features

- Stable 5V output with high accuracy (< 0.025%)
- Very low temperature coefficient (< 2ppm/°C)
- Battery powered for lowest noise & portability
- Power Good LED indicator
- Low Battery LED indicator

## Tests status

Link to test report: [TestReport](tests/index.md)

- [x] Initial bringup
- [ ] Line regulation
- [ ] Load regulation
- [x] Current consumption
- [ ] Low battery LED trigger voltage
- [x] Ambient temperature accuracy
- [x] Temperature drift [20°C - 50°C]
- [ ] Output stability (100h minimum)
