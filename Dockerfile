# Docker Hubにあるpythonイメージをベースにする
FROM python:3.7-alpine

# 環境変数を設定する
ENV PYTHONUNBUFFERED 1

# コンテナ内にcodeディレクトリを作り、そこをワークディレクトリとする
RUN mkdir /app
WORKDIR /app

# ホストPCにあるrequirements.txtをコンテナ内のcodeディレクトリにコピーする
# コピーしたrequirements.txtを使ってパッケージをインストールする
ADD requirements.txt /app/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# ホストPCの各種ファイルをcodeディレクトリにコピーする
ADD . /app/
