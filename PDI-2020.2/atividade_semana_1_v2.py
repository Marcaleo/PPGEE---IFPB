# -*- coding: utf-8 -*-

"""
INSTITUTO FEDERAL DA PARAÍBA - PPGEE
  DISCIPLINA: PROCESSAMENTO DIGITAL DE IMAGENS
  DOCENTE: CARLOS DANILO MIRANDA REGIS

  DISCENTE: LEONARDO MARÇAL DA SILVA
  
  ATIVIDADE 1
"""

# -------------------------------------------------- #
import numpy as np
import cv2

# -------------------------------------------------- #
# LOAD AN IMAGE AND DISPLAY THAT
img = cv2.imread('image1.png')
cv2.imshow('Original image',img)

# LOAD AND SAVE THE SAME IMAGE WITH GRAYSCALE
img2 = cv2.imread('image1.png', cv2.IMREAD_GRAYSCALE)
cv2.imshow('Grayscale image',img2)
cv2.imwrite('Grayscale.png',img2)

# -------------------------------------------------- #
# SPLIT IMAGE INTO SEPARATED CHANNELS
B,G,R = cv2.split(img)
# CREATE MATRIX FOR BLACK (NON COLOR)
K = np.zeros_like(B)

# -------------------------------------------------- #
# SAVE THE PLANE COLOR
Bcolor = cv2.merge([B,K,K])
# DISPLAYING THE BLUE PLANE IMAGE NON COLORIZED
cv2.imshow('Blue plane non colored',B)
# DISPLAYING THE BLUE PLANE IMAGE COLORIZED
cv2.imshow('Blue plane with color',Bcolor)
# SAVE NON COLORIZES AND COLORIZED IMAGES
cv2.imwrite('BluePlane.png',B)
cv2.imwrite('BluePlaneColored.png',Bcolor)

# -------------------------------------------------- #
# SAVE THE PLANE COLOR
Gcolor = cv2.merge([K,G,K])
# DISPLAYING THE BLUE PLANE IMAGE NON COLORIZED
cv2.imshow('Green plane non colored',G)
# DISPLAYING THE BLUE PLANE IMAGE COLORIZED
cv2.imshow('Green plane with color',Gcolor)
# SAVE NON COLORIZES AND COLORIZED IMAGES
cv2.imwrite('GreenPlane.png',G)
cv2.imwrite('GreenPlaneColored.png',Gcolor)

# -------------------------------------------------- #
# SAVE THE PLANE COLOR
Rcolor = cv2.merge([K,K,R])
# DISPLAYING THE BLUE PLANE IMAGE NON COLORIZED
cv2.imshow('Red plane non colored',R)
# DISPLAYING THE BLUE PLANE IMAGE COLORIZED
cv2.imshow('Red plane with color',Rcolor)
# SAVE NON COLORIZES AND COLORIZED IMAGES
cv2.imwrite('RedPlane.png',R)
cv2.imwrite('RedPlaneColored.png',Rcolor)

# -------------------------------------------------- #
# WAIT FOR NON CRASH PYTHON KERNEL
cv2.waitKey(0)
# CLOSE ALL WINDOWS
cv2.destroyAllWindows()