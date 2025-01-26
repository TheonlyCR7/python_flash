import json
import random
import time

from flask import Blueprint, render_template, request, session, jsonify, make_response, url_for
import logging

from app.config.config import config
from app.settings import env
from common import response_message
from common.utils import compress_image, model_to_json
from model.article import Article
from model.favorite import Favorite
from model.feedback import Feedback
from model.user import User

personal = Blueprint("personal",__name__)
@personal.before_request
def personal_before_request():
    url = request.path
    is_login = session.get("is_login")
    if url.startswith("/personal") and is_login != 'true':
        response = make_response("登录重定向",302)
        response.headers["Location"] = url_for("index.home")
        return response

@personal.route("/personal")
def personal_center():
    # url  ?type=我的评论、 我的收藏
    type_name = request.args.get("type")
    if type_name is None:
        type_name = "article"
    user_id = session.get("user_id")
    # user_id = 1
#     如果是文章
    article = Article()
    if type_name == "article":
        article_data = article.get_article_by_userid(user_id)
#     如果是收藏
    elif type_name == "favorite":
        article_data = article.get_favirite_article_by_userid(user_id)

    # 如果是评论
    elif type_name == "feedback":
        article_data = article.get_feedback_article_by_userid(user_id)

    else:
        return response_message.PersonalMessage.error("参数传递错误")
    user = User().find_by_userid(user_id)
    return render_template("personal_center.html",
                           article_data=article_data,
                           type_name=type_name,
                           active=type_name,
                           user=user)
