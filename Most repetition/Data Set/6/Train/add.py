# Python program to
# demonstrate merging of
# two files
f = []
base = 54131
for i in range(100):
        f.append(str(base+i) + ".txt")
# Creating a list of filenames
#f = ['101567.txt', '101568.txt', '101569.txt', '101570.txt', '101571.txt', '101572.txt', '101573.txt', '101574.txt', '101575.txt', '101576.txt', '101577.txt', '101578.txt', '101579.txt', '101580.txt', '101581.txt', '101582.txt', '101583.txt', '101584.txt', '101585.txt', '101586.txt', '101587.txt', '101588.txt', '101589.txt', '101590.txt', '101591.txt', '101592.txt', '101593.txt', '101594.txt', '101595.txt', '101596.txt', '101597.txt', '101598.txt', '101599.txt', '101600.txt', '101601.txt', '101602.txt', '101603.txt', '101604.txt', '101605.txt', '101606.txt', '101607.txt', '101608.txt', '101609.txt', '101610.txt', '101611.txt', '101612.txt', '101613.txt', '101614.txt', '101615.txt', '101616.txt', '101617.txt', '101618.txt', '101619.txt', '101620.txt', '101621.txt', '101622.txt', '101623.txt', '101624.txt', '101625.txt', '101626.txt', '101627.txt', '101628.txt', '101629.txt', '101630.txt', '101631.txt', '101632.txt', '101633.txt', '101634.txt', '101635.txt', '101636.txt', '101637.txt', '101638.txt', '101639.txt', '101640.txt', '101641.txt', '101642.txt', '101643.txt', '101644.txt', '101645.txt', '101646.txt', '101647.txt', '101648.txt', '101649.txt', '101650.txt', '101651.txt', '101652.txt', '101653.txt', '101654.txt', '101655.txt', '101656.txt', '101657.txt', '101658.txt', '101659.txt', '101660.txt', '101661.txt', '101662.txt', '101663.txt', '101664.txt', '101665.txt']# Open file3 in write mode
with open('All_6.txt', 'w') as outfile:

	# Iterate through list
	for names in f:

		# Open each file in read mode
		with open(names) as infile:

			# read the data from file1 and
			# file2 and write it in file3
			outfile.write(infile.read())

		# Add '\n' to enter data of file2
		# from next line
		outfile.write("\n")
