# The new config inherits a base config to highlight the necessary modification
_base_ = ['downloads/detr_r50_8x2_150e_coco.py']

# We also need to change the num_classes in head to match the dataset's annotation
model = dict(
    bbox_head=dict(
        num_classes=13)
)
# Modify dataset related settings
dataset_type = 'COCODataset'
classes = ('bishop',
    'black-bishop',
    'black-king',
    'black-knight',
    'black-pawn',
    'black-queen',
    'black-rook',
    'white-bishop',
    'white-king',
    'white-knight',
    'white-pawn',
    'white-queen',
    'white-rook')
data_root = 'data/chess/'

data = dict(
    train=dict(
        img_prefix='data/chess/train/',
        classes=classes,
        ann_file='data/chess/train/_annotations.coco.json'),
    val=dict(
        img_prefix='data/chess/valid/',
        classes=classes,
        ann_file='data/chess/valid/_annotations.coco.json'),
    test=dict(
        img_prefix='data/chess/test/',
        classes=classes,
        ann_file='data/chess/test/_annotations.coco.json',
    )
)

runner = dict(type='EpochBasedRunner', max_epochs=100)
checkpoint_config = dict(interval=3)