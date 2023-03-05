<h1>django_qrmaker</h1>
<h3>description: english</h3>

An application that converts any character string into a QR code. There is a UUID1 conversion function for strings and a database management function,

<h3>description: japanize</h3>

任意の文字列をQRコードに変換するアプリ。文字列のUUID1化機能とデータベース管理機能があります

<hr>
<h3>◆Application Env</h3>

Python 3.9.10
Django 4.1.7
django-bootstrap4 22.3
Pillow 9.4.0
qrcode 7.4.2

<hr>
<h3 style="color:red;">◆主な機能</h3>

No1

・QRコードの作成と登録は、HTML上の同一のFormタグを使っており、どちらのボタンもjqueryのAjaxを使っている為、
　どちらのボタンが押されたのかをIDで確認して、実行するAjaxの動作を変化させている。
・QR code creation and registration use the same Form tag on HTML, and both buttons use jquery Ajax,
By checking which button was pressed by ID, the Ajax operation to be executed is changed.

<hr>
<h2>Djangoアプリのイメージ動画</h2>
https://user-images.githubusercontent.com/43007654/222945343-f8771996-1ba9-4f77-9a42-6c853e45ced3.mp4


<br><hr><hr>
<h2>追加したい機能メモ</h2>
<br>・表示されるQRコードのサイズを任意変更して、読み取りやすさを検証できるようにする
<br>・QRコードの耐環境性能の指標チャートを表示（どれだけ弱いか）
<br>・QRコードに対して汚れ・一部破損フィルタを適応する機能
<br>・検索モードから、登録情報の編集を可能にする（元URLだけを変更してQRコードを使いまわせるようにする機能）
<br><hr><hr>
