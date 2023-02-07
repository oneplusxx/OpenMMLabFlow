_base_ = ['../_base_/models/resnet18.py', '../_base_/datasets/imagenet_bs32.py', '../_base_/default_runtime.py']

model = dict(
    head=dict(
        num_classes=5,
        topk=(1,)
    ))

data = dict(
	samples_per_gpu=32,
	workers_per_gpu=2,
	train=dict(
		data_prefix='data/flower_data/train',
		ann_file='data/flower_data/train.txt',
		classes='data/flower_data/classes.txt'
	),
    val=dict(
        data_prefix='data/flower_data/val',
        ann_file='data/flower_data/val.txt',
        classes='data/flower_data/classes.txt'
    ),
)

# 定义评估⽅法
# evaluation = dict(metric_options={'topk': (1, )})
# 优化器
optimizer = dict(type='SGD', lr=0.001, momentum=0.9, weight_decay=0.0001)
optimizer_config = dict(grad_clip=None)
# 学习率策略
lr_config = dict(
	policy='step',
	step=[1])

runner = dict(type='EpochBasedRunner', max_epochs=100)

# /HOME/scz0ato/run/mmclassification/configs/resnet18
# 预训练模型
load_from =\
	'/HOME/scz0ato/run/mmclassification/checkpoints/resnet18_batch256_imagenet_20200708-34ab8f90.pth'
