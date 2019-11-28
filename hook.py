import cv2
import logging
import numpy as np

LOG = logging.getLogger(__name__)

PARAMS = {
    'params_text': 'default'
}


def init_hook(ctx, **kwargs):
    PARAMS.update(kwargs)
    LOG.info('initialize hook with params: {}'.format(PARAMS))


def update_hook(ctx, **kwargs):
    PARAMS.update(kwargs)
    LOG.info('update hook with params: {}'.format(PARAMS))


def process(inputs, ctx, **kwargs):
    ret = {
        'params_text': PARAMS['params_text']
    }
    test_image = inputs.get('test_image')
    if test_image is not None:
        LOG.info('test_image:')
        LOG.info(test_image)
        test_image = cv2.imdecode(np.frombuffer(test_image, np.uint8), cv2.IMREAD_COLOR)
        ret['test_image_shape'] = test_image.shape
    test_text = inputs.get('test_text')
    if test_text is not None:
        ret['test_image'] = test_text
    test_int = inputs.get('test_int')
    if test_int is not None:
        ret['test_int'] = test_int
    test_float = inputs.get('test_float')
    if test_float is not None:
        ret['test_float'] = test_float
    return ret
