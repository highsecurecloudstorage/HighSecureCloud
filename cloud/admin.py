from django.contrib import admin
from cloud.models import UserProfile,FileShare,FileDetails,TempStorage,FileAccess,MacAddress

admin.site.register(UserProfile)
admin.site.register(FileShare)
admin.site.register(FileDetails)
admin.site.register(TempStorage)
admin.site.register(FileAccess)
admin.site.register(MacAddress)

