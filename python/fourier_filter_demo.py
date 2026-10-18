"""Numerical 4f spatial-filtering demonstration using a 2D FFT.

Computational companion to the experimental design; simulated output is not
presented as experimental measurement.
"""
from __future__ import annotations
import numpy as np
import matplotlib.pyplot as plt


def synthetic_target(n:int=384)->np.ndarray:
    y,x=np.mgrid[-1:1:complex(n),-1:1:complex(n)]
    target=np.zeros((n,n),float)
    target[(np.abs(x)<.58)&(np.abs(y)<.42)]=.5
    target[(np.abs(x+.18)<.018)&(np.abs(y)<.35)]=1.0
    target[(np.abs(y-.12)<.018)&(np.abs(x)<.48)]=1.0
    texture=.22*(1+np.cos(2*np.pi*18*x))
    return np.clip(target+texture*(target>0),0,1)


def frequency_grid(n:int):
    f=np.fft.fftshift(np.fft.fftfreq(n)); fy,fx=np.meshgrid(f,f,indexing='ij')
    return fx,fy,np.sqrt(fx**2+fy**2)


def masks(n:int):
    fx,fy,r=frequency_grid(n)
    low=(r<=.055).astype(float); high=(r>=.035).astype(float)
    band=((r>=.025)&(r<=.075)).astype(float); directional=(np.abs(fx)<=.015).astype(float)
    notch=np.ones((n,n)); f0=18/n
    notch[(np.sqrt((fx-f0)**2+fy**2)<.009)|(np.sqrt((fx+f0)**2+fy**2)<.009)]=0
    return {'Low-pass':low,'High-pass':high,'Band-pass':band,'Directional':directional,'Notch':notch}


def apply_filter(image,mask):
    spectrum=np.fft.fftshift(np.fft.fft2(image))
    return np.abs(np.fft.ifft2(np.fft.ifftshift(spectrum*mask)))


def make_demo():
    image=synthetic_target(); all_masks=masks(image.shape[0])
    names=['Original','Low-pass','High-pass','Band-pass','Directional','Notch']
    images=[image]+[apply_filter(image,all_masks[name]) for name in names[1:]]
    fig,axes=plt.subplots(2,3,figsize=(10,6.6))
    for ax,name,img in zip(axes.flat,names,images):
        ax.imshow(img,cmap='gray'); ax.set_title(name); ax.axis('off')
    fig.suptitle('Numerical spatial filtering in a 4f system'); fig.tight_layout(); plt.show()

if __name__=='__main__': make_demo()
