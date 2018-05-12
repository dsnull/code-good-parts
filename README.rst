==============================
Pnの受け側のプロジェクトです。
==============================

GETリクエストを受け取って、DeviceTokenテーブルに
device_tokenと登録年月日を登録します。

試験する時は、
http://<yourhostname>:8000/api/v1/register/?devcice_token=xxxx
で呼び出して下さい。

Pn側から結合する時は、
Pn側の以下ファイルのregister_server_urlのIPアドレス部分を<yourhostname>に置き換えてください。
Pn\app\src\main\res\values\strings.xml

Requirement
===========

:Python: 3.6
:Django: 1.8

Environment
===========
先日Evernoteで公開したメモ参照。

Quick start
===========

#. プロジェクトのクローン::

        git clone https://github.com/dsnull/code-good-parts

#. モデルのmigrate::

        cd code-good-parts
        pytyon3 manage.py migrate

#. サーバプロセスを起動する::

       python3 manage.py runserver 0.0.0.0:8000

Notes
===========

#. 登録されたdevice_tokenの見方::

        http://<yourhostname>:8000/admin/
        へアクセス。
        DeviceTokensをクリックして出てくる一覧の中から
        一番上の行をクリックする。

        但し、認証を要求してくるので、superuserを作っておく。

#. supueruserの作り方::

        python3 manage.py createsuperuser
         
        ユーザ名、メールアドレス、パスワードを要求されるので、
        入力する。

**上記のpython3は、python3.6へのシンボリックリンクです。

**python3.6、django1.8のインストール方法はググって下さい。

