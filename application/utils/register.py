# -*- coding: utf-8 -*-
try:
    from application import twoauth
except:
    import twoauth
try:
    from application.keys import TwitterKeys
    from application.models.users import DBAccess, User
except:
    from keys import TwitterKeys
    from models.users import DBAccess, User


def make_authorize_url():
    """
    登録用 URL 作成
    """
    key = TwitterKeys.consumer_key
    secret = TwitterKeys.consumer_secret
    oauth = twoauth.oauth(key, secret)
    req_token = oauth.request_token()
    url = oauth.authorize_url(req_token)
    oauth_token_secret = req_token['oauth_token_secret']
    return url, oauth_token_secret


def get_access_token(token, secret):
    """
    Access Token 取得 
    """
    ckey = TwitterKeys.consumer_key
    csecret = TwitterKeys.consumer_secret
    oauth = twoauth.oauth(ckey, csecret)
    # Request Token 組み立て
    request_token = dict(oauth_token=token, oauth_token_secret=secret)
    pin = "dummy"
    # Access Token 取得
    access_token = oauth.access_token(request_token, pin)
    print access_token
    return access_token


def save_access_token(access_token):
    """
    Access Token 保存
    """
    user_id = access_token["user_id"]
    token_key = access_token["oauth_token"]
    token_secret = access_token["oauth_token_secret"]
    DBAccess.create()
    users = User.query.filter("user_id='%s'" % user_id)
    for user in users:
        is_exist = False
        if user and user.user_id == user_id:
            is_exist = True
            user.update(token_key, token_secret)
            break
    if is_exist == False:
        newuser = User(user_id)
        newuser.update(token_key, token_secret)
        DBAccess.add(newuser)
    DBAccess.commit()
