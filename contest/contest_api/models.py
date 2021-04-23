from django.db import models

#======================== 옵션 설명 ========================#
# auto_now_add=True : 생성일자(최초 생성시 날짜 저장, 수정 불가능)
# auto_now=True     : 수정일자(모델이 save 될 때마다 현재 날짜로 갱신)

# 공모전 모델
class Contest(models.Model):
    objects = models.Manager()
    # id = models.BigAutoField(help_text="Contest ID", primary_key=True)
    title = models.CharField(help_text="Contest Title", max_length=200)
    imageUrl = models.CharField(help_text="Contest ImageUrl", max_length=300)
    tags = models.JSONField(help_text="Contest Tag", max_length=500)
    summary = models.JSONField(help_text="Contest Summary", max_length=500)
    detail = models.JSONField(help_text="Contest Detail", max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)

    def __str__(self):
        return self.title


#====================== 삽질 NOTE =====================#
# 아래는 왜래키로 상세정보 조인하는 방법이다. 이렇게 할 필요가 없었다...
# 그냥 Array는 ["value1","value2"], Object는 [{"key" : "value"}] 이렇게 받으면 된다.
# 즉, 그냥 받아오는 JSON 데이터 그대로 통째로 저징하면 된다.
# 아래 객체 조인하는 방법은 나중에 쓸 일이 있을 것이니 참고.

#=====================================================#
# # 상세정보
# class Detail(models.Model):
#     objects = models.Manager()
#     id = models.BigAutoField(help_text="Detail ID", primary_key=True)
#     # "contest_id" 필드에 db_column 을 설정해주지 않으면 자동으로 뒤에 "_id" 가 붙어서 필드명이 "contest_id_id" 가 된다.
#     contest_id = models.ForeignKey("Contest", related_name="detail", on_delete=models.CASCADE, db_column="contest_id")
#     마감기한 = models.CharField(help_text="Detail 마감기한", max_length=12)
#     지원자격 = models.CharField(help_text="Detail 지원자격", max_length=500)
#     대회일정 = models.CharField(help_text="Detail 대회일정", max_length=500)
#     상금 = models.CharField(help_text="Detail 상금", max_length=500)
#     홈페이지 = models.CharField(help_text="Detail 홈페이지", max_length=200)

# # 요약정보
# class Summary(models.Model):
#     objects = models.Manager()
#     id = models.BigAutoField(help_text="Summary ID", primary_key=True)
#     contest_id = models.ForeignKey("Contest", related_name="summary", on_delete=models.CASCADE, db_column="contest_id")
#     기관 = models.CharField(help_text="Summary 기관", max_length=100)
#     상금 = models.CharField(help_text="Summary 상금", max_length=100)
