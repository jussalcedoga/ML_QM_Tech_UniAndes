from matplotlib import pyplot
from glob import glob
import numpy
import matplotlib 
import cycler
from collections import defaultdict
import os 

def main():

    files = glob("Data/*")
    n_array = sorted([int(f.split("_")[-1]) for f in files])

    markers = 5*["*", "o", "s", ">", "<", "h"]
    n = 8
    color = pyplot.cm.jet(numpy.linspace(0, 1,n))
    matplotlib.rcParams['axes.prop_cycle'] = cycler.cycler('color', color)

    fig = pyplot.figure(figsize = (16, 6))
    ax = fig.add_subplot(121)
    ax1 = fig.add_subplot(122)

    os.system("mkdir -p Results")

    files_n = defaultdict(list)
    for f in files:
        n = int(f.split("_")[1])
        files_n[n] = f

    last_acc = []
    last_cost = []
    for i, n in enumerate(n_array):
        epoch, acc, cost = numpy.loadtxt(files_n[n], unpack=True)
        last_acc.append(acc[-1])
        last_cost.append(cost[-1])
        ax.plot(epoch, acc, color = color[i], marker = markers[i], ms = 7, label = r"$ n = %i$"%n)
        ax1.plot(epoch, cost, color = color[i], marker = markers[i], ms = 7, label = r"$ n = %i$"%n)
    axes = [ax, ax1]
    for a in axes:
        a.legend(loc = "best")
        a.set_xlabel(r"$\rm{Epoch}$", fontsize=20)
        a.grid()

    ax.set_ylabel(r"$\rm{Accuracy}$", fontsize=20)
    ax1.set_ylabel(r"$\rm{Training \ Cost}$", fontsize=20)
    pyplot.tight_layout()
    pyplot.savefig("Results/varying_n.pdf")
    pyplot.close()

    fig2 = pyplot.figure(figsize = (16, 6))
    ax3 = fig2.add_subplot(121)
    ax4 = fig2.add_subplot(122)
    ax3.plot(n_array, last_acc, "-s", ms = 8)
    ax4.plot(n_array, last_cost, "-s", ms = 8)

    ax_ = [ax3, ax4]
    for a_ in ax_:
        a_.legend(loc = "best")
        a_.set_xlabel(r"$\rm{n}$", fontsize=20)
        a_.grid()

    ax3.set_ylabel(r"$\rm{Accuracy}$", fontsize=20)
    ax4.set_ylabel(r"$\rm{Training \ Cost}$", fontsize=20)
    pyplot.tight_layout()
    pyplot.savefig("Results/converged.pdf")
    pyplot.close()

if __name__ == '__main__':
    main()