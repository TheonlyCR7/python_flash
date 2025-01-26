from sqlalchemy import Table, or_, func

from common.database import db_connect
from app.config.config import config
from app.settings import env
from common.utils import model_to_json
from model.user import User

db_session,Base,engine = db_connect()
class Feedback(Base):
    __table__ = Table("comment", Base.metadata, autoload_with=engine)


    """
    我们需要最终给前端返回一个完整的数据
    那么最终的数据样式
    final_data_list=[{
    最上层评论的数据以及用户数据，
    replay_list:[{
        from_user:"",
        to_user:"",
        reply:""
    },{},{}]
    },{},{}]
    
    """
    def get_feedback_user_list(self,article_id):
        final_data_list = []
        # 查询文章的一级评论 ，就是那些带有楼层的，新开的评论
        feedback_list = self.find_feedback_by_article_id(article_id)
        for feedback in feedback_list:
            user = User()
            # 根据一级评论的数据，获取回复评论的评论的内容
            all_reply = self.find_reply_by_replyid(base_reply_id=feedback.id)
            feedback_user = user.find_by_userid(feedback.user_id)
            reply_list = []
            # 再根据每一条回复的评论，查询用户信息
            for reply in all_reply:
                # 用于存储当前这条原始评论的所有回复评论，如果没有回复，这个值就为空
                reply_content_with_user = {}
                from_user_data = user.find_by_userid(reply.user_id)
                # 获取回复谁的评论的用户信息
                to_user_reply_data = self.find_reply_by_id(reply.reply_id)
                to_user_data = user.find_by_userid(to_user_reply_data[0].user_id)

                reply_content_with_user["from_user"] = model_to_json(from_user_data)
                reply_content_with_user["to_user"] = model_to_json(to_user_data)
                reply_content_with_user["content"] = model_to_json(reply)
                reply_list.append(reply_content_with_user)

            # 存储每一个回复下的所有数据
            every_feedback_data = model_to_json(feedback)
            every_feedback_data.update(model_to_json(feedback_user))
            every_feedback_data["reply_list"] = reply_list
            final_data_list.append(every_feedback_data)
        return final_data_list




    def find_feedback_by_article_id(self,article_id):
        result = db_session.query(Feedback).filter_by(
            article_id=article_id,
            reply_id=0,
            base_reply_id=0
        ).order_by(
            Feedback.id.desc()
        ).all()
        return result

    def find_reply_by_replyid(self,base_reply_id):
        result = db_session.query(Feedback).filter_by(
            base_reply_id=base_reply_id
        ).order_by(
            Feedback.id.desc()
        ).all()
        return result

    def find_reply_by_id(self,id):
        result = db_session.query(Feedback).filter(
            Feedback.id == id
        ).order_by(
            Feedback.id.desc()
        ).all()
        return result

    def get_article_feedback_count(self,article_id):
        result = db_session.query(Feedback).filter_by(
            article_id=article_id,
            reply_id=0,
            base_reply_id=0
        ).count()
        return result


    # 插入一级评论
    def insert_comment(self,user_id,article_id,content,ipaddr):
        # label的意思就是重新起一个名字给字段
        feedback_max_floor = db_session.query(
            func.max(Feedback.floor_number).label("max_floor")
        ).filter_by(article_id=article_id).first()
        if feedback_max_floor.max_floor == 0 or feedback_max_floor.max_floor is None:
            feedback = Feedback(user_id=user_id,
                                article_id=article_id,
                                content=content,
                                ipaddr=ipaddr,
                                floor_number=1,
                                reply_id=0,
                                base_reply_id=0)
        else:
            feedback = Feedback(user_id=user_id,
                                article_id=article_id,
                                content=content,
                                ipaddr=ipaddr,
                                floor_number=int(feedback_max_floor.max_floor)+1,
                                reply_id=0,
                                base_reply_id=0)
        db_session.add(feedback)
        db_session.commit()
        # 做一个手动刷新就可以拿到插入的数据的值了
        # db_session.refresh()
        return feedback

    def insert_reply(self,article_id,user_id,content,ipaddr,reply_id,base_reply_id):
        feedback = Feedback(user_id=user_id,
                            article_id=article_id,
                            content=content,
                            ipaddr=ipaddr,
                            reply_id=reply_id,
                            base_reply_id=base_reply_id)
        db_session.add(feedback)
        db_session.commit()