#!/usr/bin/python3
#Author: Matthew Yu
#pythonStructTest.py

#for the purposes of testing classes as possible C struct replacements by adding
#instance properties at runtime.

class Object:
    X = None
    Y = None
    W = None
    H = None
    Type = None

ObjectList = Object()
ObjectList.X = []
ObjectList.Y = []
ObjectList.W = []
ObjectList.H = []
ObjectList.Type = []

ObjectList.X.append(1)
ObjectList.Y.append(1)
ObjectList.Y.append(2)
ObjectList.Y.append(3)
ObjectList.W.append("hello")
ObjectList.W.append("bye")
ObjectList.H.append(0)
ObjectList.Type.append(2)

for v in ObjectList.X:
    print(v)
for v in ObjectList.Y:
    print(v)
for v in ObjectList.W:
    print(v)
for v in ObjectList.H:
    print(v)
for v in ObjectList.Type:
    print(v)
