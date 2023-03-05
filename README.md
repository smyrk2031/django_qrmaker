# django_qrmaker
description: english

An application that converts any character string into a QR code. There is a UUID1 conversion function for strings and a database management function,

description: japanize

任意の文字列をQRコードに変換するアプリ。文字列のUUID1化機能とデータベース管理機能があります


◆Application Env

Python 3.9.10
Django 4.1.7
django-bootstrap4 22.3
Pillow 9.4.0
qrcode 7.4.2


◆主な機能

No1

・QRコードの作成と登録は、HTML上の同一のFormタグを使っており、どちらのボタンもjqueryのAjaxを使っている為、
　どちらのボタンが押されたのかをIDで確認して、実行するAjaxの動作を変化させている。
・QR code creation and registration use the same Form tag on HTML, and both buttons use jquery Ajax,
By checking which button was pressed by ID, the Ajax operation to be executed is changed.

https://user-images.githubusercontent.com/43007654/222945343-f8771996-1ba9-4f77-9a42-6c853e45ced3.mp4

