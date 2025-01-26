from sqlalchemy import Table, or_

from common.database import db_connect
from app.config.config import config
from app.settings import env
from model.user import User

db_session,Base,engine = db_connect()
class Favorite(Base):
    __table__ = Table("favorite", Base.metadata, autoload_with=engine)

    def update_status(self,article_id,user_id,canceled=0):
        # canceled的值为0的意思就是收藏，为1的意思就是取消收藏
        # 查询一下这个用户是否收藏过，如果没有收藏，那么就插入数据，如果收藏过，那么就更新数据
        favorite_data = db_session.query(Favorite).filter_by(
            article_id=article_id,
            user_id=user_id
        ).first()
        if favorite_data is None:
            favorite = Favorite(
                article_id=article_id,
                user_id=user_id,
                canceled=canceled
            )
            db_session.add(favorite)
        else:
            favorite_data.canceled=canceled
        db_session.commit()

# 查询某个用户是否收藏
    def user_if_favorite(self,user_id,article_id):
        result = db_session.query(Favorite.canceled).filter_by(
            user_id=user_id,
            article_id=article_id
        ).first()
        if result is None:
            return 1
        else:
            return result[0]