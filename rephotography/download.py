import os
from huggingface_hub import hf_hub_download

def downloadModel(filename, filepath, target_path):
  print(f"path:{filepath}  name:{filename}")
  path = hf_hub_download(filepath, filename, use_auth_token=TOKEN)
  print(f"src:{path} target:{target_path}")
  file = path.split('/')[-1]
  with open(path, 'rb')as rstream:
    container = rstream.read()
    path1 = os.path.join(target_path,file)
    with open(path1, 'wb') as wstream:
        wstream.write(container)

target_path = os.getcwd()
TOKEN = "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"
modelList = [("e4e_ffhq_encode.pt", "feng2022/Time-TravelRephotography_e4e_ffhq_encode", f"{target_path}/checkpoint"),
      ("stylegan2-ffhq-config-f.pt", "feng2022/Time-TravelRephotography_stylegan2-ffhq-config-f", f"{target_path}/checkpoint"),
      ("vgg_face_dag.pt", "feng2022/Time-TravelRephotography_vgg_face_dag", f"{target_path}/checkpoint"),
      ("checkpoint_b.pt", "feng2022/Time_TravelRephotography_checkpoint_b", f"{target_path}/checkpoint/encoder"),
      ("checkpoint_g.pt", "feng2022/Time_TravelRephotography_checkpoint_g", f"{target_path}/checkpoint/encoder"),
      ("checkpoint_gb.pt", "feng2022/Time_TravelRephotography_checkpoint_gb", f"{target_path}/checkpoint/encoder"),
      ("79999_iter.pth", "feng2022/Time-TravelRephotography_79999_iter", f"{target_path}/third_party/face_parsing/res/cp")]
for model in modelList:
  downloadModel(model[0], model[1], model[2])