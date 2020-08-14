from flask import Flask
from flask import request, redirect
from flask import render_template, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import LoginManager, UserMixin, login_required, login_user

from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy import UniqueConstraint

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'a really really really really long secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///article.db'

db = SQLAlchemy(app)
app.secret_key = 'some secret salt228'
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
coaches = []
coaches.append('gerard.ismagilov@mail.ru')

class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    intro = db.Column(db.String(300), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    creators = db.Column(db.String(300), nullable=False)
    type = db.Column(db.String(300), nullable=False)
    cost = db.Column(db.Integer, nullable=False)


    def __repr__(self):
        return '<Article %r>' % self.id


class Blog(db.Model):
    __tablename__ = 'blog'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)

    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Blog %r>' % self.id


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role')

    def __repr__(self):
        return '<Role %r>' % self.name


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(128), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(64))
    surname = db.Column(db.String(64))
    intro = db.Column(db.String(400))
    text = db.Column(db.Text())

    sport = db.Column(db.String(100))

    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    # login1 = 'Misha2admin@nimda.piz'
    # password1 = 'pizzza4you2nah7Ui'


class Follow(db.Model):
    __tablename__ = 'follow'
    id = db.Column(db.Integer, primary_key=True)
    follower_login = db.Column(db.String(300), nullable=False)
    followed_login = db.Column(db.String(300), nullable=False)

    def __repr__(self):
        return '<Follow %r>' % self.name


class Saved(db.Model):
    __tablename__ = 'saved'
    id = db.Column(db.Integer, primary_key=True)
    saver_login = db.Column(db.String(300), nullable=False)
    saved_login = db.Column(db.String(300), nullable=False)
    id_post = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Saved %r>' % self.name


class WeekSaved(db.Model):
    __tablename__ = 'weeksaved'
    id = db.Column(db.Integer, primary_key=True)
    saver_login = db.Column(db.String(300), nullable=False)
    saved_login = db.Column(db.String(300), nullable=False)
    id_post = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<WeekSaved %r>' % self.name



class XXLSaved(db.Model):
    __tablename__ = 'xxlsaved'
    id = db.Column(db.Integer, primary_key=True)
    saver_login = db.Column(db.String(300), nullable=False)
    saved_login = db.Column(db.String(300), nullable=False)
    id_post = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<XXLSaved %r>' % self.name




class XXLtrainer(db.Model):
    __tablename__ = 'xxltrainer'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    intro = db.Column(db.String(300), nullable=False)
    text1 = db.Column(db.Text, nullable=False)
    text2 = db.Column(db.Text, nullable=False)
    text3 = db.Column(db.Text, nullable=False)
    text4 = db.Column(db.Text, nullable=False)
    text5 = db.Column(db.Text, nullable=False)
    text6 = db.Column(db.Text, nullable=False)
    text7 = db.Column(db.Text, nullable=False)
    text8 = db.Column(db.Text, nullable=False)
    text9 = db.Column(db.Text, nullable=False)
    text10 = db.Column(db.Text, nullable=False)
    text11 = db.Column(db.Text, nullable=False)
    text12 = db.Column(db.Text, nullable=False)
    text13 = db.Column(db.Text, nullable=False)
    text14 = db.Column(db.Text, nullable=False)
    text15 = db.Column(db.Text, nullable=False)
    text16 = db.Column(db.Text, nullable=False)
    text17 = db.Column(db.Text, nullable=False)
    text18 = db.Column(db.Text, nullable=False)
    text19 = db.Column(db.Text, nullable=False)
    text20 = db.Column(db.Text, nullable=False)
    text21 = db.Column(db.Text, nullable=False)
    text22 = db.Column(db.Text, nullable=False)
    text23 = db.Column(db.Text, nullable=False)
    text24 = db.Column(db.Text, nullable=False)
    text25 = db.Column(db.Text, nullable=False)
    text26 = db.Column(db.Text, nullable=False)
    text27 = db.Column(db.Text, nullable=False)
    text28 = db.Column(db.Text, nullable=False)
    text29 = db.Column(db.Text, nullable=False)
    text30 = db.Column(db.Text)
    text31 = db.Column(db.Text)
    compulsory = db.Column(db.Text)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    creators = db.Column(db.String(300), nullable=False)
    type = db.Column(db.String(300), nullable=False)
    cost = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<XXLtrainer%r>' % self.id


class Weektrainer(db.Model):
    __tablename__ = 'weektrainer'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    intro = db.Column(db.String(300), nullable=False)
    text1 = db.Column(db.Text, nullable=False)
    text2 = db.Column(db.Text, nullable=False)
    text3 = db.Column(db.Text, nullable=False)
    text4 = db.Column(db.Text, nullable=False)
    text5 = db.Column(db.Text, nullable=False)
    text6 = db.Column(db.Text, nullable=False)
    text7 = db.Column(db.Text, nullable=False)

    date = db.Column(db.DateTime, default=datetime.utcnow)
    creators = db.Column(db.String(300), nullable=False)
    type = db.Column(db.String(300), nullable=False)
    cost = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Weektrainer%r>' % self.id


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route("/")
def index():
    try:
        base = ""
        print(11111)
        print(session.get('role'))
        if session.get('role') == "coach":
            base = "baseforaccaunt.html"
        if session.get('role') == "":
            base = "base.html"
        if session.get('role') == "sportsmen":
            base = "baseforsporsman.html"
        articles = Blog.query.order_by(Blog.date.desc()).all()
        return render_template("index.html", articles=articles, base=base)
    except:
        base = "base.html"
        print(911)
        articles = Blog.query.order_by(Blog.date.desc()).all()
        return render_template("index.html", articles=articles, base=base)


@app.route("/about")
def about():
    return render_template("about-us.html")



@app.route("/exit")
def exit():
    session['login'] = ""
    session['id'] = 0
    session['role'] = ""

    return redirect("/")


@app.route("/contacts")
def contacts():
    try:
        base = ""
        print(11111)
        print(session.get('role'))
        if session.get('role') == "coach":
            base = "baseforaccaunt.html"
        if session.get('role') == "":
            base = "base.html"
        if session.get('role') == "sportsmen":
            base = "baseforsporsman.html"
        return render_template("contact.html", base=base)
    except:
        base = "base.html"
        print(911)
        return render_template("contact.html", base=base)




@app.route("/offer/<int:id>")
def offer(id):
    article = Article.query.get_or_404(id)
    saved = Saved(saver_login=article.creators, saved_login=session.get('login'), id_post=article.id)

    try:
        db.session.add(saved)
        db.session.commit()
        return redirect("/treaning")
    except:
        return "Авторизуйтесь"


@app.route("/reject/<int:id>")
def reject(id):
    saved = Saved.query.filter_by(id_post=id, saved_login=session.get('login')).first()

    try:
        db.session.delete(saved)
        db.session.commit()
        return redirect("/treaning")
    except:
        return "Авторизуйтесь"


@app.route("/weekoffer/<int:id>")
def weekoffer(id):
    print(id)
    article = Weektrainer.query.get_or_404(id)
    saved = WeekSaved(saver_login=article.creators, saved_login=session.get('login'), id_post=article.id)

    try:
        db.session.add(saved)
        db.session.commit()
        return redirect("/weektraining")
    except:
        return "Авторизуйтесь"


@app.route("/weekreject/<int:id>")
def weekreject(id):
    saved = WeekSaved.query.filter_by(id_post=id, saved_login=session.get("login")).first()

    try:
        db.session.delete(saved)
        db.session.commit()
        return redirect("/weektraining")
    except:
        return "Авторизуйтесь"


@app.route("/XXLoffer/<int:id>")
def xxloffer(id):
    print(id)
    article = XXLtrainer.query.get_or_404(id)
    saved = XXLSaved(saver_login=article.creators, saved_login=session.get('login'), id_post=article.id)

    try:
        db.session.add(saved)
        db.session.commit()
        return redirect("/XXLtraining")
    except:
        return "Авторизуйтесь"


@app.route("/XXLreject/<int:id>")
def xxlreject(id):
    saved = XXLSaved.query.filter_by(id_post=id, saved_login=session.get("login")).first()

    try:
        db.session.delete(saved)
        db.session.commit()
        return redirect("/XXLtraining")
    except:
        return "Авторизуйтесь"


@app.route("/edit", methods=["POST", "GET"])
def edit():
    if request.method == 'POST':
        login = session.get('id')
        user = User.query.get(login)
        user.name = request.form['name']
        user.surname = request.form['surname']
        user.sport = request.form['sport']
        user.intro = request.form['intro']
        user.text = request.form['text']

        db.session.commit()
        return redirect("/account")
    else:
        return render_template("edit.html")


@app.route("/registration", methods=["POST", "GET"])
def registrations():
    if request.method == 'POST':
        login = request.form['email']
        password = request.form['password']
        password2 = request.form['password2']
        who = request.form['who']
        print(password)

        if len(password) < 8:
            flash("Пароль должен быть больше 8 знаков")
            return render_template('registration.html')
        print(22334566666666666666666666666666666)

        user = User.query.filter_by(login=login).first()
        if user:

            return redirect("/error-with-registration")
        elif not (login or password or password2):
            flash("Please, fill all fields!")
        elif password != password2:
            flash('Password is not equale!')
        else:

            print("wtf")
            hash_pwd = generate_password_hash(password)
            print("doublewtf")
            new_user = User(login=login, password=hash_pwd, role_id=who, name="  ", surname="  ", sport=" ", intro=" ",
                            text=" ")
            print("wtfwtf")
            db.session.add(new_user)
            db.session.commit()

            return redirect("/login")

    return render_template('registration.html')


@app.route("/create-article", methods=['POST', 'GET'])
@login_required
def create_article():

    if request.method == 'POST':
        title = request.form['title']
        intro = request.form['intro']
        text = request.form['text']
        who = request.form['who']
        cost = request.form['cost']
        user = User.query.filter_by(login=session.get('login')).first()
        print(user.role_id)
        if user.role_id == "sportsmen":
            return "Вы не тренер"
        if who == "free":
            who = "Бесплатная"
            cost = 0
        else:
            who = "Платная"

        article = Article(title=title, intro=intro, text=text, creators=session.get('login'), type=who, cost=cost)
        try:
            db.session.add(article)
            db.session.commit()
            return redirect("/account")
        except:
            return "При добавлении статьи произошла ошибка!"
    else:
        user = User.query.filter_by(login=session.get('login')).first()
        print(user.role_id)
        if user.role_id == "sportsmen":
            return "Вы не тренер"
        return render_template("create-article.html")


@app.route("/create-weekarticle", methods=['POST', 'GET'])
@login_required
def create_weekarticle():
    if request.method == 'POST':
        title = request.form['title']
        intro = request.form['intro']
        text1 = request.form['text1']
        text2 = request.form['text2']
        text3 = request.form['text3']
        text4 = request.form['text4']
        text5 = request.form['text5']
        text6 = request.form['text6']
        text7 = request.form['text7']
        who = request.form['who']
        cost = request.form['cost']
        user = User.query.filter_by(login=session.get('login')).first()
        print(user.role_id)
        if user.role_id == "sportsmen":
            return "Вы не тренер"
        if who == "free":
            who = "Бесплатная"
            cost = 0

        else:
            who = "Платная"

        article = Weektrainer(title=title, intro=intro, text1=text1, text2=text2, text3=text3, text4=text4, text5=text5,
                              text6=text6, text7=text7, creators=session.get('login'), type=who, cost=cost)
        print("ok")

        db.session.add(article)
        db.session.commit()
        return redirect("/account")

    else:
        user = User.query.filter_by(login=session.get('login')).first()
        print(user.role_id)
        if user.role_id == "sportsmen":
            return "Вы не тренер"
        return render_template("create-weekarticle.html")




@app.route("/create-XXLtrainer", methods=['POST', 'GET'])
@login_required
def create_XXL():
    if request.method == 'POST':
        title = request.form['title']
        intro = request.form['intro']
        text1 = request.form['text1']
        text2 = request.form['text2']
        text3 = request.form['text3']
        text4 = request.form['text4']
        text5 = request.form['text5']
        text6 = request.form['text6']
        text7 = request.form['text7']
        text8 = request.form['text8']
        text9 = request.form['text9']
        text10 = request.form['text10']
        text11 = request.form['text11']
        text12 = request.form['text12']
        text13 = request.form['text13']
        text14 = request.form['text14']
        text15 = request.form['text15']
        text16 = request.form['text16']
        text17 = request.form['text17']
        text18 = request.form['text18']
        text19 = request.form['text19']
        text20 = request.form['text20']
        text21 = request.form['text21']
        text22 = request.form['text22']
        text23 = request.form['text23']
        text24 = request.form['text24']
        text25 = request.form['text25']
        text26 = request.form['text26']
        text27 = request.form['text27']
        text28 = request.form['text28']
        text29 = request.form['text29']
        text30 = request.form['text30']
        text31 = request.form['text31']
        who = request.form['who']
        cost = request.form['cost']
        print("WTF")
        user = User.query.filter_by(login=session.get('login')).first()
        print(user.role_id)
        if user.role_id == "sportsmen":
            return "Вы не тренер"
        if who == "free":
            who = "Бесплатная"
            cost = 0

        else:
            who = "Платная"

        article = XXLtrainer(title=title, intro=intro, text1=text1, text2=text2, text3=text3, text4=text4, text5=text5, text6=text6, text7=text7, text8=text8, text9=text9, text10=text10,
                             text11=text11, text12=text12, text13=text13, text14=text14, text15=text15, text16=text16, text17=text17, text18=text18, text19=text19, text20=text20,
                             text21=text21, text22=text22, text23=text23, text24=text24, text25=text25, text26=text26, text27=text27, text28=text28, text29=text29, text30=text30,
                             text31=text31, creators=session.get('login'), type=who, cost=cost)
        print("ok")

        db.session.add(article)
        db.session.commit()
        return redirect("/account")

    else:
        user = User.query.filter_by(login=session.get('login')).first()
        print(user.role_id)
        if user.role_id == "sportsmen":
            return "Вы не тренер"
        return render_template("create-XXLtrainer.html")







@app.route("/create-blog", methods=['POST', 'GET'])
@login_required
def create_blog():
    user = User.query.filter_by(login=session.get('login')).first()
    print(user.role_id)
    if user.role_id == "sportsmen":
        return "Вы не тренер"
    if request.method == 'POST':
        title = request.form['title']

        text = request.form['text']

        article = Blog(title=title, text=text)
        if session.get('login') == 'gerard.ismagilov@mail.ru':
            db.session.add(article)
            db.session.commit()
            return redirect("/account")
        else:
            return "У вас пока нет прав, чтобы вы могли создавать новости"

    else:

        return render_template("create-blog.html")


@app.route("/login", methods=['POST', 'GET'])
def login_page():
    if request.method == 'POST':
        login = request.form['login']
        password = request.form['password']

        user = User.query.filter_by(login=login).first()
        if user and check_password_hash(user.password, password):
            login_user(user)

            if user.role_id == "coach":
                session['login'] = login
                session['id'] = user.id
                session['role'] = user.role_id
                return redirect("/account")
            else:
                session['login'] = login
                session['id'] = user.id
                session['role'] = user.role_id
                return redirect("/sportsmansaccount")

        else:
            return redirect("/error-with-login")
    else:
        flash('Please fill login and password')

        return render_template('login.html')


@app.route("/treaning_copy")
@login_required
def traning_copy():
    user = User.query.filter_by(login=session.get('login')).first()
    print(user.role_id)
    if user.role_id == "sportsmen":
        return "Вы не тренер"
    else:
        if session.get('login') == "gerard.ismagilov@mail.ru":
            articles = Article.query.order_by(Article.date.desc()).all()
            return render_template("post_copy.html", articles=articles)
        else:
            articles = Article.query.filter_by(creators=session.get('login')).all()
            return render_template("post_copy.html", articles=articles)


@app.route("/blog_copy")
def blog_copy():
    user = User.query.filter_by(login=session.get('login')).first()
    print(user.role_id)
    if user.role_id == "sportsmen":
        return "Вы не тренер"
    if session.get('login') == 'gerard.ismagilov@mail.ru':
        articles = Blog.query.order_by(Blog.date.desc()).all()
        return render_template("news_copy.html", articles=articles)
    else:
        return "Вы еще не можете удалять чужие новости"

@app.route("/weektrain_copy")
def week_copy():
    user = User.query.filter_by(login=session.get('login')).first()
    print(user.role_id)
    if user.role_id == "sportsmen":
        return "Вы не тренер"
    else:
        if session.get('login') == 'gerard.ismagilov@mail.ru':
            articles = Weektrainer.query.order_by(Weektrainer.date.desc()).all()

            return render_template("weektrainer_copy.html", articles=articles)
        else:
            articles = Weektrainer.query.filter_by(creators=session.get('login')).all()
            return render_template("weektrainer_copy.html", articles=articles)


@app.route("/XXLtrain_copy")
def XXL_copy():
    user = User.query.filter_by(login=session.get('login')).first()
    print(user.role_id)
    if user.role_id == "sportsmen":
        return "Вы не тренер"
    else:
        if session.get('login') == 'gerard.ismagilov@mail.ru':
            articles = XXLtrainer.query.order_by(XXLtrainer.date.desc()).all()

            return render_template("XXLtrainer_copy.html", articles=articles)
        else:
            articles = Weektrainer.query.filter_by(creators=session.get('login')).all()
            return render_template("XXLtrainer_copy.html", articles=articles)



@app.route("/treaning")
def treaning():
    try:
        base = ""
        print(11111)
        print(session.get('role'))
        if session.get('role') == "coach":
            base = "baseforaccaunt.html"
        if session.get('role') == "":
            base = "base.html"
        if session.get('role') == "sportsmen":
            base = "baseforsporsman.html"
        articles = Article.query.order_by(Article.date.desc()).all()
        saved = Saved.query.filter_by(saved_login=session.get("login")).all()
        myfollow = []
        for save in saved:
            if save.id_post not in myfollow:
                myfollow.append(save.id_post)
        print(myfollow)

        return render_template("post.html", articles=articles, follower=myfollow, base=base)
    except:
        base = "base.html"
        print(911)
        articles = Article.query.order_by(Article.date.desc()).all()
        saved = Saved.query.filter_by(saved_login=session.get("login")).all()
        myfollow = []
        for save in saved:
            if save.id_post not in myfollow:
                myfollow.append(save.id_post)
        print(myfollow)

        return render_template("post.html", articles=articles, follower=myfollow, base=base)




@app.route("/weektraining")
def weektreaning():
    try:
        base = ""
        print(11111)
        print(session.get('role'))
        if session.get('role') == "coach":
            base = "baseforaccaunt.html"
        if session.get('role') == "":
            base = "base.html"
        if session.get('role') == "sportsmen":
            base = "baseforsporsman.html"
        articles = Weektrainer.query.order_by(Weektrainer.date.desc()).all()
        saved = WeekSaved.query.filter_by(saved_login=session.get("login")).all()
        myfollow = []
        for save in saved:
            if save.id_post not in myfollow:
                myfollow.append(save.id_post)
        print(myfollow)

        return render_template("weektrainer.html", articles=articles, follower=myfollow, base=base)
    except:
        base = "base.html"
        print(911)
        articles = Weektrainer.query.order_by(Weektrainer.date.desc()).all()
        saved = WeekSaved.query.filter_by(saved_login=session.get("login")).all()
        myfollow = []
        for save in saved:
            if save.id_post not in myfollow:
                myfollow.append(save.id_post)
        print(myfollow)

        return render_template("weektrainer.html", articles=articles, follower=myfollow, base=base)




@app.route("/XXLtraining")
def xxltreaning():
    try:
        base = ""
        print(11111)
        print(session.get('role'))
        if session.get('role') == "coach":
            base = "baseforaccaunt.html"
        if session.get('role') == "":
            base = "base.html"
        if session.get('role') == "sportsmen":
            base = "baseforsporsman.html"
        articles = XXLtrainer.query.order_by(XXLtrainer.date.desc()).all()
        saved = XXLSaved.query.filter_by(saved_login=session.get("login")).all()
        myfollow = []
        for save in saved:
            if save.id_post not in myfollow:
                myfollow.append(save.id_post)
        print(myfollow)

        return render_template("XXLtrainer.html", articles=articles, follower=myfollow, base=base)
    except:
        base="base.html"
        articles = XXLtrainer.query.order_by(Weektrainer.date.desc()).all()
        saved = XXLSaved.query.filter_by(saved_login=session.get("login")).all()
        myfollow = []
        for save in saved:
            if save.id_post not in myfollow:
                myfollow.append(save.id_post)
        print(myfollow)

        return render_template("XXLtrainer.html", articles=articles, follower=myfollow, base=base)



@app.route("/treaningdel/<int:id>")
@login_required
def traning_del(id):
    article = Article.query.get_or_404(id)
    if article.creators == session.get('login') or session.get('login') == "gerard.ismagilov@mail.ru":
        try:
            db.session.delete(article)
            db.session.commit()
            return redirect("/account")
        except:
            return "При удалении статьи произошла ошибка"
    else:
        return "А фиг те, не ты ее писал"


@app.route("/newsdel/<int:id>")
@login_required
def news_del(id):
    article = Blog.query.get_or_404(id)

    try:
        db.session.delete(article)
        db.session.commit()
        return redirect("/account")
    except:
        return "При удалении статьи произошла ошибка"

@app.route("/weekdel/<int:id>")
@login_required
def week_del(id):
    article = Weektrainer.query.get_or_404(id)

    try:
        db.session.delete(article)
        db.session.commit()
        return redirect("/account")
    except:
        return "При удалении статьи произошла ошибка"

@app.route("/XXLdel/<int:id>")
@login_required
def XXL_del(id):
    article = XXLtrainer.query.get_or_404(id)

    try:
        db.session.delete(article)
        db.session.commit()
        return redirect("/account")
    except:
        return "При удалении статьи произошла ошибка"


@app.route("/treaning/<int:id>")
def traning_details(id):
    session['train'] = id
    return redirect("/trainigDetail")



@app.route("/trainigDetail")
def traning_detail():
    try:
        base = ""
        print(11111)
        print(session.get('role'))
        if session.get('role') == "coach":
            base = "baseforaccaunt.html"
        if session.get('role') == "":
            base = "base.html"
        if session.get('role') == "sportsmen":
            base = "baseforsporsman.html"

        article = Article.query.get(session.get("train"))
        print(session.get("train"))
        print(article.type)

        saved = Saved.query.filter_by(saved_login=session.get("login")).all()
        myfollow = []
        for save in saved:
            if save.id_post not in myfollow:
                myfollow.append(save.id_post)
        print(myfollow)
        if article.type == "Платная":
            print(article.type)
            return article.cost
        else:
            print(100)
            return render_template("trainingDetail.html", articles=article, base=base, follower=myfollow)
    except:
        base = "base.html"
        print(911)
        articles = Article.query.get(session.get("train"))

        return render_template("trainingDetail.html", articles=articles, base=base)


@app.route("/weektreaning/<int:id>")
def weektraning_details(id):
    session['weektrain'] = id
    return redirect("/weektrainigDetail")


@app.route("/weektrainigDetail")
def weektraning_detail():
    try:
        base = ""
        print(11111)
        print(session.get('role'))
        if session.get('role') == "coach":
            base = "baseforaccaunt.html"
        if session.get('role') == "":
            base = "base.html"
        if session.get('role') == "sportsmen":
            base = "baseforsporsman.html"


        articles = Weektrainer.query.order_by(Weektrainer.date.desc()).all()
        saved = WeekSaved.query.filter_by(saved_login=session.get("login")).all()
        myfollow = []
        for save in saved:
            if save.id_post not in myfollow:
                myfollow.append(save.id_post)
        print(myfollow)
        article = Weektrainer.query.get(session.get("weektrain"))
        if article.type == "Платная":
            print(article.type)
            return article.cost
        else:
            return render_template("weeksearchDetail.html", articles=article, base=base, follower=myfollow)
    except:
        base = "base.html"
        print(911)
        articles = Weektrainer.query.get(id)
        return render_template("weeksearchDetail.html", articles=articles, base=base)


@app.route("/XXLtreaning/<int:id>")
def xxltraning_details(id):
    session['xxltrain'] = id
    return redirect("/xxltrainigDetail")



@app.route("/xxltrainigDetail")
def XXLtraning_detail():
    try:
        base = ""
        print(11111)
        print(session.get('role'))
        if session.get('role') == "coach":
            base = "baseforaccaunt.html"
        if session.get('role') == "":
            base = "base.html"
        if session.get('role') == "sportsmen":
            base = "baseforsporsman.html"
        articles = XXLtrainer.query.get(session.get("xxltrain"))
        saved = XXLSaved.query.filter_by(saved_login=session.get("login")).all()
        myfollow = []
        for save in saved:
            if save.id_post not in myfollow:
                myfollow.append(save.id_post)
        print(myfollow)

        if articles.type == "Платная":
            print(articles.type)
            return articles.cost
        else:
            return render_template("XXLsearchDetail.html", articles=articles, base=base, follower=myfollow)
    except:
        base = "base.html"
        print(911)
        articles = XXLtrainer.query.get(id)
        saved = XXLSaved.query.filter_by(saved_login=session.get("login")).all()
        myfollow = []
        for save in saved:
            if save.id_post not in myfollow:
                myfollow.append(save.id_post)
        print(myfollow)
        return render_template("XXLsearchDetail.html", articles=articles, base=base, follower=myfollow)



@app.route("/treanerserch")
def treanersearch():
    try:
        base = ""
        print(11111)
        print(session.get('role'))
        if session.get('role') == "coach":
            base = "baseforaccaunt.html"
        if session.get('role') == "":
            base = "base.html"
        if session.get('role') == "sportsmen":
            base = "baseforsporsman.html"
        only_coach_accounts = User.query.filter_by(role_id='coach').all()
        subs = Follow.query.filter_by(followed_login=session.get("login"))
        follower = []
        for sub in subs:
            if sub.follower_login not in follower:
                print(sub.follower_login)
                follower.append(sub.follower_login)
        print(follower)
        return render_template("treanersearch.html ", accounts=only_coach_accounts, follower=follower, base=base)
    except:
        base = "base.html"
        print(911)
        only_coach_accounts = User.query.filter_by(role_id='coach').all()
        subs = Follow.query.filter_by(followed_login=session.get("login"))
        follower = []
        for sub in subs:
            if sub.follower_login not in follower:
                print(sub.follower_login)
                follower.append(sub.follower_login)
        print(follower)
        return render_template("treanersearch.html ", accounts=only_coach_accounts, follower=follower, base=base)


@app.route("/treanersearch/<int:id>")
def treansearh(id):
    session['searchofcoach'] = id
    return redirect("/treanersearchid")





@app.route("/treanersearchid")
def treaner_detail():


    try:

        base = ""
        print(11111)
        print(session.get('role'))
        if session.get('role') == "coach":
            base = "baseforaccaunt.html"
        if session.get('role') == "":
            base = "base.html"
        if session.get('role') == "sportsmen":
            base = "baseforsporsman.html"
        account = User.query.get_or_404(session.get("searchofcoach"))
        login = account.login
        articles = Article.query.filter_by(creators=login)
        articles1 = Weektrainer.query.filter_by(creators=login)
        articles2 = XXLtrainer.query.filter_by(creators=login)
        saved = Saved.query.filter_by(saved_login=session.get("login")).all()
        myfollow = []
        for save in saved:
            if save.id_post not in myfollow:
                myfollow.append(save.id_post)

        saved1 = WeekSaved.query.filter_by(saved_login=session.get("login")).all()
        myfollow1 = []
        for save in saved1:
            if save.id_post not in myfollow:
                myfollow1.append(save.id_post)

        saved2 = XXLSaved.query.filter_by(saved_login=session.get("login")).all()
        myfollow2 = []
        for save in saved2:
            if save.id_post not in myfollow2:
                myfollow2.append(save.id_post)

        user = User.query.filter_by(login=login).first()

        return render_template("treaner1searchDetail.html", account=user, base=base, articles=articles,
                                   articles1=articles1, articles2=articles2, follower=myfollow,
                                   follower1=myfollow1, follower2=myfollow2)


    except:
        base = "base.html"
        print(911)
        return render_template("treanersearchDetail.html", account=account, base=base)




@app.route("/subscribe/<int:id>")
def subscribe(id):
    account = User.query.filter_by(id=id).first()
    login = account.login
    print(login)
    user = Follow.query.filter_by(follower_login=login).first()

    print("OK")
    follow = Follow(follower_login=login, followed_login=session.get('login'))

    db.session.add(follow)
    db.session.commit()
    return redirect("/treanerserch")


@app.route("/subscribedel/<int:id>")
def subscribedel(id):
    account = User.query.get_or_404(id)
    login = account.login
    print(login)

    follow = Follow.query.filter_by(follower_login=login, followed_login=session.get('login')).first()
    print("OK")

    db.session.delete(follow)
    db.session.commit()

    return redirect("/treanerserch")


@app.route("/forme")
def postforme():
    try:
        base = ""
        print(11111)
        print(session.get('role'))
        if session.get('role') == "coach":
            base = "baseforaccaunt.html"
        if session.get('role') == "":
            base = "base2.html"
        if session.get('role') == "sportsmen":
            base = "baseforsporsman.html"
        posts = []
        post = Follow.query.filter_by(followed_login=session.get("login")).all()

        print(session.get("login"))
        print(11)
        for article in post:
            arts = Article.query.filter_by(creators=article.follower_login).all()
            print(article.follower_login)
            for art in arts:
                posts.append(art)

        return render_template("forme.html", articles=posts, base=base)
    except:
        base = "base2.html"
        print(911)
        posts = []
        post = Follow.query.filter_by(followed_login=session.get("login")).all()

        print(session.get("login"))
        print(11)
        for article in post:
            arts = Article.query.filter_by(creators=article.follower_login).all()
            print(article.follower_login)
            for art in arts:
                posts.append(art)

        return render_template("forme.html", articles=posts, base=base)



@app.route("/error-with-login")
def errorlogin():
    return render_template("Error with login.html")


@app.route("/error-with-registration")
def errorregistration():
    return render_template("Error with regisration.html")


@app.route("/account")
@login_required
def account():
    posts = []
    post = Saved.query.filter_by(saved_login=session.get("login")).all()

    print(session.get("login"))
    print(11)
    for article in post:
        arts = Article.query.filter_by(creators=article.saver_login).all()
        print(article.saver_login)
        for art in arts:
            posts.append(art)
    account = session.get(session.get('id'))

    articles = Weektrainer.query.order_by(Weektrainer.date.desc()).all()
    saved = WeekSaved.query.filter_by(saved_login=session.get("login")).all()
    myfollow = []
    for save in saved:
        if save.id_post not in myfollow:
            myfollow.append(save.id_post)
    print(myfollow)

    return render_template("account.html", user=account, article=post, follower=myfollow)


@app.route("/sportsmansaccount")
@login_required
def spsaccount():
    if session.get('role') == "coach":
        base = "baseforaccaunt.html"
    if session.get('role') == "":
        base = "base2.html"
    if session.get('role') == "sportsmen":
        base = "baseforsporsman.html"
    account = session.get('id')
    articles = Article.query.order_by(Article.date.desc()).all()
    saved = Saved.query.filter_by(saved_login=session.get("login")).all()
    myfollow = []
    for save in saved:
        if save.id_post not in myfollow:
            myfollow.append(save.id_post)
    print(myfollow)

    articles1 = Weektrainer.query.order_by(Weektrainer.date.desc()).all()
    saved1 = WeekSaved.query.filter_by(saved_login=session.get("login")).all()
    myfollow1 = []
    for save in saved1:
        if save.id_post not in myfollow1:
            myfollow1.append(save.id_post)
    print(myfollow1)
    articles2 = XXLtrainer.query.order_by(XXLtrainer.date.desc()).all()
    saved2 = XXLSaved.query.filter_by(saved_login=session.get("login")).all()
    myfollow2 = []
    for save in saved2:
        if save.id_post not in myfollow2:
            myfollow2.append(save.id_post)
    print(myfollow2)

    return render_template("oncesaved.html", user=account, articles=articles, myfollow=myfollow,
                           follower=myfollow1, articles1=articles1, follower2=myfollow2, articles2=articles2, base=base)


@app.route("/savedweek")
@login_required
def savedweek():
    if session.get('role') == "coach":
        base = "baseforaccaunt.html"
    if session.get('role') == "":
        base = "base2.html"
    if session.get('role') == "sportsmen":
        base = "baseforsporsman.html"
    account = session.get('id')
    articles = Article.query.order_by(Article.date.desc()).all()
    saved = Saved.query.filter_by(saved_login=session.get("login")).all()
    myfollow = []
    for save in saved:
        if save.id_post not in myfollow:
            myfollow.append(save.id_post)
    print(myfollow)

    articles1 = Weektrainer.query.order_by(Weektrainer.date.desc()).all()
    saved1 = WeekSaved.query.filter_by(saved_login=session.get("login")).all()
    myfollow1 = []
    for save in saved1:
        if save.id_post not in myfollow1:
            myfollow1.append(save.id_post)
    print(myfollow1)
    articles2 = XXLtrainer.query.order_by(XXLtrainer.date.desc()).all()
    saved2 = XXLSaved.query.filter_by(saved_login=session.get("login")).all()
    myfollow2 = []
    for save in saved2:
        if save.id_post not in myfollow2:
            myfollow2.append(save.id_post)
    print(myfollow2)

    return render_template("weeksaved.html", user=account, articles=articles, myfollow=myfollow,
                           follower=myfollow1, articles1=articles1, follower2=myfollow2, articles2=articles2, base=base)



@app.route("/savedmonth")
@login_required
def savedmonth():
    print(session.get("role"))

    if session.get('role') == "coach":
        base = "baseforaccaunt.html"
    if session.get('role') == "":
        base = "base2.html"
    if session.get('role') == "sportsmen":
        base = "baseforsporsman.html"
    account = session.get('id')
    articles = Article.query.order_by(Article.date.desc()).all()
    saved = Saved.query.filter_by(saved_login=session.get("login")).all()
    myfollow = []
    for save in saved:
        if save.id_post not in myfollow:
            myfollow.append(save.id_post)
    print(myfollow)

    articles1 = Weektrainer.query.order_by(Weektrainer.date.desc()).all()
    saved1 = WeekSaved.query.filter_by(saved_login=session.get("login")).all()
    myfollow1 = []
    for save in saved1:
        if save.id_post not in myfollow1:
            myfollow1.append(save.id_post)
    print(myfollow1)
    articles2 = XXLtrainer.query.order_by(XXLtrainer.date.desc()).all()
    saved2 = XXLSaved.query.filter_by(saved_login=session.get("login")).all()
    myfollow2 = []
    for save in saved2:
        if save.id_post not in myfollow2:
            myfollow2.append(save.id_post)
    print(myfollow2)

    return render_template("monthsaved.html", user=account, articles=articles, myfollow=myfollow,
                           follower=myfollow1, articles1=articles1, follower2=myfollow2, articles2=articles2, base=base)


@app.route("/search", methods=['POST', 'GET'])
def search():
    base = ""
    print(11111)
    print(session.get('role'))
    if session.get('role') == "coach":
        base = "baseforaccaunt.html"
    if session.get('role') == "":
        base = "base.html"
    if session.get('role') == "sportsmen":
        base = "baseforsporsman.html"
    if request.method == 'POST':
        login = request.form['login']
        articles = Article.query.filter_by(creators=login)
        articles1 = Weektrainer.query.filter_by(creators=login)
        articles2 = XXLtrainer.query.filter_by(creators=login)
        saved = Saved.query.filter_by(saved_login=session.get("login")).all()
        myfollow = []
        for save in saved:
            if save.id_post not in myfollow:
                myfollow.append(save.id_post)

        saved1 = WeekSaved.query.filter_by(saved_login=session.get("login")).all()
        myfollow1 = []
        for save in saved1:
            if save.id_post not in myfollow:
                myfollow1.append(save.id_post)

        saved2 = XXLSaved.query.filter_by(saved_login=session.get("login")).all()
        myfollow2 = []
        for save in saved2:
            if save.id_post not in myfollow2:
                myfollow2.append(save.id_post)
        try:
            user = User.query.filter_by(login=login).first()

            return render_template("treaner1searchDetail.html", account=user, base=base, articles=articles, articles1=articles1, articles2=articles2, follower=myfollow,
                                   follower1=myfollow1, follower2=myfollow2)
        except:
            return "Такого тренера нет"
    else:

        return render_template("search.html", base=base)




@app.route("/searcht/<int:id>")
def searchf(id):
    base = ""
    print(11111)
    print(session.get('role'))
    if session.get('role') == "coach":
        base = "baseforaccaunt.html"
    if session.get('role') == "":
        base = "base2.html"
    if session.get('role') == "sportsmen":
        base = "baseforsporsman.html"
    if request.method == 'POST':
        login = request.form['login']
        articles = Article.query.filter_by(creators=login)
        articles1 = Weektrainer.query.filter_by(creators=login)
        articles2 = XXLtrainer.query.filter_by(creators=login)
        saved = Saved.query.filter_by(saved_login=session.get("login")).all()
        myfollow = []
        for save in saved:
            if save.id_post not in myfollow:
                myfollow.append(save.id_post)

        saved1 = WeekSaved.query.filter_by(saved_login=session.get("login")).all()
        myfollow1 = []
        for save in saved1:
            if save.id_post not in myfollow:
                myfollow1.append(save.id_post)

        saved2 = XXLSaved.query.filter_by(saved_login=session.get("login")).all()
        myfollow2 = []
        for save in saved2:
            if save.id_post not in myfollow2:
                myfollow2.append(save.id_post)
        try:
            user = User.query.filter_by(login=login).first()

            return render_template("treaner1searchDetail.html", account=user, base=base, articles=articles, articles1=articles1, articles2=articles2, follower=myfollow,
                                   follower1=myfollow1, follower2=myfollow2)
        except:
            return "Такого тренера нет"
    else:

        return render_template("search.html", base="base2.html")



@app.route("/aboutforcoach")
def infoforcoach():

    return render_template("abouforcoach.html")

# overade>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# overade>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# overade>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@app.route("/account/")
def aindex():
    articles = Blog.query.order_by(Blog.date.desc()).all()
    return render_template("newsa.html", articles=articles)


video = []
@app.route("/motivation")
def mativation():

    return render_template("motivation.html", video=video)

if __name__ == '__main__':
    import os

    app.run(debug=True)
