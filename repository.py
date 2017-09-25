from peewee import *
from playhouse.sqlite_ext import SqliteExtDatabase

db = SqliteExtDatabase('data/database.db')


class BaseModel(Model):
    class Meta:
        database = db


class Video(BaseModel):
    id = IntegerField(primary_key=True)
    view_id = CharField(null=True, unique=True)
    title = CharField(null=True, default=0)
    img_url = CharField(null=True)
    download_url = CharField(null=True, default=0)
    vid = CharField(null=True)
    vno = CharField(null=True)
    vtime = CharField(null=True)
    user_name = CharField(null=True)
    user_no = CharField(null=True)
    downloaded = IntegerField(default=0)


class VideoSource(BaseModel):
    id = IntegerField(primary_key=True)
    view_id = CharField(null=True, unique=True)
    title = CharField(null=True, default=0)
    img_url = CharField(null=True)
    download_url = CharField(null=True, default=0)
    vid = CharField(null=True)
    vno = CharField(null=True)
    vtime = CharField(null=True)
    user_name = CharField(null=True)
    user_no = CharField(null=True)
    downloaded = IntegerField(default=0)


try:
    db.connect()
    db.create_tables([Video])
except OperationalError:
    pass

try:
    db.create_tables([VideoSource])
except OperationalError:
    pass


def persist_video(video_info):
    try:
        if video_info is None:
            return None
        video = Video.get(Video.view_id == video_info['view_id'])
        # print('{} exist, skip'.format(video_info['view_id']))
    except Video.DoesNotExist:
        video = Video.create(**video_info)
        # print('save {}, success'.format(video_info['view_id']))

    return video


def persist_video_source(video_info):
    try:
        if video_info is None:
            return None
        video = VideoSource.get(VideoSource.view_id == video_info['view_id'])
        # print('{} exist, skip'.format(video_info['view_id']))
    except VideoSource.DoesNotExist:
        video = VideoSource.create(**video_info)
        # print('save {}, success'.format(video_info['view_id']))

    return video
