import logging

LOG = logging.getLogger(__name__)

PARAMS = {
    'prefix': 'default'
}


def init_hook(ctx, **kwargs):
    PARAMS.update(kwargs)
    LOG.info('initialize hook with params: {}'.format(PARAMS))


def update_hook(ctx, **kwargs):
    PARAMS.update(kwargs)
    LOG.info('update hook with params: {}'.format(PARAMS))


def process(inputs, ctx, **kwargs):
    inp = inputs.get('input')
    LOG.info(f'input: {inp}')
    return {'output': '{}{}'.format(PARAMS['prefix'], inp)}
