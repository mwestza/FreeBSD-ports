--- archivebox/core/apps.py.orig	2022-12-24 07:28:57.119930000 +0000
+++ archivebox/core/apps.py	2022-12-24 07:29:09.350757000 +0000
@@ -3,4 +3,4 @@
 
 class CoreConfig(AppConfig):
     name = 'core'
-    default_auto_field = 'django.db.models.UUIDField'
+    default_auto_field = 'django.db.models.BigAutoField'
