import numpy as np
import pickle
import matplotlib.pyplot as plt


def question1():
    # Varation 1
    q = np.array([
        [0.2, 0.1],
        [0.1, 0.15]
    ])
    # tau*dw/dt = Qw
    # Find eigenvectors of q
    vals, vecs = np.linalg.eig(q)
    print(f"Vec: {vecs[-1]}")


def question7():
    with open("c7p7.pickle", "rb") as f:
        data = np.array(pickle.load(f)["c10p1"])
    x_mean, y_mean = np.average(data, axis=0)
    data[:, 0] -= x_mean
    data[:, 1] -= y_mean
    plt.scatter(data[:, 0], data[:, 1])
    # plt.show()

    nu = 1
    alpha = 1
    delta_t = 0.01
    w = np.random.randn(2)
    all_ws = []
    data_len = len(data)
    for i in range(0, 100000):  # Iterate 100k times
        idx = i % data_len
        u = data[idx]
        v = u.dot(w)
        new_w = w + delta_t*nu*(v*u - alpha*(v**2)*w)  # Oja
        # new_w = w + delta_t*nu*(v*u)  # Hebb
        all_ws.append(new_w)
        w = new_w

    all_ws = np.array(all_ws)

    correlation_matrix = data.T.dot(data) / data_len
    vals, vecs = np.linalg.eig(correlation_matrix)

    plt.scatter(all_ws[:, 0], all_ws[:, 1])
    # plt.scatter(vecs[:,0], vecs[:,1])
    plt.show()
    tw = 2


if __name__ == "__main__":
    # question1()
    question7()
