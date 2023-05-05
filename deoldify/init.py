from deoldify import device
from deoldify.device_id import DeviceId

device.set(device=DeviceId.GPU0)


import torch

if torch.cuda.is_available():
    print('GPU available.')
else :
    print('GPU not found')


import fastai
from deoldify.visualize import *

torch.backends.cudnn.benchmark = True

colorizer = get_image_colorizer(artistic=True)


source_url = 'https://media.discordapp.net/attachments/919136025509494836/1103669921180823594/origin.png' #@param {type:"string"}
render_factor = 35  #@param {type: "slider", min: 7, max: 40}
watermarked = False #@param {type:"boolean"}

if source_url is not None and source_url !='':
    image_path = colorizer.plot_transformed_image_from_url(url=source_url, render_factor=render_factor, compare=True, watermarked=watermarked)
else:
    print('Provide an image url and try again.')
