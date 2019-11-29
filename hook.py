import logging
from ml_serving.utils import helpers

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
    if 'test_image' in inputs:
        test_image, _ = helpers.load_image(inputs, 'test_image', rgb=False)
        ret['test_image_exists'] = True
        ret['test_image_type'] = str(type(test_image))
        ret['test_image_shape'] = test_image.shape
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
