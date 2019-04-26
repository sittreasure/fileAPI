from django.db import models

class FileType(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=20)
  regularExpression = models.TextField(db_column='regular_expression')
  fileType = models.CharField(max_length=5, db_column='file_type')
  initialCode = models.TextField(null=True, blank=True, db_column='initial_code')
  createdAt = models.DateTimeField(db_column='created_at', auto_now_add=True)
  updatedAt = models.DateTimeField(db_column='updated_at', auto_now=True)

  class Meta:
    db_table = 'FileTypes'

  def __str__(self):
    return 'file type : {name}'.format(name=self.name)
