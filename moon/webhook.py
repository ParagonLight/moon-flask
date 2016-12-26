from moon import *
import os, subprocess

import traceback

from flask import request, abort, make_response

#################

def refresh_moon():
    ''' Refresh the code repository

    '''
    # Make webhook more lightweight
    # ret_code = subprocess.call(GIT_PULL_MOON)
    # print('execute "%s" with ret %d' % (' '.join(GIT_PULL_MOON), ret_code))

    # ret_code = subprocess.call(GIT_INIT_SUBMODULES)
    # print('execute "%s" with ret %d' % (' '.join(GIT_INIT_SUBMODULES), ret_code))

    # ret_code = subprocess.call(GIT_UPDATE_SUBMODULES)
    # print('execute "%s" with ret %d' % (' '.join(GIT_UPDATE_SUBMODULES), ret_code))

    ret_code = subprocess.call(GIT_PULL_SUBMODULES)
    print('execute "%s" with ret %d' % (' '.join(GIT_PULL_SUBMODULES), ret_code))

##################


@app.route('/gitlabwebhooks', methods=['POST','GET'])
def gitlab_webhooks():
    ''' Gitlab webhooks

    '''

    KEY = 'GITLabWebHook$'

    try:
        token = request.headers.get('X-Gitlab-Token')
    except Exception as e:
        abort(500)

    if token != KEY:
        abort(400)

    try:
        refresh_moon()
    except Exception:
        traceback.print_exc()
        abort(500)

    return make_response("", 200)


###################