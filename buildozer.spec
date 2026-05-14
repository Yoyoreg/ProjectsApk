[app]
title = HomeStore
package.name = homestore
package.domain = org.marcidia

# مسار ملفاتك
source.dir = .
source.include_exts = py,png,jpg,html,css,js

# الأيقونة وشاشة البداية (ارفع ملفات بهذه الأسماء)
icon.filename = icon.png
presplash.filename = splash.png

# القوة الحقيقية: الصلاحيات المتقدمة
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE, CAMERA, ACCESS_FINE_LOCATION

# نسخة أندرويد
android.api = 33
android.minapi = 21
