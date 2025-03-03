import matplotlib.pyplot as plt
import numpy as np
import csv


logging_folder = "log"
logFile = "03032025-151109_DMM6500Logging_TempDrift_50C_2h"
skipLines_number = 3


with open(f"{logging_folder}/{logFile}.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    dict = {}
    header = []
    for row in csv_reader:
        if line_count < skipLines_number:
            line_count += 1
            continue
        if line_count == skipLines_number:
            print(f'Column names are: {", ".join(row)}')
            header = row
            for i in row:
                dict[i] = []
            line_count += 1
        else:
            for i in range(len(row)):
                dict[header[i]].append(float(row[i]))
            line_count += 1
    print(f'Processed {line_count} lines.')

dict["voltage"] = np.array(dict["voltage"])

# dict["voltage"] /= (1-27.8e-6)

fig = plt.figure(figsize=(10,7))
plt.subplot(211)
plt.title("Temperature vs Time")
plt.xlabel("Time (s)")
plt.ylabel("Temperature (°C)")
plt.plot(dict["timestamp"], dict["temperature"], 'o', markersize=1)
plt.subplot(212)
plt.title("Voltage vs Time")
plt.xlabel("Time (s)")
plt.ylabel("Voltage (V)")
plt.plot(dict["timestamp"], dict["voltage"], 'o', markersize=1)
fig.tight_layout()

fig = plt.figure()
plt.title("Error vs Temperature")
plt.xlabel("Temperature (°C)")
plt.ylabel("Error (ppm)")
ppm = [(volt-5)/5*1e6 for volt in dict["voltage"]]
plt.plot(dict["temperature"], ppm, 'o', markersize=1)
plt.plot([25, 50], [-27.8, -27.8+25*2])
plt.plot([25, 50], [-27.8, -27.8-25*2])
plt.plot([25, 20], [-27.8, -27.8+5*2])
plt.plot([25, 20], [-27.8, -27.8-5*2])
fig.tight_layout()

plt.show()
