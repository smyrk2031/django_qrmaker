from django.db import models
import io
from PIL import Image
import datetime

# QR画像生成時に一時保存する
class temp_image(models.Model):
    # id
    image_id = models.IntegerField("qrimg_id", blank=True, null=True, default=0)
     # 最終更新日
    regist_date = models.DateTimeField('日時', blank=True, null=True, default=datetime.datetime.now())
    # QRコード画像
    image = models.ImageField(upload_to='images/', blank=True, null=True)

# 登録
class regist_table(models.Model):
    # id
    regist_id = models.IntegerField('リダイレクトカウント', blank=True, null=True, default=0)
    # タイトル
    title = models.CharField('タイトル', max_length=512, null=True, blank=True, default='')
    # テキスト
    text = models.CharField('テキスト', max_length=512, null=True, blank=True, default='')
    # 最終更新日
    regist_date = models.DateTimeField('日時', blank=True, null=True, default=datetime.datetime.now())
    # 最終更新ユーザーID
    user_id = models.IntegerField('リダイレクトカウント', blank=True, null=True, default=0)
    # 短縮URL
    my_shorturl = models.CharField('短縮URL', max_length=50, null=True, blank=True, default='')
    # 元URL_使用中
    my_seturl = models.CharField('設定URL', max_length=512, null=True, blank=True, default='')
    # 元URL_履歴
    my_seturl_hist = models.CharField('設定URLの履歴', max_length=512, null=True, blank=True, default='')
    # アクセス数カウント: SUM
    redirect_count = models.IntegerField('アクセスカウント', blank=True, null=True, default=0)
    # QRコード画像
    image = models.ImageField(upload_to='images/', blank=True, null=True)


class UploadImage(models.Model):
    image = models.ImageField(upload_to='img_temp/')
    
    def transform(self, angle, gray):

        # アップロードされたファイルから画像オブジェクト生成
        org_img = Image.open(self.image)

        # PILでの画像処理ここから！
        ret_img = org_img.rotate(angle)

        if gray:
            ret_img = ret_img.convert('L')
        # PILでの画像処理ここまで！

        # 画像処理後の画像のデータをbufferに保存
        buffer = io.BytesIO()
        ret_img.save(fp=buffer, format=org_img.format)

        # 以前保存した画像処理後の画像ファイルを削除
        self.result.delete()

        # bufferのデータをファイルとして保存（レコードの更新も行われる）
        self.result.save(name=self.image.name, content=buffer)