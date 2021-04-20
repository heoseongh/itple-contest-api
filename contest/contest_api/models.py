from django.db import models


class Contest(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=1000)
    desc = models.CharField(max_length=500000)
    pub_date = models.DateTimeField('data published')
    #organizer = models.ForeignKey

    # 각 데이터가 어떻게 넘어오는지 알아야하는것 아닌가
    # 데이터 타입이 다르면 안 되겠지?
    

    # tags ?
    #requirements
    #rewards

    # date
    
    
    #start_date
    #end_date

    #view_count


"""
외부 서비스의 모델
contest - organizer

"""