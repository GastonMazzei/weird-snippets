import cv2
import matplotlib.pyplot as plt
import numpy as np
import sys


def main(names: str) -> None:
	"""
	Opens an image-type file with name equal to name_1, 2, 3, 4
	Displays it with only one call to the axis object
	"""

	# Create the figure object
	N,M = 2,2
	f, ax = plt.subplots(N,M, figsize=(30,30))

	# Iterate over the images
	for i,x in enumerate(names):

		# Open the Image	
		img = cv2.imread(x, cv2.IMREAD_GRAYSCALE)

		#***************************************************************************************************
		# WEIRD SNIPPET: list the methods, arguments, and both plotting and showing the title in one call***
		#***************************************************************************************************
		CMDS = [ 
			[
			 'imshow',		# method name 1
			  [img],		# positional arguments 1
			  {'cmap':'gray'}	# keyword arguments 1
			 ],
			 [
			  'set_title',						# method name 2
			  [f'image: "{x.split("/")[-1].split(".")[0]}"'],		# positional arguments 2
			  {}							# keyword arguments 2
			 ],
			]
		output = [_ for _ in map(lambda x: getattr(ax[i//2,i%2],x[0])(*x[1],**x[2]), CMDS)]


	# Hide axes' axis and display
	for i in range(N):
		for j in range(M):
			ax[i,j].axis('off')
	plt.show()


if __name__=='__main__':
	try:
		main(*sys.argv[1:])
	except:
		main(['images/lena.png', 'images/face_grid.png', 'images/escher_print_gallery.png', 'images/little_cross.png'])

