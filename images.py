from PIL import Image,ImageFilter
import sys
import os
from PIL import Image
folder = sys.argv[1]
new_fold = sys.argv[2]
if not folder.endswith('\\') and not folder.endswith('\\'):
	folder = folder + '\\'
	new_fold = new_fold + '\\'




if not os.path.exists(new_fold):
	os.makedirs(new_fold)

for filename in os.listdir(folder):
	img = Image.open(f'{folder}{filename}')
	clean_name = os.path.splitext(filename)[0]
	img.save(f'{new_fold}{clean_name}.png','png')


