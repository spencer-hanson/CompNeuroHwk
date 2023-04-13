import numpy as np
import matplotlib.pyplot as plt

total_size = 100


def plot_six(a1, b1, a2, b2):
    fig, ax = plt.subplots(3, 2)
    ax[0, 0].plot(a1)
    ax[1, 0].plot(b1)
    ax[2, 0].plot(a1 + b1)

    ax[0, 1].plot(a2)
    ax[1, 1].plot(b2)
    ax[2, 1].plot(a2 + b2)

    plt.show()


def cell_a(times, values):
    response = np.zeros((total_size,))
    started = False
    len_count = 0
    prev_value = values[0]
    for t in times:
        val = values[t]
        if prev_value <= 20 <= val or val <= 20 <= prev_value:
            started = True
        prev_value = val
        if len_count == 40 or t >= total_size - 1:
            started = False

        if started:
            len_count += 1
            response[t] = 1
        else:
            response[t] = 0

    return response


def cell_b(times, values):
    response = np.zeros((total_size,))
    started = False
    len_count = 0
    prev_value = values[0]
    for t in times:
        val = values[t]
        if prev_value <= 40 <= val or val <= 40 <= prev_value:
            started = True
        prev_value = val

        if len_count == 20 or len_count >= total_size-1:
            started = False

        if started:
            response[t] = 1
            len_count += 1
        else:
            response[t] = 0
    return response


def main():
    stimulus_time_data = np.array(range(0, total_size))

    def plot_direction():
        l2r_stimulus_data = np.array(range(0, total_size))
        r2l_stimulus_data = np.array(range(total_size, 0, -1))

        a_response_l2r = np.array(cell_a(stimulus_time_data, l2r_stimulus_data))
        b_response_l2r = np.array(cell_b(stimulus_time_data, l2r_stimulus_data))

        a_response_r2l = np.array(cell_a(stimulus_time_data, r2l_stimulus_data))
        b_response_r2l = np.array(cell_b(stimulus_time_data, r2l_stimulus_data))

        plot_six(
            a_response_l2r,
            b_response_l2r,
            a_response_r2l,
            b_response_r2l
        )

    plot_direction()


if __name__ == "__main__":
    main()
