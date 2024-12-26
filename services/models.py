from django.db import models

class StudentMobilityCourse(models.Model):
    background_photo = models.ImageField(upload_to='student_mobility_courses/')
    title = models.CharField(max_length=255)
    title_heading_details = models.TextField()
    description = models.TextField()
    courses_included = models.TextField()
    course_contents = models.TextField()
    course_trainer = models.CharField(max_length=255)
    start_date = models.DateField()
    duration = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image1 = models.ImageField(upload_to='student_mobility_courses/')
    image2 = models.ImageField(upload_to='student_mobility_courses/')
    image3 = models.ImageField(upload_to='student_mobility_courses/')
    image1_description = models.CharField(max_length=255, default="Image 1 description",null=True, blank=True)
    image2_description = models.CharField(max_length=255, default="Image 2 description",null=True, blank=True)
    image3_description = models.CharField(max_length=255, default="Image 3 description",null=True, blank=True)
    

    def __str__(self):
        return self.title

