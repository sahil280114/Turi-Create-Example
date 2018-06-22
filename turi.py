import turicreate as tc 
import os

data = tc.image_analysis.load_images('dataset',with_path=True)

data['hero-name'] = data['path'].apply(lambda path: os.path.basename(os.path.dirname(path)))

data.save('turi.sframe')
data.explore()