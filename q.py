def fun():
	from cloud.models import UserProfile,TempStorage,FileDetails,FileShare,Permission
	FileDet=FileDetails()
	FileDet.fileName='fname'
	FileDet.fileId='0'
	FileDet.save()
	permissioN=Permission()
	current_user=User.objects.get(username='pc')
	user1 = UserProfile.objects.get(user=current_user)
	current_user=User.objects.get(username='test')
	user2 = UserProfile.objects.get(user=current_user)
	fileShare=FileShare()
	fileShare.owner=user1
	fileShare.file_requested=FileDet
	fileShare.save()
	p1=Permission(user=user1)
	p1.save()
	p2=Permission(user=user2)
	p2.save()
	fileShare.permission.add(p1,p2)
	fileShare.save()