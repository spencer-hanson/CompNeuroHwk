import numpy as np
import matplotlib.pyplot as plt
import pickle
import math


def fano_factor(data):
    return np.var(data) / np.mean(data)


def main():
    with open("c4p7.pickle", 'rb') as f:
        data = pickle.load(f)
    stim = data["stim"]
    neuron1 = data["neuron1"]
    neuron2 = data["neuron2"]
    neuron3 = data["neuron3"]
    neuron4 = data["neuron4"]
    avg_neuron1 = np.average(neuron1, 0)
    avg_neuron2 = np.average(neuron2, 0)
    avg_neuron3 = np.average(neuron3, 0)
    avg_neuron4 = np.average(neuron4, 0)

    time_interval = 10  # 10 seconds per firing rate recording in the data

    print(f"Fano Factor for Neuron1: {fano_factor(neuron1 / time_interval)}")
    print(f"Fano Factor for Neuron2: {fano_factor(neuron2 / time_interval)}")
    print(f"Fano Factor for Neuron3: {fano_factor(neuron3 / time_interval)}")
    print(f"Fano Factor for Neuron4: {fano_factor(neuron4 / time_interval)}")

    with open("c4p9.pickle", 'rb') as f:
        data2 = pickle.load(f)
    r_vecs = np.array([data2[f"r{i}"] for i in range(1, 5)])
    c_vecs = np.array([data2[f"c{i}"] for i in range(1, 5)])
    max_firing_rate_neurons = np.array([np.max(d) for d in [avg_neuron1, avg_neuron2, avg_neuron3, avg_neuron4]])
    r_vecs_avg = np.average(r_vecs, 1)

    pop_vec = sum((r_vecs_avg/max_firing_rate_neurons).reshape(4,1)*c_vecs)
    angle = math.atan(pop_vec[1]/pop_vec[0])
    degrees = angle/(2*math.pi)*360 + 360  # Convert to degrees, make value positive
    degrees = degrees % 360
    # Restructure such that the Y-axis is 90 and X is 0
    degrees = 360 - degrees  # swap from counterclockwise to clockwise
    degrees += 90  # rotate 0 deg to Y axis
    print(f"Unknown stimulius direction is {degrees} deg")
    tw = 2

    plt.plot(stim, avg_neuron1)
    plt.plot(stim, avg_neuron2)
    plt.plot(stim, avg_neuron3)
    plt.plot(stim, avg_neuron4)
    plt.legend(["n1", "n2", "n3", "n4"])
    plt.show()

    tw = 2

    # plt.plot(time, sta)
    # plt.xlabel('Time (ms)')
    # plt.ylabel('Stimulus')
    # plt.title('Spike-Triggered Average')
    #
    # plt.show()


if __name__ == "__main__":
    main()
