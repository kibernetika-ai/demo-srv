import logging

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
    test_text = inputs.get('test_text')
    test_image = inputs.get('test_image')
    test_int = inputs.get('test_int')
    test_float = inputs.get('test_float')
    LOG.info(f'test_text: {test_text}')
    LOG.info(f'test_image length: {len(test_image)}')
    LOG.info(f'test_int: {test_int}')
    LOG.info(f'test_float: {test_float}')
    return {'output': '{}{}'.format(PARAMS['params_text'], test_text)}
