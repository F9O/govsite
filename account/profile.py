#encoding=utf-8
import web
from common import render
from account.auth import is_logined, authenticate, login as auth_login, logout as auth_logout,\
        ERR_USER_NOTEXISTS, ERR_OK, ERR_PASSWORD_NOTCORRECT
from account.dbutil import save_user
from account.form import login_form


class signup:
    def GET(self):
        if is_logined():
            raise web.seeother('/')
        return render.signup()

    def POST(self):
        data = web.input()
        save_user(-1, data)
        raise web.seeother('/')


class login:
    def GET(self):
        if is_logined():
            raise web.seeother('/')
        redirect_url = ""
        data = web.input()
        if 'redirect_to' in data:
            redirect_url = data.redirect_to
        form = login_form()
        req = web.ctx.req
        req.update({
            'form': form,
            'redirect_url': redirect_url,
            })
        return render.login(**req)

    def POST(self):
        form = login_form()
        if not form.validates():
            return render.login(form=form)
        data = web.input()
        errcode, user = authenticate(data.username, data.password)
        req = web.ctx.req
        if errcode != ERR_OK:
            if errcode == ERR_USER_NOTEXISTS:
                req.err(u'User is not exists!')
            elif errcode == ERR_PASSWORD_NOTCORRECT:
                req.err(u'password error!')
            if 'redirect_to' in data:
                redirect_url = data.redirect_to
            req.update({
                'form': form,
                'redirect_url': redirect_url,
                })
            return render.login(**req)
        auth_login(user)
        redirect_url = data.redirect_to
        if redirect_url:
            raise web.seeother(redirect_url)
        else:
            raise web.seeother('/', True)

class logout:
    def GET(self):
        auth_logout()
        raise web.seeother('/', True)

class reset:
    def GET(self):
        session.login = 0
        session.privilege = 0
        render = create_render(session.privilege)
        return "%s" % (render.logout())
