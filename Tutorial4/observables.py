import numpy

def main():
	results = "Data_ising2d/RBM_samples/samples_nH4_L4_T2.269.txt"
	L = 4
	configs = numpy.loadtxt(results)
	sum_ = numpy.abs(numpy.sum(configs, axis = 1))
	mean_sum = numpy.mean(sum_)/L**2
	print(mean_sum)
	# X = (numpy.mean(sum_ ** 2) - numpy.mean(sum_)**2) / (2.269 * L**2)
	# mag = mean_sum/L**2
	# print(X)
if __name__ == '__main__':
	main()