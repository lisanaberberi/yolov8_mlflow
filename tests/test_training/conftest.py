"""Fixtures module for api training. This is a configuration file designed
to prepare the tests function arguments on the test_*.py files located in
the same folder.

You can add new fixtures following the next structure:
```py
@pytest.fixture(scope="module", params=[{list of possible arguments}])
def argument_name(request):
    # You can add setup code here for your argument/fixture
    return request.param  # Argument that will be passed to the test
```
The fixture argument `request` includes the parameter generated by the
`params` list. Every test in the folder that uses the fixture will be run
at least once with each of the values inside `params` list unless specified
otherwise. The parameter is stored inside `request.param`.

When multiple fixtures are defined with more than one parameter, every tests
will run multiple times, each with one of all the possible combinations of
the generated parameters unless specified otherwise. For example, in the
following configuration:
```py
@pytest.fixture(scope="module", params=['a','b'])
def my_fixture1(request):
    return request.param

@pytest.fixture(scope="module", params=['x','y'])
def my_fixture2(request):
    return request.param
```
The for the test functions in this folder, the following combinations will
be generated:
    - Tests that use only one my_fixture1: ['a','b']
    - Tests that use only one my_fixture2: ['x','y']
    - Tests that use both: [('a','x'), ('a','y'), ('b','x'), ('b','y')]
    - Tests that use none of the fixtures: []

Be careful when using multiple fixtures with multiple parameters, as the
number of tests generated can grow exponentially.
"""
# pylint: disable=redefined-outer-name
import pytest
import os
import api

script_dir = os.path.dirname(os.path.abspath(__file__))
TEST_DATA_PATH = api.config.TEST_DATA_PATH
# Fixture for the 'task_type' parameter
@pytest.fixture(scope="module", params=["det", "seg"])
def task_type_param(request):
    return request.param


# Fixture for the 'model' parameter
@pytest.fixture(scope="module", params=["yolov8n.yaml"])
def model_param(request):
    return request.param


# Fixture for the 'data' parameter
@pytest.fixture(scope="module", params=["coco128.yaml"])
def data_param(request):
    return request.param
# Fixture for the 'pretrained' parameter
@pytest.fixture(scope="module", params=[None])
def weights_param(request):
    return request.param


# Fixture for the 'disable_wandb' parameter
@pytest.fixture(scope="module", params=[True])
def disable_wandb_param(request):
    return request.param
'''
# Fixture for the 'weight_decay' parameter
@pytest.fixture(scope="module", params=[0.001])
def weight_decay_param(request):
    return request.param
# Fixture for the 'epochs' parameter
@pytest.fixture(scope="module", params=[200])
def epochs_param(request):
    return request.param


# Fixture for the 'patience' parameter
@pytest.fixture(scope="module", params=[20])
def patience_param(request):
    return request.param


# Fixture for the 'batch' parameter
@pytest.fixture(scope="module", params=[1])
def batch_param(request):
    return request.param


# Fixture for the 'imgsz' parameter
@pytest.fixture(scope="module", params=[[800]])
def imgsz_param(request):
    return request.param


# Fixture for the 'save_period' parameter
@pytest.fixture(scope="module", params=[2])
def save_period_param(request):
    return request.param


# Fixture for the 'device' parameter
@pytest.fixture(scope="module", params=["cuda:0"])
def device_param(request):
    return request.param


# Fixture for the 'workers' parameter
@pytest.fixture(scope="module", params=[8])
def workers_param(request):
    return request.param


# Fixture for the 'resume' parameter
@pytest.fixture(scope="module", params=[False])
def resume_param(request):
    return request.param





# Fixture for the 'optimizer' parameter
@pytest.fixture(scope="module", params=["auto"])
def optimizer_param(request):
    return request.param


# Fixture for the 'seed' parameter
@pytest.fixture(scope="module", params=[123])
def seed_param(request):
    return request.param


# Fixture for the 'deterministic' parameter
@pytest.fixture(scope="module", params=[False])
def deterministic_param(request):
    return request.param


# Fixture for the 'single_cls' parameter
@pytest.fixture(scope="module", params=[False])
def single_cls_param(request):
    return request.param


# Fixture for the 'rect' parameter
@pytest.fixture(scope="module", params=[False])
def rect_param(request):
    return request.param


# Fixture for the 'cos_lr' parameter
@pytest.fixture(scope="module", params=[False])
def cos_lr_param(request):
    return request.param


# Fixture for the 'mask_ratio' parameter
@pytest.fixture(scope="module", params=[8])
def mask_ratio_param(request):
    return request.param


# Fixture for the 'dropout' parameter
@pytest.fixture(scope="module", params=[0.1])
def dropout_param(request):
    return request.param


# Fixture for the 'lr0' parameter
@pytest.fixture(scope="module", params=[0.001])
def lr0_param(request):
    return request.param


# Fixture for the 'lrf' parameter
@pytest.fixture(scope="module", params=[0.1])
def lrf_param(request):
    return request.param


# Fixture for the 'momentum' parameter
@pytest.fixture(scope="module", params=[0.9])
def momentum_param(request):
    return request.param


# Fixture for the 'warmup_epochs' parameter
@pytest.fixture(scope="module", params=[4.0])
def warmup_epochs_param(request):
    return request.param


# Fixture for the 'warmup_momentum' parameter
@pytest.fixture(scope="module", params=[0.9])
def warmup_momentum_param(request):
    return request.param


# Fixture for the 'warmup_bias_lr' parameter
@pytest.fixture(scope="module", params=[0.8])
def warmup_bias_lr_param(request):
    return request.param


# Fixture for the 'close_mosaic' parameter
@pytest.fixture(scope="module", params=[15])
def close_mosaic_param(request):
    return request.param


# Fixture for the 'amp' parameter
@pytest.fixture(scope="module", params=[False])
def amp_param(request):
    return request.param


# Fixture for the 'fraction' parameter
@pytest.fixture(scope="module", params=[0.8])
def fraction_param(request):
    return request.param


# Fixture for the 'box' parameter
@pytest.fixture(scope="module", params=[5.0])
def box_param(request):
    return request.param


# Fixture for the 'cls' parameter
@pytest.fixture(scope="module", params=[0.3])
def cls_param(request):
    return request.param


# Fixture for the 'dfl' parameter
@pytest.fixture(scope="module", params=[2.0])
def dfl_param(request):
    return request.param


# Fixture for the 'kobj' parameter
@pytest.fixture(scope="module", params=[0.8])
def kobj_param(request):
    return request.param


# Fixture for the 'label_smoothing' parameter
@pytest.fixture(scope="module", params=[0.1])
def label_smoothing_param(request):
    return request.param


# Fixture for the 'nbs' parameter
@pytest.fixture(scope="module", params=[64])
def nbs_param(request):
    return request.param


# Fixture for the 'hsv_h' parameter
@pytest.fixture(scope="module", params=[0.02])
def hsv_h_param(request):
    return request.param


# Fixture for the 'hsv_s' parameter
@pytest.fixture(scope="module", params=[0.8])
def hsv_s_param(request):
    return request.param


# Fixture for the 'hsv_v' parameter
@pytest.fixture(scope="module", params=[0.5])
def hsv_v_param(request):
    return request.param


# Fixture for the 'degrees' parameter
@pytest.fixture(scope="module", params=[5.0])
def degrees_param(request):
    return request.param


# Fixture for the 'translate' parameter
@pytest.fixture(scope="module", params=[0.7])
def translate_param(request):
    return request.param


# Fixture for the 'scale' parameter
@pytest.fixture(scope="module", params=[0.8])
def scale_param(request):
    return request.param


# Fixture for the 'shear' parameter
@pytest.fixture(scope="module", params=[10.0])
def shear_param(request):
    return request.param


# Fixture for the 'perspective' parameter
@pytest.fixture(scope="module", params=[0.001])
def perspective_param(request):
    return request.param


# Fixture for the 'flipud' parameter
@pytest.fixture(scope="module", params=[0.2])
def flipud_param(request):
    return request.param


# Fixture for the 'fliplr' parameter
@pytest.fixture(scope="module", params=[0.5])
def fliplr_param(request):
    return request.param


# Fixture for the 'mosaic' parameter
@pytest.fixture(scope="module", params=[0.8])
def mosaic_param(request):
    return request.param


# Fixture for the 'mixup' parameter
@pytest.fixture(scope="module", params=[0.1])
def mixup_param(request):
    return request.param




'''
@pytest.fixture(scope="module")
def train_kwds(
    task_type_param,
    model_param,
    disable_wandb_param,
    weights_param,
    
#    batch_size_param,
#    num_workers_param,
#    epochs_param,
#    optimizer_param,
#    loss_param,
#    seed_param,
#    deterministic_param,
#    single_cls_param,
#    rect_param,
#    cos_lr_param,
#    overlap_mask_param,
#    mask_ratio_param,
#    dropout_param,
#    lr0_param,
#    lrf_param,
#    momentum_param,
#    weight_decay_param,
#    warmup_epochs_param,
#    warmup_momentum_param,
#    warmup_bias_lr_param,
#    close_mosaic_param,
#    amp_param,
#    fraction_param,
#    profile_param,
#    box_param,
#    cls_param,
#    dfl_param,
#    kobj_param,
#    label_smoothing_param,
#    nbs_param,
#    hsv_h_param,
#    hsv_s_param,
#    hsv_v_param,
#    degrees_param,
#    translate_param,
#    scale_param,
#    shear_param,
#    perspective_param,
#    flipud_param,
#    fliplr_param,
#    mosaic_param,
#    mixup_param,

#    resume_param,
#    workers_param,
#    device_param,
#    save_period_param,
#    imgsz_param,
#    batch_param,
#    patience_param,
):
    """Fixture to return arbitrary keyword arguments for predictions."""
    train_kwds = {
        "task_type": task_type_param,
        "model": model_param,
        "disable_wandb": disable_wandb_param,
        "weights": weights_param,
       # "data": data_param,
       # "batch_size": batch_size_param,
       # "num_workers": num_workers_param,
       # "epochs": epochs_param,
       # "optimizer": optimizer_param,
       # "loss": loss_param,
       # "seed_param": seed_param,
       # "deterministic": deterministic_param,
       # "single_cls": single_cls_param,
       # "rect": rect_param,
       # "cos_lr": cos_lr_param,
       # "overlap": overlap_mask_param,
       # "mask_ratio": mask_ratio_param,
       # "dropout": dropout_param,
       # "lr0": lr0_param,
       # "lrf": lrf_param,
       # "momentum": momentum_param,
       # "weight_decay": weight_decay_param,
       # "warmup_epochs": warmup_epochs_param,
       # "warmup_momentum": warmup_momentum_param,
       # "warmup_bias_lr": warmup_bias_lr_param,
       # "close_mosaic": close_mosaic_param,
       # "amp": amp_param,
       # "fraction": fraction_param,
       # "box": box_param,
       # "cls": cls_param,
       # "dfl": dfl_param,
        #"kobj": kobj_param,
        #"label_smoothing": label_smoothing_param,
        #"nbs": nbs_param,
        #"hsv_h": hsv_h_param,
        #"hsv_s": hsv_s_param,
        #"hsv_v": hsv_v_param,
        #"degrees": degrees_param,
        #"translate": translate_param,
        #"scale": scale_param,
        #"shear": shear_param,
        #"perspective": perspective_param,
        #"flipud": flipud_param,
        #"fliplr": fliplr_param,
        #"mosaic": mosaic_param,
        #"mixup": mixup_param,
        #"resume": resume_param,
        #"workers": workers_param,
        #"device": device_param,
        #"save_period": save_period_param,
        #"imgsz": imgsz_param,
        #"batch": batch_param,
        #"patience": patience_param,
    }
    return {k: v for k, v in train_kwds.items()}


@pytest.fixture(scope="module")
def training(train_kwds):
    """Fixture to return trained model path."""
    if train_kwds["task_type"]=='seg':
        train_kwds["data"] = os.path.join(TEST_DATA_PATH,'det/data.yaml')
    elif train_kwds["task_type"]=='det':
        train_kwds["data"] = os.path.join(TEST_DATA_PATH,'seg/label.yaml')
    path=api.utils.check_paths_in_yaml(train_kwds["data"], TEST_DATA_PATH)
    assert path, "The path to the either train or validation "\
                "test data does not exist. Please provide a valid path."      
    result = api.train(**train_kwds)
    saved_model_path = str(result).split(" ")[-1].rstrip("'}")
    yield saved_model_path