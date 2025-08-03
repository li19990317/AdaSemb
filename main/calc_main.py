import argparse
from calc_calculator import *


def main():

	parser = argparse.ArgumentParser(description = 'RLIPP_score calculation')
	parser.add_argument('-hidden', help = 'Hidden folders path', type = str,default='../hidden')
	parser.add_argument('-ontology', help = 'Ontology file', type = str,default='../sample/ontology.txt')
	# parser.add_argument('-test', help = 'Test file', type = str,default ='../sample/test_data.txt')
	parser.add_argument('-test', help = 'Test file', type = str,default ='../test_data.txt')
	parser.add_argument('-predicted', help = 'Predicted result file', type = str, default='../result/results.txt')
	parser.add_argument('-gene2idfile', help = 'Gene-index file', type = str, default='../sample/gene2ind.txt')
	parser.add_argument('-cell2idfile', help = 'Cell-index file', type = str, default='../sample/cell2ind.txt')
	parser.add_argument('-sys_output', help = 'RLIPP file', type = str, default='../RLIPP/rlipp_socre.txt')
	parser.add_argument('-gene_output', help = 'Gene rho file', type = str, default='../RLIPP/gene_spearman.txt')
	parser.add_argument('-cpu_count', help = 'No of available cores', type = int, default = 1)
	parser.add_argument('-drug_count', help = 'No of top performing drugs', type = int, default = 38)
	parser.add_argument('-genotype_hiddens', help = 'Mapping for the number of neurons in each term in genotype parts', type = int, default = 4)

	cmd_args = parser.parse_args()

	rlipp_calculator = RLIPPCalculator(cmd_args)
	rlipp_calculator.calc_scores()


if __name__ == "__main__":
	main()


