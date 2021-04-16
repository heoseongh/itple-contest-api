"""
models.Manager() 객체 생성하는 이유
views.py 에서 all명령어를 수행하려면 models.Manager()객체를 받아서 수행해야 한다.
그래서 models.py 에서 models.Manager() 객체를 생성한다.
"""
"""
Contest에 추가할 필드
subtitle
모집기간
시상규모
홈페이지
활동분야
참여대상
우대역량
활동혜택
"""

from django.db import models
class Contest(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=200)
    desc = models.TextField()
    poster = models.ImageField()


#class manager(modles.Model):



#class organizer(modles.Model):
