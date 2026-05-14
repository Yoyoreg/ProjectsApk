from kivy.app import App
from kivy.uix.webview import WebView # قد تحتاج لتعديل بسيط حسب نسخة Buildozer
from kivy.utils import platform

class HomeStoreApp(App):
    def build(self):
        # في أندرويد، نقوم بفتح ملف الـ HTML المحلي
        if platform == 'android':
            from android.webview import WebView
            wv = WebView("file:///android_asset/assets/index.html")
            return wv
        else:
            # للتشغيل التجريبي على الكمبيوتر
            print("التطبيق يعمل الآن كحاوية للمتصفح")

HomeStoreApp().run()
