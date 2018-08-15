#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 8/10/18 4:11 PM
# @Author  : bai yang
# @Site    : 
# @File    : run.py
# @Software: PyCharm
from article.settings import app
from article import first_page_bp
from aoiklivereload import LiveReloader

reloader = LiveReloader()
reloader.start_watcher_thread()


@app.middleware('response')
async def custom_banner(request, response):
    pass
    # response.headers["content-type"] = "application/json"


app.blueprint(first_page_bp)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
