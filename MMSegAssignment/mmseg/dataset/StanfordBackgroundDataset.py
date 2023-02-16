from mmseg.registry import DATASETS
from mmseg.datasets import BaseSegDataset

@DATASETS.register_module()
class StanfordBackgroundDataset(BaseSegDataset):
	# 类别和对应的颜色
	classes = ('background', 'glomeruili')
	palette = [[128, 128, 128], [151, 189, 8]]
	METAINFO = dict(classes = classes, palette = palette)
	def __init__(self, **kwargs):
		super().__init__(img_suffix='.png', seg_map_suffix='.png', **kwargs)