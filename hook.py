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
    LOG.info(inputs)
    ret = {
        'params_text': PARAMS['params_text']
    }
    test_image = inputs.get('test_image')
    if test_image is not None:
        LOG.info('test_image:')
        LOG.info(test_image)
        LOG.info(type(test_image))
        LOG.info(test_image.shape)
        # test_image_2 = cv2.imdecode(np.array(test_image[0]), cv2.IMREAD_COLOR)
        # LOG.info(type(test_image_2))
        # ret['test_image_shape'] = test_image.shape
        ret['test_image_exists'] = True
        ret['test_image_type'] = str(type(test_image))
    test_text = inputs.get('test_text')
    if test_text is not None:
        ret['test_text'] = test_text
        ret['test_text_type'] = str(type(test_text))
    test_int = inputs.get('test_int')
    if test_int is not None:
        ret['test_int'] = test_int
        ret['test_int_type'] = str(type(test_int))
    test_float = inputs.get('test_float')
    if test_float is not None:
        ret['test_float'] = test_float
        ret['test_float_type'] = str(type(test_float))
    return ret
