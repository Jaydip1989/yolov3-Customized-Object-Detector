import os

images_files = []
os.chdir(os.path.join('data','obj'))
for filename in os.listdir(os.getcwd()):
    if filename.endswith(".jpg"):
        images_files.append('data/obj/'+filename)
os.chdir("..")
with open("train.txt","w") as outfile:
    for image in images_files:
        outfile.write(image)
        outfile.write('\n')
    outfile.close()
os.chdir("..")