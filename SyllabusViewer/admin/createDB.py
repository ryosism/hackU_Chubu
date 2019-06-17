from sqlalchemy import create_engine, Column, String, Integer, types
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from datetime import datetime

# ---------------------
# dbの初期設定
# ---------------------

engine = create_engine('sqlite:///user.db')  # user.db というデータベースを使うという宣言です
Base = declarative_base()  # データベースのテーブルの親です

class User(Base):  # PythonではUserというクラスのインスタンスとしてデータを扱います
    __tablename__ = 'users'  # テーブル名は users です
    id = Column(Integer, primary_key=True, unique=True)  # 整数型のid をprimary_key として、被らないようにします
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    studentID = Column(String)
    passwd = Column(String, nullable=False)

    def __repr__(self):
        return "User<{}, {}, {}, {}, {}>".format(
            self.id,
            self.name,
            self.email,
            self.studentID,
            self.passwd
        )


class Kougi(Base):
    __tablename__ = 'kougis'
    id = Column(Integer, primary_key=True, unique=True)
    title = Column(String, nullable=False)
    teacher = Column(String)

    def __repr__(self):
        return "Kougi<{}, {}, {}>".format(
            self.id,
            self.title,
            self.teacher
        )


class Review(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True, unique=True)
    kougiID = Column(Integer)
    star = Column(Integer)
    studentID = Column(Integer)
    tag1 = Column(String)
    tag2 = Column(String)
    tag3 = Column(String)
    text = Column(String)
    timeStamp = Column(types.DateTime)
    title = Column(String)

    def __repr__(self):
        return "Review<{}, {}, {}, {}, {}, {}, {}, {}, {}>".format(
            self.id,
            sekf.kougiID,
            self.studentID,
            self.title,
            self.timeStamp,
            self.text,
            self.star,
            self.tag1,
            self.tag2,
            self.tag3
        )


Base.metadata.create_all(engine)  # 実際にデータベースを構築します
SessionMaker = sessionmaker(bind=engine)  # Pythonとデータベースの経路です
session = SessionMaker()  # 経路を実際に作成しました

# -------------------
# DBにのデータを追加
# -------------------

user_ryosism = User(
    email = "ryosism@icloud.com",
    name = "ryosism",
    studentID = "TP18008",
    passwd = "alpine"
)
user_aaa = User(
    email = "aaa@example.com",
    name = "aaa",
    studentID = "EP14074",
    passwd = "alpine"
)
kougi_aaa = Kougi(
    title = "情報処理技術者演習",
    teacher = "山本公一"
)
review_aaa = Review(
    kougiID = 3,
    star = 4,
    studentID = "TP18008",
    tag1 = "簡単",
    tag2 = "寝れる",
    tag3 = "試験持ち込み可",
    text = "めっちゃ簡単に単位取れるよ",
    timeStamp = datetime.now(),
    title = "受ける価値アリ"
)

session.add(user_ryosism)
session.add(user_aaa)
session.add(kougi_aaa)
session.add(review_aaa)
session.commit()
