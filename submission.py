import string
import matplotlib
import matplotlib.pyplot as plt


import numpy as np
import random

#construct the seed for all characters in the alphabet
v=np.random.random(26*3)
t = np.arange(0.0, 26.0*3, 1)


fig, ax = plt.subplots()
ax.plot(t, v)
ax.grid()
plt.show()
################################################


#takes input of a string and returns number values
phrase="yeet"
phraseToInt=[]
for p in phrase:
    #x=string.ascii_lowercase.index(p)
    x= ord(p)-97
    phraseToInt.append(x)
    print(x)
    ############################################


#For the given phrase, takes the values needed from the seed
requiredValues=[]
for p in phraseToInt:
    requiredValues.append(v[3*p])
    requiredValues.append(v[(3*p)+1])
    requiredValues.append(v[(3*p)+2])
requiredValues.append(np.random.random())
len(requiredValues)
#######################################################


#Constructs the Cookie Cutter!
n = len(phrase) # Number of possibly sharp edges
r = .7 # magnitude of the perturbation from the unit circle, 
# should be between 0 and 1
N = n*3+1 # number of points in the Path

angles = np.linspace(0,2*np.pi,N)
codes = np.full(N,Path.CURVE4)
codes[0] = Path.MOVETO

verts = np.stack((np.cos(angles),np.sin(angles)))
verts=verts.T*(2*r*(2*r*np.asarray(requiredValues)+1-r))[:,None]
verts[-1,:] = verts[0,:]

paths = Path(verts,codes)

fig = plt.figure()
ax = fig.add_subplot(111)
patch = patches.PathPatch(paths, facecolor='none', lw=2)
ax.add_patch(patch)

ax.set_xlim(np.min(verts)*1.1, np.max(verts)*1.1)
ax.set_ylim(np.min(verts)*1.1, np.max(verts)*1.1)
ax.axis('off') # removes the axis to leave only the shape
fig.savefig("example.pdf",bbox_inches='tight')

yoTimeToPrep=paths.vertices
paths
#################################################################



# cookie cutter constructed without any bezier curves
w=verts
path=Path(w)
fig = plt.figure()
ax = fig.add_subplot(111)
patch = patches.PathPatch(path, facecolor='none', lw=2)
ax.set_xlim(np.min(verts)*1.1, np.max(verts)*1.1)
ax.set_ylim(np.min(verts)*1.1, np.max(verts)*1.1)
ax.add_patch(patch)
w