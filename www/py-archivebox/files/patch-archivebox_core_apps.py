--- archivebox/core/apps.py.orig	2021-04-10 11:42:34 UTC
+++ archivebox/core/apps.py
@@ -3,4 +3,4 @@ from django.apps import AppConfig
 
 class CoreConfig(AppConfig):
     name = 'core'
-    default_auto_field = 'django.db.models.UUIDField'
+    default_auto_field = 'django.db.models.BigAutoField'
