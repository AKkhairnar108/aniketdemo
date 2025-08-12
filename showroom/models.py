from django.db import models
#models are ORM system.define structure of database tables
#and serve as interface for interacting with database data.
#Each model class maps a single table in database and each
#attribute of class represents a field(column) in that table.
# Create your models here.
class Bike(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    price = models.IntegerField()
    def __str__(self):#this name can show on database.
        return f"{self.name}"

#in views we call as:
#books=Book.objects.all()
#for create
# #book=Book.objects.create(title='aniket',author=my_author)
#for update
# book=Book.objects.get(id=1)
# book.title='Advance Django'
# book.save()
# for delete
# book=Book.objects.get(id=1)
# book.delete()