
# 通用的返回消息
class UserMessage():
    # 成功的返回消息
    @staticmethod
    def success(data):
        return {"status":1000,"data":data}
    # 失败的返回消息
    @staticmethod
    def error(data):
        return {"status": 1002, "data": data}

    @staticmethod
    def other(data):
        return {"status": 1001, "data": data}

# article文章的状态 就以2开头
class ArticleMessage():
    @staticmethod
    def success(data):
        return {"status":2000,"data":data}
    @staticmethod
    def save_success(article_id,data):
        return {"status":2003,"article_id":article_id,"data":data}

    @staticmethod
    def error(data):
        return {"status": 2002, "data": data}

    @staticmethod
    def other(data):
        return {"status": 2001, "data": data}


# 收藏的就以3开头
class FavoriteMessage():
    @staticmethod
    def success(data):
        return {"status":3000,"data":data}

    @staticmethod
    def error(data):
        return {"status": 3002, "data": data}

    @staticmethod
    def other(data):
        return {"status": 3001, "data": data}



# 评论的就以4开头
class FeedbackMessage():
    @staticmethod
    def success(data):
        return {"status":4000,"data":data}

    @staticmethod
    def error(data):
        return {"status": 4002, "data": data}

    @staticmethod
    def other(data):
        return {"status": 4001, "data": data}

# 个人中心的就以5开头
class PersonalMessage():
    @staticmethod
    def success(data):
        return {"status":4000,"data":data}

    @staticmethod
    def error(data):
        return {"status": 4002, "data": data}

    @staticmethod
    def other(data):
        return {"status": 4001, "data": data}
