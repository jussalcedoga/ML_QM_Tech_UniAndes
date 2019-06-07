from matplotlib import pyplot 
import numpy
from glob import glob
from collections import defaultdict
import matplotlib 
import cycler
from tqdm import tqdm

def main():
    L_array = [20]
    for L in L_array:
        mag_file = glob("data_tutorial3/*spinConfigs_*L{}*.txt".format(L))
        temperature_file = glob("data_tutorial3/*temperatures_*L{}*.txt".format(L))

        mag_file = numpy.loadtxt(mag_file[0])
        temperature_file = numpy.loadtxt(temperature_file[0])

        # mag_array = []
        # for i in range(2000):
        #   mag_array.append(sum(mag_file[i, :]))
        # mag_array = numpy.array(mag_array)

        # pyplot.figure()
        # pyplot.plot(temperature_file, numpy.abs(mag_array), "o")

        # pyplot.show()
        # pyplot.close()
        # print(mag_file.shape)
        # print(temperature_file.shape)

        X = mag_file
        X_mean_cols = numpy.mean(X, axis=0)
        X_c = X - X_mean_cols
        X_c_mean = numpy.mean(X_c, axis=0)

        assert numpy.allclose(X_c_mean, numpy.zeros_like(X_c_mean))


        (lamb, P) = numpy.linalg.eig(numpy.dot(X_c.T, X_c))
        X_prime = numpy.matmul(X_c, P)
        x1 = X_prime.T[0]
        x2 = X_prime.T[1]
        labels = []

        right = numpy.matmul(numpy.matmul(P, numpy.diag(lamb)), P.T)
        left = numpy.matmul(X_c.T, X_c)
        print(numpy.allclose(right, left))

        labeled_x = defaultdict(list)
        for i, t in enumerate(temperature_file):
            labeled_x[t].append((x1[i], x2[i]))

        labels = list((set(temperature_file)))

        n = len(labels) + 1
        color = pyplot.cm.jet(numpy.linspace(0, 1,n))
        matplotlib.rcParams['axes.prop_cycle'] = cycler.cycler('color', color)

        fig = pyplot.figure()
        ax = fig.add_subplot(111)

        for i, temp in enumerate(labels):
            to_plot = numpy.array(labeled_x[temp])
            ax.scatter(to_plot[:, 0], to_plot[:, 1], color=color[i])

        ax.grid()
        ax.set_xlim(-100, 100)
        ax.set_ylim(-50, 50)
        ax.set_aspect("equal")
        ax.set_ylabel(r"$x_{2}^{\prime}$", fontsize=20)
        ax.set_xlabel(r"$x_{1}^{\prime}$", fontsize=20)
        pyplot.savefig("L_{}_colorbar.pdf".format(L))
        pyplot.savefig("L_{}_colorbar.png".format(L))
        pyplot.close()

if __name__ == '__main__':
    main()