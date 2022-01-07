#%%
import math
from function_1 import *
import matplotlib.pyplot as plt
# import argparse

'''
Mapping Method

im2col, SDK, VW-SDK

The input/output channel have to be scaled-down (8x)
ex) 3x3x128x256 -> 3x3x16x32
'''


image, kernel, ic, oc, ar, ac, method = 32, 3, 8, 16, 32, 32, 'VW-SDK'

print("="*50)
print("INFORMATION")
print("-"*30)
print("    Array   Size = {} x {}".format(ar, ac))
print("    Image   Size = {} x {}".format(image, image))
print("    Kernel  Size = {} x {}".format(kernel, kernel))
print("    Channel Size = {} x {}".format(ic, oc))
print("-"*30)

result_vw(image, kernel, ic, oc, ar, ac, method)


# %%
# import argparse

# parser = argparse.ArgumentParser(description='Set the parameters to operate VW-SDK')
# parser.add_argument('--im', default = 32, type = int, help = 'the size of the input image or activation')
# parser.add_argument('--k', default = 3, type = int, help = 'the kernel size')
# parser.add_argument('--ic', default = 64, type = int, help = 'N of input channels')
# parser.add_argument('--oc', default = 128, type = int, help = 'N of output channels')
# parser.add_argument('--ar', default = 512, type = int, help = 'N of rows of the PIM array')
# parser.add_argument('--ac', default = 512, type = int, help = 'N of columns of the PIM array')
# args = parser.parse_args()

# print("="*50)|
# print("INFORMATION")
# print("-"*30)
# print("    Array   Size = {} x {}".format(args.ar, args.ac))
# print("    Image   Size = {} x {}".format(args.im, args.im))
# print("    Kernel  Size = {} x {}".format(args.k, args.k))
# print("    Channel Size = {} x {}".format(args.ic, args.oc))
# print("-"*30)

# result(args.im, args.k, args.ic, args.oc, args.ar, args.ac)

# %%
