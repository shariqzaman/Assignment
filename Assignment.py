# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'

#%%
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from PIL import Image as im


#%%
list1=[]
for i in range(20):
    im1=(im.open('C:\\Users\\shari\\Desktop\\Assignment\\images\\'+str(i+1)+'.jpg'))


#%%
im1=im1.resize((500,500),im.ANTIALIAS)


#%%
im1.save('resize'+str(i+1)+'.jpg')
list1.append(np.array(im1))


#%%
print(list1)


#%%



