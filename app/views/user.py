from flask import Blueprint, render_template, redirect, url_for, current_app, flash, request
from flask_login import login_user, logout_user, current_user, login_required
from app.extensions import db
from app.forms import RegisterForm, LoginForm
from app.email import send_mail
from app.models import User

user = Blueprint('user', __name__)


@user.route('/register/', methods=['POST', 'GET'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        print(form.password.data)
        u = User(username=form.username.data,
                 password=form.password.data,
                 email=form.email.data)
        db.session.add(u)
        db.session.commit()
        token = u.generate_activate_token(expires_in=100)
        send_mail(u.email, '用户注册', 'email/account_activate', token=token, username=u.username)
        flash('激活邮件已发送，请点击链接完成用户激活')
        return redirect(url_for('main.index'))
    return render_template('user/register.html', form=form)


@user.route('/activate/<token>')
def activate(token):
    if User.check_activate_token(token):
        flash('账户激活成功,请登录')
        # TODO: 此处需要删除数据库,但是我不会,呵呵呵
        return redirect(url_for('user.login'))
    else:
        flash('账户激活失败,请重新注册')
        return redirect(url_for('user.register'))


@user.route('/login/', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        u = User.query.filter_by(username=form.username.data).first()
        if u.activation is False:
            flash('请先激活账户')
        else:
            if u is None:
                flash('用户名有误')
                return redirect(url_for('user.login'))
            if u.verify_password(form.password.data):
                login_user(u, remember=form.Remember_password.data)
                flash('登陆成功')
                return redirect(request.args.get('next') or url_for('main.index'))
            else:
                flash('密码有误')
    return render_template('user/login.html', form=form)


@user.route('/logout/')
# 保护路由 必须登录才可以访问
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))


# 退出登录
@user.route('/change_password/')
# 保护路由 必须登录才可以访问
@login_required
def change_password():
    # TODO：此处需要写修改密码
    return render_template('user/change_password.html')


@user.route('/test/')
def test():
    u = User.query.all()
    x = []
    for i in u:
        x.append(i.password)
    return str(x)

# 修改密码
# @user.route('/profile/')
# 保护路由 必须登录才可以访问


# @login_required
# def profile():
#     # TODO：此处需要写用户信息  做展示
#     return render_template('user/profile.html')


# 修改邮箱
@user.route('/change_email/')
# 保护路由 必须登录才可以访问
@login_required
def change_email():
    # TODO：此处需要写修改邮箱
    return render_template('user/change_email.html')


# 修改头像
@user.route('/change_icon/')
# 保护路由 必须登录才可以访问
@login_required
def change_icon():
    # TODO：此处需要写修改头像
    return render_template('user/chang_icon.html')
